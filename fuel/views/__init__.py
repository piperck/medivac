# coding: utf-8
from flask import Blueprint


medivac = Blueprint(
    'medivac',
    __name__,
    template_folder='templates',
    static_folder='static')

import fuel.views.hello
