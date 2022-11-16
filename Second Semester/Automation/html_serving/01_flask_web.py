from flask import Flask,request

app = Flask(__name__) # determine the rout path (eg.: image)

@app.route('/')
def index():
    return 'This is the main page of the website'

# arguments, syntax base_url/name?var1=value1&var2&value2
@app.route('/cat')
def cat():
    cat_name = request.args.get("name", "Anonymus")
    cat_age = request.args.get("age", "42")
    return f'My cats name is {cat_name} and its age is {cat_age}'

# parameters syntax base_url/greetings/value
@app.route('/greetings/<uname>')
def hello(uname):
    return f'''
    Hello <b>{uname}</b><br>
    <p>Hello there</p>
    <p><a href="https://github.com/green-fox-academy/teaching-materials/tree/master/syllabus/ibs/automation">Line</a></p>
    '''

if __name__ == '__main__':
    app.run(
        host = 'localhost',
        port=5000,
        debug=True
    )