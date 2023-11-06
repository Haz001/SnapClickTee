
import os

# import Flask 
from flask import Flask

# Inject Flask magic
app = Flask(__name__)


# Import routing to render the pages
from apps import views
