import os

# This is the basic config file for all the pods
BASE_DIR = os.path.expanduser('~')

CONFIG_DIR = os.path.dirname(os.path.expanduser(__file__))

HYDRA_DIR = os.path.join(BASE_DIR, '.hydra')

DATA_DIR = os.path.join(BASE_DIR, '.hydra', 'data')

MODEL_DIR = os.path.join(BASE_DIR, '.hydra', 'model')

#
_user = "test_admin@hwi-test-db"
_password = "JuNiMo2020!"

_db_name = "test"

_server_name = "hwi-test-db.mysql.database.azure.com"
_port = 3306

SECRET_KEY='\xa2\x98\xd5\x1f\xcd\x97(\xa4K\xbfF\x99R\xa2\xb4\xf4M\x13R\xd1]]\xec\xae'

SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{}:{}@{}:{}/{}".format(_user, _password, _server_name, _port, _db_name)

ASM_PORT=443
HWI_EXTENSIONS_DIR = '/usr/local/lib/python3.6/dist-packages/'

POLYVIS_URL='http://polyvis.org/'

DEBUG=False
TESTING=False
MAIL_DEBUG=False
SECURITY_CONFIRMABLE=True
SECURITY_SEND_REGISTER_EMAIL = True

MAIL_USERNAME = 'AKIAYEZ2DBMTV5XE42NI'
MAIL_PASSWORD = 'BFPXVrbXazWt9k0TU0nGEgJd0J+FE7i9snZYFEYS9jC7'

EXTENSIONS = {
    'pywr_extension': {
        'home': os.path.join(HWI_EXTENSIONS_DIR, 'pywr_extension'),
        'blueprintname': 'pywrextension',
        'templates': {
            'network': {
                'script': 'script.html'
            }
        },
        'js': {
            'network': ['pywr.js', 'bootstrap-tagsinput.js'],
        },
        'css': {
            'network': ['pywr.css', 'bootstrap-tagsinput.css'],
        }
    }
}

COOKIE_CONSENT_MESSAGE = {
    "main": "This website uses cookies to ensure you get the best experience on our website.",
    "link": {
        "url": "https://cookiesandyou.com/",
        "message": "Learn more"
    },
    "default": {
        "country_code": "GB"
    }
}

BETA_WEBSITE_MESSAGE = "I acknowledge that this is currently a beta version for trial use and commit to providing feedback, bug reports and feature requests to the developers to help improve functionality for the community of users. Feedback can be sent to feedback@hydra.org.uk"

JOB_QUEUE_HOST_IP       = os.getenv('JOB_QUEUE_HOST_IP', '0.0.0.0')
JOB_QUEUE_HOST_PORT     = os.getenv('JOB_QUEUE_HOST_PORT', '8082')
LOG_MANAGER_URL = os.getenv('LOG_MANAGER_URL', '0.0.0.0')
LOG_MANAGER_PORT = os.getenv('LOG_MANAGER_PORT', 8083)

HOW_TO_VIDEOS = [
    {
        'name': 'HWI-Pywr Tutorial 1',
        'description': 'How to create a new project and network ready to build a model in Tutorial 2',
        'url': 'https://www.youtube.com/embed/psutXes0Irk'
    },
    {
        'name': 'HWI-Pywr Tutorial 2',
        'description': 'How to build a basic simulation model, add attributes, run the model, view results and create different scenarios to compare outcomes',
        'url': 'https://www.youtube.com/embed/tE014BqLK0M'
    },
    {
        'name': 'HWI-Pywr Tutorial 3',
        'description': 'Extending the model from Tutorial 2 with hydropower and abstraction demands',
        'url': 'https://www.youtube.com/embed/U-xOlFgrCZg'
    },
]
ASM_SLEEP_PERIOD = 2

#this is the deployment-test IAM user
AWS_ACCESS_KEY_ID = os.getenv('K8S_AWS_ACCESS_KEY_ID', 'AKIAYEZ2DBMTXMM2FCCI')
AWS_SECRET_ACCESS_KEY = os.getenv('K8S_AWS_SECRET_ACCESS_KEY', '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')

FLASKS3_BUCKET_NAME='hwi-test'

DATA_BUCKET_NAME = 'hwi-test-data'
S3_ACTIVE = True

DOCKER_APP_VOLUMES = {
    'apps-uploads':{
        'volume_name' :"/root/.hydra/apps/uploads/",
        'mount_folder' :"/root/.hydra/apps/uploads/"
    }
}

APPS_DIR=os.environ.get('HWI_APPS_DIR', os.path.join(HYDRA_DIR, 'apps'))
HWI_DEPLOYMENT_NAME = os.environ.get('HWI_DEPLOYMENT_NAME', 'test')

print("***** Loaded Specific Config ******")
