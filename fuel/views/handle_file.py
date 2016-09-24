# coding: utf-8
from flask import request
from fuel.views import medivac
from fuel.broker.handle_file import generate_uri_from_put


@medivac.route("/<file_name>", methods=["POST", "PUT"])
def handle_upload_file(file_name):
    if request.method == "PUT":
        real_file = request.data
        file_uri = generate_uri_from_put(file_name, real_file)
        return file_uri
