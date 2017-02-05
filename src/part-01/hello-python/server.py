from bottle import route, run

@route('/')
def hello():
    return "Hello Python!\n Chat do caos.\n"

run(host='0.0.0.0', port=8085, debug=True)
