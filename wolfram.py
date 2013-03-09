from bottle import route, run

@route('/')
def main():
    return "Hello World!"

run(host='localhost', port=8000, debug=True)
