import os
import dotenv
from app.settings import get_environ
from django.core.wsgi import get_wsgi_application

env_file = '.env.prod' if get_environ('IS_PROD') else '.env.dev'
dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), env_file))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_wsgi_application()