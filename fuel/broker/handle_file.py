# coding: utf-8
import io
import os
from fuel.models.file_map import FileMap
from fuel.init_db import db_session


UPLOAD_FOLDER = "/home/command_center"


def generate_uri_from_put(file_name, real_file):
    # save file
    file_uri = os.path.join(UPLOAD_FOLDER, file_name)
    with io.open(file_uri, "w", encoding="utf-8") as f:
        f.write(real_file)

    # add_database
    split = file_name.rsplit(".", 1)
    if len(split) == 1:
        file_name, file_extension_name = split[0], ''
    else:
        file_name, file_extension_name = split
    file_map = FileMap(file_name=file_name, file_extension_name=file_extension_name, file_uri=file_uri)
    db_session.add(file_map)
    db_session.commit()

    return file_uri
