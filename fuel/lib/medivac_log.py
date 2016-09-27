import datetime
import logging
import logging.handlers


def gen_medivac_building_handler(error=False):
    path_prefix = "var/log/medivac_log/"
    str_format = "%(asctime)s: %(name)s:%(levelname)s:%(message)s"
    date_fmt = "%Y-%m-%dT%H:%M:%S"

    if error:
        name = "{0}error.log-{1}".format(path_prefix, datetime.date.today())
        sc2_building_handler = logging.handlers.RotatingFileHandler(filename=name)
        sc2_building_handler.setLevel(level=logging.ERROR)
    else:
        name = "{0}info.log-{1}".format(path_prefix, datetime.date.today())
        sc2_building_handler = logging.handlers.RotatingFileHandler(filename=name)
        sc2_building_handler.setLevel(level=logging.INFO)

    formatter = logging.Formatter(str_format, date_fmt)
    sc2_building_handler.setFormatter(formatter)

    return sc2_building_handler


class BaseLogger(object):

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.level = logging.INFO

    def gen_sc2_logger(self):
        # set produce log level
        self.logger.setLevel(self.level)

        # gen two handler and set it on the logger
        handler_info = gen_medivac_building_handler()
        handler_error = gen_medivac_building_handler(error=True)
        self.logger.addHandler(handler_info)
        self.logger.addHandler(handler_error)

        return self.logger
