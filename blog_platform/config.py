import os

basedir = os.path.abspath(os.path.dirname(__file__))


class FlaskConfig:
    ENV = 'production'
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = None
    TRAP_HTTP_EXCEPTIONS = True
    TRAP_BAD_REQUEST_ERRORS = None
    SECRET_KEY = None
    SESSION_COOKIE_NAME = 'session'  # Replace with your session cookie name
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_PATH = None
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = None
    PERMANENT_SESSION_LIFETIME = 31_536_000  # 1 year (in seconds)
    SESSION_REFRESH_EACH_REQUEST = True
    USE_X_SENDFILE = False
    SEND_FILE_MAX_AGE_DEFAULT = None  # 12 hours (in seconds)
    SERVER_NAME = None
    APPLICATION_ROOT = '/'
    PREFERRED_URL_SCHEME = 'http'
    MAX_CONTENT_LENGTH = None  # 16 * 1024 * 1024  # 16 MB
    TEMPLATES_AUTO_RELOAD = False
    EXPLAIN_TEMPLATE_LOADING = False
    MAX_COOKIE_SIZE = 4093
    JSON_AS_ASCII = True
    JSON_SORT_KEYS = True
    JSONIFY_PRETTYPRINT_REGULAR = True
    JSONIFY_MIMETYPE = 'application/json'


class FlaskRestxConfig(FlaskConfig):
    RESTX_JSON = {}  # JSON encoder/decoder
    RESTX_VALIDATE = False  # Enable request validation
    RESTX_MASK_HEADER = 'X-Fields'  # Header for request masking
    RESTX_MASK_SWAGGER = True  # Mask sensitive data in Swagger UI
    RESTX_INCLUDE_ALL_MODELS = False  # Include all models in Swagger UI
    BUNDLE_ERRORS = True  # Bundle validation errors
    ERROR_404_HELP = None  # Show 404 help message
    HTTP_BASIC_AUTH_REALM = None  # HTTP Basic Auth realm
    SWAGGER_VALIDATOR_URL = None  # URL for Swagger validator
    SWAGGER_UI_DOC_EXPANSION = None  # Swagger UI docs expansion
    SWAGGER_UI_OPERATION_ID = None  # Show operation IDs in Swagger UI
    SWAGGER_UI_REQUEST_DURATION = None  # Show request duration in Swagger UI
    SWAGGER_UI_OAUTH_APP_NAME = None  # OAuth app name for Swagger UI
    SWAGGER_UI_OAUTH_CLIENT_ID = None  # OAuth client ID for Swagger UI
    SWAGGER_UI_OAUTH_REALM = None  # OAuth realm for Swagger UI
    # SWAGGER_SUPPORTED_SUBMIT_METHODS = ['get', 'post', 'put', 'delete', 'patch', 'options',
    #                                     'head']  # Supported HTTP methods in Swagger UI


class DatabaseConfig:
    DB_DIALECT = 'postgresql'
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_USER = 'postgres'
    DB_PASSWORD = 'a'
    DB_NAME = 'blog_platform'
    DB_DATA_DIR = '/pgdata/pg16'


class BaseConfig(DatabaseConfig):
    APP_NAME = 'Blog Platform'
    DEBUG = False

    RESTX_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTX_VALIDATE = True
    RESTX_MASK_SWAGGER = False
    RESTX_ERROR_404_HELP = False
    SWAGGER_UI_JSONEDITOR = False
    ENABLED_MODULES = (
        'v1'
    )
    RABBITMQ_USER = 'guest'
    RABBITMQ_PASS = 'guest'
    LOG_CONFIG_PATH = 'C:\\Users\\Richa\\PycharmProjects\\Blog_Platform\\blog_platform\\logging.conf'
    RABBITMQ_URL = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@rabbitmq-blog:5672"
    ERROR_INCLUDE_MESSAGE = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'prod'


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True


class TestingConfig(BaseConfig):
    ENV = 'testing'
    DEBUG = True
    DB_NAME = 'blog_platform_test'


config_by_name = {'dev': DevelopmentConfig, 'testing': TestingConfig, 'prod': ProductionConfig}
