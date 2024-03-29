"""
    config.py: contains 3 API configuration classes DevelopmentConfig, TestingConfig,
    & ProductionConfig.

    in addition, it also has a config dict that maps the above 3 classes to a string

    config_dict = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
"""
# built-in fs modules
import os
import pathlib

# env manager
from dotenv import load_dotenv

# load env. vars
load_dotenv()


class Config:  # pylint: disable=too-few-public-methods
    """
    base configuration class. all other configuration classes
    (Testing, Development, Production) inherit from this class.

    Config specifies basic Flask configuration options such as
    number of threads per page, CSRF session key, Flask secret key
    and Celery URLs for executing background tasks
    """

    # base dir
    BASE_DIR = pathlib.Path(__file__).parent.parent.absolute()
    # application threads
    THREADS_PER_PAGE = 2
    # protection agains Cross-site Request Forgery (CSRF)
    CSRF_ENABLED = True
    # unique + secret key for signing the data. Psuedo-randomly
    # generated
    CSRF_SESSION_KEY = os.urandom(64)
    # secret key for signing cookies
    SECRET_KEY = os.urandom(64)


class TestingConfig(Config):  # pylint: disable=too-few-public-methods
    """
    testing configuration class. sets up a local
    SQLite database for testing, disables CSRF
    protections & configures Flask
    """

    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False
    CSRF_ENABLED = False


class DevelopmentConfig(Config):  # pylint: disable=too-few-public-methods
    """
    development configuration class. sets up a local
    SQLite database for development, enables CSRF
    protections & configures Flask
    """

    DEBUG = True
    TESTING = False
    WTF_CSRF_ENABLED = True
    CSRF_ENABLED = True


class ProductionConfig(Config):  # pylint: disable=too-few-public-methods
    """
    production configuration class. sets up a local
    SQLite database for production, enables CSRF
    protections & configures Flask for production
    """

    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    CSRF_ENABLED = True


# importable config dict that maps each configuration
# class from above to a keyword (can be used to get
# the configuration just using one key word w/o having
# to import all 3 classes i.e. config_dict["development"]
# returns DevelopmentConfig)
config_dict = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
