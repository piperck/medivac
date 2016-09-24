# coding: utf-8
from fuel.views import medivac


@medivac.route("/")
def hello():
    return "let's move!"


@medivac.route("/<some_one>")
def hello(some_one):
    return "let's move %s!" % some_one
