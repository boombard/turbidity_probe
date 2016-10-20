from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():

    # Generate whatever data you need in this view and send it to your template

    data = [1, 2, 3]
    return render_template("turbidity_probe_graph.html", data=data)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
