#encoding:utf-8

from settings import *
import dj_database_url

ALLOWED_HOSTS = [ '.herokuapp.com', ]

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, "db.sqlite3"))
}