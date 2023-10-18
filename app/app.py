from flask import Flask
from home.views import home_blueprint
from profile.views import profile_blueprint
from index import index_blueprint
application = Flask(__name__)
application.register_blueprint(home_blueprint, url_prefix='/home')
application.register_blueprint(profile_blueprint, url_prefix='/profile')
application.register_blueprint(index_blueprint)




