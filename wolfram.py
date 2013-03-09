from bottle import route, run

@route('/')
def helloworld():
    return "Hello World!"

run(host='localhost', port=8000, debug=True)
