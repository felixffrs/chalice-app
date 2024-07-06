from chalice import Blueprint
from ..auth.authorizer import my_custom_authorizer
from ..config import MY_VAR

authors = Blueprint(__name__)

@authors.route('/', methods=['GET'], authorizer=my_custom_authorizer)
def index():
    authors.log.info("dadas")
    print(MY_VAR)
    return {'hello': 'world'}