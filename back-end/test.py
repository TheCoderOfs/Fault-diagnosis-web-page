from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello,world!'


@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return f'Blog number: {postID}!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
