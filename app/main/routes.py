from flask import render_template
from app.main import main

@main.route('/')
def main():
    return render_template('index.html')