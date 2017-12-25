from src.app import app

__author__ = "Prajesh Ananthan"

app.run(debug=app.config['DEBUG'], port=4990)
