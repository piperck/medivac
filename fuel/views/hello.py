from fuel.views import medivac


@medivac.route("/")
def hello():
    return "let's move!"