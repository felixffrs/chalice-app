
from chalice import Blueprint, AuthResponse
from ..config import API_TOKEN

authorizer = Blueprint(__name__)

def validate_bearer_token(bearer_token):

    bearer_token_splitted = bearer_token.split(" ")
    
    if len(bearer_token_splitted) != 2:
        return False
    
    token = bearer_token_splitted[1]

    if token == API_TOKEN:
        return True
    
    return False

@authorizer.authorizer(ttl_seconds=300, name="custom_authorizer")
def my_custom_authorizer(auth_request):
    bearer_token = auth_request.token
    if bearer_token is not None and validate_bearer_token(bearer_token):
        return AuthResponse(routes=['*'], principal_id='user')
    return AuthResponse(routes=[], principal_id=None)
