import os
from dotenv import  load_dotenv

load_dotenv(verbose=True)
env_file = os.path.join(
    os.path.dirname(__file__),
    '.env'
)
load_dotenv(env_file)

MYSQL_DATABASE = os.environ.get('DEV_MYSQL_DATABASE')
MYSQL_HOST = os.environ.get('DEV_MYSQL_HOST')
MYSQL_USER = os.environ.get('DEV_MYSQL_USER')
MYSQL_ROOT_PASSWORD = os.environ.get('DEV_MYSQL_ROOT_PASSWORD')
MYSQL_PASSWORD = os.environ.get('DEV_MYSQL_PASSWORD')
MYSQL_CHARSET = os.environ.get('MYSQL_CHARSET')
APP_ID = os.environ.get('APP_ID')
QUERY_NUM = os.environ.get('QUERY_NUM')
