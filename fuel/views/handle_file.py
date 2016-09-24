# coding: utf-8
from flask import request
from fuel.views import medivac
from fuel.broker.handle_file import generate_uri


@medivac.route("/<file_name>", method=["POST"])
def handle_upload_file(file_name):
    real_file = request.files.get(file_name)
    file_uri = generate_uri(file_name, real_file)

    return file_uri
