# filepath: c:\XP-Credit\src\backend\flask_app\run.py
import logging
from flask_app import create_app

logging.basicConfig(level=logging.DEBUG)
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)