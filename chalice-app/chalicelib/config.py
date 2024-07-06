import os
from .secrets import get_secret

MY_VAR = os.environ["MY_VAR"]
CHALICE_APP_SECRET_NAME = os.environ["CHALICE_APP_SECRET_NAME"]

CHALICE_APP_SECRETS = get_secret(CHALICE_APP_SECRET_NAME)
API_TOKEN = CHALICE_APP_SECRETS["api-token"]