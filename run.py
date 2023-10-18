"""Main."""
from app import create_app
from config import APP_DEBUG, APP_HOST, APP_PORT

if __name__ == "__main__":
    app = create_app()
    app.run(port=APP_PORT, debug=APP_DEBUG, host=APP_HOST)
