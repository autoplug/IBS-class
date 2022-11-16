from flask import Flask, render_template

app = Flask(__name__) # determine the rout path (eg.: image)

@app.route('/cats/<int:cat_age>')
def index(cat_age):
    my_var = cat_age + 1
    return render_template('cat.html', idx=my_var)


if __name__ == '__main__':
    app.run(
        host = 'localhost',
        port=5000,
        debug=True
    )