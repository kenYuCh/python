from crypt import methods
from flask import Flask, send_file,request, redirect, escape,render_template,escape
from flask_restful import Resource, request, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return "hello"

@app.route("/<string:number>")
def paratest(number):
    return f"Hello, {escape(number)}!"

@app.route('/<int:post_id>', methods=['POST'])
def postid(post_id):
    return f'Post {post_id}'

@app.route('/about/')
def about():
    return 'The about page'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return #do_the_login()
    else:
        return #show_the_login_for

if __name__ == "__main__":
    app.run(debug=True)