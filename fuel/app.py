from flask import Flask
from fuel.views import medivac
from myconf.online_config import OnlineConfig

# init application
app = Flask(__name__)

# add_config
app.config.from_object(OnlineConfig)

# add blue_print
app.register_blueprint(medivac)
