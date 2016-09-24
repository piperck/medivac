# coding: utf-8
from flask import request
from fuel.views import medivac


@medivac.route("/<file_name>", method=["POST"])
def handle_upload_file(file_name):
    extension_name = file_name.rsplit(".")[1]
    file = request.files.get(file_name)
    return 0
