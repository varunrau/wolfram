from bottle import route, run, template, view

@route('/')
@view('main_template')
def main():
    return dict(greeting='Wolfram')

run(host='localhost', port=8000, debug=True)
