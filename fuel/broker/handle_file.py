# coding: utf-8
import io
import os
import uuid
import hashlib
from fuel.models.file_map import FileMap
from fuel.init_db import db_session


UPLOAD_FOLDER = "/home/command_center"


def generate_uri_from_put(file_name, real_file):
    # add_database
    split = file_name.rsplit(".", 1)
    if len(split) == 1:
        _, file_extension_name = split[0], ''
    else:
        _, file_extension_name = split

    # born unique no
    x = str(uuid.uuid4())
    file_hash = str(hashlib.md5(x).hexdigest())

    # save file
    file_uri = os.path.join(UPLOAD_FOLDER, file_hash)
    with io.open(file_uri, "w", encoding="utf-8") as f:
        f.write(real_file)

    file_map = FileMap(file_path=file_hash, file_extension_name=file_extension_name, file_uri=file_uri)
    db_session.add(file_map)
    db_session.commit()

    return file_uri
