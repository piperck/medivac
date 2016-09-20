from medivac.app import app


@app.route("/")
def hello():
    return "let's move!"
