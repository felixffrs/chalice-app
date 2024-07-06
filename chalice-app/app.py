import logging
from chalice import Chalice
from chalicelib.api.author_api import authors
from chalicelib.auth.authorizer import authorizer

app = Chalice(app_name='chalice-app')
app.log.setLevel(logging.INFO)

app.register_blueprint(authorizer)
app.register_blueprint(authors, url_prefix="/authors")
