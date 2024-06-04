from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_start_page():
    return 'Fuck you'