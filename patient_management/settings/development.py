from environ import Env
from .base import *

env = Env()

#####################################################################
#                      SECURITY/DEPLOYMENT                          #
# https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/ #
#####################################################################
SECRET_KEY = env("SECRET_KEY", default=False, cast=str)
DEBUG = env("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = ["*"]


#####################################################################
#                          DATABASE                                 #
#  https://docs.djangoproject.com/en/5.0/ref/settings/#databases    #
#####################################################################

DATABASES = {"default": env.db()}
