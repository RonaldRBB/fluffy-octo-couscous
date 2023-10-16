"""Main."""
from app import create_app
from config import APP_PORT

if __name__ == "__main__":
    app = create_app()
    app.run(port=APP_PORT)
