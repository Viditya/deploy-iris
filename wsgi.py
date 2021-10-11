from api import app
#gunicorn --bind 0.0.0.0:5000 --workers=5 --threads=2 wsgi:app
if __name__ == "__main__":
    app.run()