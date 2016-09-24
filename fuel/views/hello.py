# coding: utf-8
from fuel.views import medivac


@medivac.route("/")
def hello():
    return "let's move!"


@medivac.route("/medivac")
def hello_some_one():
    return "let's move medivac!"
