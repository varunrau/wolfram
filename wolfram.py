from bottle import route, run, template, view, post, request

@route('/')
@view('main_template')
def main():
    return dict(greeting='Wolfram')

@post('/query')
@view('query_template')
def query():
    value = request.forms.get('value')
    return value

run(host='localhost', port=8000, debug=True)
