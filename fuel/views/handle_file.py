# coding: utf-8
from flask import request
from fuel.const import MaxFile
from fuel.views import medivac
from fuel.broker.handle_file import generate_uri_from_put


@medivac.route("/<file_name>", methods=["POST", "PUT"])
def handle_upload_file(file_name):
    if request.method == "PUT":
        real_file = request.get_data(as_text=True)
        if len(real_file) > MaxFile.MAX_CONTENT_LENGTH:
            return "Too big file, your file must less than %s byte for now :);" % MaxFile.MAX_CONTENT_LENGTH

        file_uri = generate_uri_from_put(str(file_name), real_file)

        return file_uri
