from flask import Flask
from fuel.views import medivac
from myconf.online_config import OnlineConfig
from fuel.init_db import db_session

# init application
app = Flask(__name__)

# add_config
app.config.from_object(OnlineConfig)

# add blue_print
app.register_blueprint(medivac)


# the request en gone away auto shutdown SQLAlchemy connect
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
