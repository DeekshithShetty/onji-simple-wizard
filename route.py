from flask import Blueprint, send_from_directory, send_file

wapp_page = Blueprint("wapp", __name__)

# serve index page
@wapp_page.route("/", methods=["GET"])
def send_index_page():
    return send_file("index.html")

# serve wizard partial views
@wapp_page.route("/views/<path:path>", methods=["GET"])
def send_views(path):
    return send_from_directory("views", path)

# serve js files
@wapp_page.route("/js/<path:path>", methods=["GET"])
def send_js(path):
    return send_from_directory("js", path, mimetype="text/javascript")

# serve css files
@wapp_page.route("/css/<path:path>", methods=["GET"])
def send_css(path):
    return send_from_directory("css", path)

# serve image files
@wapp_page.route("/images/<path:path>", methods=["GET"])
def send_images(path):
    return send_from_directory("images", path)
