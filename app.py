from flask import Flask
from flask.blueprints import Blueprint

import config
import route

app = Flask(__name__, static_url_path="/")

app.debug = config.DEBUG

# register route
for blueprint in vars(route).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    print("App running on: " + config.HOST + ":" + str(config.PORT))
    app.run(host=config.HOST, port=config.PORT)
