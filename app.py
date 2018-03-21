from flask import Flask
app.Flask (__name__)

@app.route('/')
def index ():
    return 'hola mundo'

@app.route('/user/<name>')
def user (name):
    return 'Hola %s' % name

if __name__ == '__main__':
    app.run(debudebuge)
