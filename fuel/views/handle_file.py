# coding: utf-8
from flask import request
from fuel.const import MaxFile
from fuel.views import medivac
from fuel.broker.handle_file import generate_url, get_file_by_short_url


@medivac.route("/<file_name>", methods=["PUT"])
def handle_upload_file(file_name):
    real_file = request.get_data(as_text=True)
    if len(real_file) > MaxFile.MAX_CONTENT_LENGTH:
        return "Too big file, your file must less than %s byte for now :);" % MaxFile.MAX_CONTENT_LENGTH

    return generate_url(file_name, real_file)


@medivac.route("/<short_url>", methods=["GET"])
def get_file(short_url):
    try:
        short_url = str(short_url)
    except (ValueError, TypeError):
        return "What are you doing?....."

    return get_file_by_short_url(short_url)
