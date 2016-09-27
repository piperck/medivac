# coding: utf-8
from flask import request, send_from_directory
from fuel.myconf.online_config import MAX_CONTENT_LENGTH
from fuel.views import medivac
from fuel.broker.handle_file import generate_url, get_file_by_short_url


@medivac.route("/<file_name>", methods=["PUT"])
def handle_upload_file(file_name):
    real_file = request.get_data()
    if len(real_file) > MAX_CONTENT_LENGTH:
        return "Too big file, your file must less than %s byte for now :);" % MAX_CONTENT_LENGTH

    url = generate_url(file_name, real_file)+'\n'

    return url


@medivac.route("/<short_url>", methods=["GET"])
def get_file(short_url):
    try:
        short_url = str(short_url)
    except (ValueError, TypeError):
        return "What are you doing?....."

    file_directory, file_name, file_extension_name = get_file_by_short_url(short_url)
    complete_file_name = "%s.%s" % (file_name, file_extension_name)

    return send_from_directory(file_directory, file_name, as_attachment=True, attachment_filename=complete_file_name)
