from flask import Flask, render_template


app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<h1>I am sivaranjani</h1>"

@app.route("/<username>")
def hello_world(username):
    return render_template('index.html',data=username)

if __name__=="__main__":
    app.run(debug=True)