from .base import *
import re
import dj_database_url
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
REDMINE_ID = "14590"
APIS_LIST_VIEWS_ALLOWED = True
APIS_DETAIL_VIEWS_ALLOWED = True
BIRTH_REL_NAME = "place of birth"
DEATH_REL_NAME = "place of death"
APIS_BASE_URI = "https://nomansland.acdh.oeaw.ac.at/"


ALLOWED_HOSTS = re.sub(
    r"https?://",
    "",
    os.environ.get(
        "ALLOWED_HOSTS", os.environ.get("GITLAB_ENVIRONMENT_URL", "localhost,127.0.0.1")
    ),
).split(",")
# You need to allow '10.0.0.0/8' for service health checks.
ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]


SECRET_KEY = (
    "d3j@454545()(/)@zlck/6dsaf*#sdfsaf*#sadflj/6dsfk-11$)d6ixcvjsdfsdf&-u35#ayi"
)
DEBUG = True
DEV_VERSION = True

SPECTACULAR_SETTINGS["COMPONENT_SPLIT_REQUEST"] = True
SPECTACULAR_SETTINGS["COMPONENT_NO_READ_ONLY_REQUIRED"] = True

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

LANGUAGE_CODE = "de"

INSTALLED_APPS += ['apis_bibsonomy']

APIS_BIBSONOMY = [{
   'type': 'zotero', #or zotero
   'url': 'https://api.zotero.org', #url of the bibsonomy instance or zotero.org
   'user': os.environ.get('APIS_BIBSONOMY_USER'), #for zotero use the user id number found in settings
   'API key': os.environ.get('APIS_BIBSONOMY_PASSWORD'),
   'group': '4400472'
}]


# APIS_COMPONENTS = ['deep learning']

# APIS_BLAZEGRAPH = ('https://blazegraph.herkules.arz.oeaw.ac.at/metaphactory-play/sparql', 'metaphactory-play', 'KQCsD24treDY')


APIS_RELATIONS_FILTER_EXCLUDE += ["annotation", "annotation_set_relation"]
