# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_minify  import Minify

from apps import app


if __name__ == "__main__":
    app.run(host="0.0.0.0")
