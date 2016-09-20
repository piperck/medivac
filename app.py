from flask import Flask
from views import medivac
app = Flask(__name__)

# add blue_print
app.register_blueprint(medivac)
