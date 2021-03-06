# coding: utf-8
import io
import os
import uuid
import hashlib
from fuel.models.file_maps import FileMaps
from fuel.init_db import db_session
from fuel.lib.util import generate_short_url
from fuel.myconf.online_config import logger, UPLOAD_FOLDER, DOMAIN_NAME
from fuel.exception import NotFindUrl


def generate_url(file_name, real_file):
    # add_database
    split = file_name.rsplit(".", 1)
    if len(split) == 1:
        file_name, file_extension_name = split[0], ''
    else:
        file_name, file_extension_name = split

    # born unique no
    x = str(uuid.uuid4())
    file_name_hash = str(hashlib.md5(x).hexdigest())

    # save file
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    file_uri = os.path.join(UPLOAD_FOLDER, file_name_hash)
    with io.open(file_uri, "wb") as f:
        f.write(real_file)

    # generate a short url
    secret = generate_short_url(file_name_hash)

    # save into database
    file_map = FileMaps(file_name=file_name, file_extension_name=file_extension_name, file_uri=file_uri, short_url=secret)
    db_session.add(file_map)
    db_session.commit()

    file_url = "%s/%s" % (DOMAIN_NAME, secret)
    logger.info("Upload file. file_name: {0}, file_uri: {1}, file_extension_name: {2}".format(file_name, file_uri, file_extension_name))

    return file_url


def get_file_by_short_url(short_url):
    file_maps = FileMaps.query.filter(FileMaps.short_url == short_url).first()

    if not file_maps:
        logger.error("File_maps is None. short_url: {0}".format(short_url))
        raise NotFindUrl

    file_directory, file_name = file_maps.file_uri.rsplit("/", 1)
    file_extension_name = file_maps.file_extension_name
    logger.info("Get file. file_directory: {0}, file_hash: {1}, file_extension_name: {2}".format(file_name, file_name, file_extension_name))

    return file_directory, file_name, file_extension_name
