import os
from functools import wraps

from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from modules.search_engine import ShadowDoxEngine

load_dotenv()

app = Flask(
    __name__,
    template_folder="modules/templates/templates",
    static_folder="modules/templates/templates/static",
)

app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "dev-only-change-this-secret"
)

APP_PASSWORD = os.getenv("SHADOWDOX_PASSWORD", "Nathan")

engine = ShadowDoxEngine()


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get("authenticated"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped_view


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("authenticated"):
        return redirect(url_for("index"))

    if request.method == "POST":
        password = request.form.get("password", "")

        if password == APP_PASSWORD:
            session.clear()
            session["authenticated"] = True
            return redirect(url_for("index"))

        flash("Mot de passe incorrect.", "danger")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    results = None

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            results = engine.search(query)
        else:
            flash("Entre quelque chose à rechercher.", "warning")

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=False,
    )
  
