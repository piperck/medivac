import datetime
from fuel.lib.medivac_log import BaseLogger


logger = BaseLogger("medivac").gen_medivac_logger()


# UPLOAD_PATH
UPLOAD_FOLDER = "/home/medivac/command_center/%s" % datetime.date.today()

# NOW DOMAIN
DOMAIN_NAME = "http://www.nuanhi.com"

# MAX_UPLOAD_FILE_SIZE
MAX_CONTENT_LENGTH = 1024 * 1024 * 10
