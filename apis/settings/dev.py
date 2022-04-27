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

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    )
}

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

INSTALLED_APPS += ['apis_bibsonomy', 'apis_highlighter']

APIS_BIBSONOMY = [{
   'type': 'zotero', #or zotero
   'url': 'https://api.zotero.org', #url of the bibsonomy instance or zotero.org
   'user': os.environ.get('APIS_BIBSONOMY_USER'), #for zotero use the user id number found in settings
   'API key': os.environ.get('APIS_BIBSONOMY_PASSWORD'),
   'group': '2801369'
}]



# APIS_COMPONENTS = ['deep learning']

# APIS_BLAZEGRAPH = ('https://blazegraph.herkules.arz.oeaw.ac.at/metaphactory-play/sparql', 'metaphactory-play', 'KQCsD24treDY')


APIS_RELATIONS_FILTER_EXCLUDE += ["annotation", "annotation_set_relation"]

APIS_ENTITIES = {
    "Place": {
        "merge": True,
        "search": ["name"],
        "form_order": ["name", "kind", "lat", "lng", "status", "collection"],
        "table_fields": ["name"],
        "additional_cols": ["id", "lat", "lng", "part_of"],
        "list_filters": [
            {"name": {"method": "name_label_filter"}},
            {"collection": {"label": "Collection"}},
            {"kind": {"label": "Kind of Place"}},
            "related_entity_name",
            "related_relationtype_name",
            "lat",
            "lng",
        ],
    },
    "Person": {
        "merge": True,
        "search": ["name", "first_name"],
        "form_order": [
            "first_name",
            "name",
            "start_date_written",
            "end_date_written",
            "profession",
            "status",
            "collection",
        ],
        "table_fields": [
            "name",
            "first_name",
            "start_date_written",
            "end_date_written",
        ],
        "additional_cols": ["id", "profession", "gender"],
        "list_filters": [
            "name",
            {"gender": {"label": "Gender"}},
            {"start_date": {"label": "Date of Birth"}},
            {"end_date": {"label": "Date of Death"}},
            {"profession": {"label": "Profession"}},
            {"title": {"label": "Title"}},
            {"collection": {"label": "Collection"}},
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
    "Institution": {
        "merge": True,
        "search": ["name"],
        "form_order": [
            "name",
            "start_date_written",
            "end_date_written",
            "kind",
            "status",
            "collection",
        ],
        "additional_cols": [
            "id",
            "kind",
        ],
        "list_filters": [
            {"name": {"label": "Name or label of institution"}},
            {"kind": {"label": "Kind of Institution"}},
            {"start_date": {"label": "Date of foundation"}},
            {"end_date": {"label": "Date of termination"}},
            {"collection": {"label": "Collection"}},
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
    "Work": {
        "merge": True,
        "search": ["name"],
        "additional_cols": [
            "id",
            "kind",
        ],
        "list_filters": [
            {"name": {"label": "Name of work"}},
            {"kind": {"label": "Kind of Work"}},
            {"start_date": {"label": "Date of creation"}},
            {"collection": {"label": "Collection"}},
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
    "Event": {
        "merge": True,
        "search": ["name"],
        "additional_cols": [
            "id",
        ],
        "list_filters": [
            {"name": {"label": "Name of event"}},
            {"kind": {"label": "Kind of Event"}},
            {"start_date": {"label": "Date of beginning"}},
            {"end_date": {"label": "Date of end"}},
            {"collection": {"label": "Collection"}},
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
    "Manuscript": {
        "merge": True,
        "search": ["identifier", "name"],
        "form_order": [
            "identifier",
            "name",
            "start_date_written",
            "extent",
            "leaf_dimension",
            "written_dimension",
            "foliation_type",
            "foliation_note",
            "manuscript_conditions"
        ],
        "table_fields": [
            "identifier",
            "name",
            "start_date_written",
            "extent",
        ],
        "additional_cols": [
            "id", 
            "leaf_dimension",
            "written_dimension",
            "foliation_type",
            "foliation_note",
            "manuscript_conditions"],
        "list_filters": [
            "name",
            {"start_date": {"label": "Date of writing"}},
            {"collection": {"label": "Collection"}},
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
    "Expression": {
        "merge": True,
        "search": ["identifier", "name"],
        "form_exclude": ["name", "start_date_written", "end_date_written", "status"],
        "form_order": [
            "title",
            "locus",
            'language'
        ],
        "table_fields": [
            "title",
            "locus",
            'language'
        ],
        "additional_cols": [
            "id", 
            ],
        "list_filters": [
            "title",
            {"start_date": {"label": "Date of writing"}},
            {"collection": {"label": "Collection"}},
            "related_entity_name",
            "related_relationtype_name",
        ],
    },
}
