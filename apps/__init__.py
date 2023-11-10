
import os

# import Flask 
from flask import Flask

# Inject Flask magic
app = Flask(__name__)

static_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

print(static_root)


# Import routing to render the pages
from apps import views
from apps import ai
