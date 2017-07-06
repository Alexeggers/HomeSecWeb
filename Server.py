def index_page(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/html')])
    params = environ['params']
    with open("index.html", "r") as file:
        resp = file.read()
    yield resp.encode('utf-8')

def get_styles(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/css')])
    with open("css/styles.css", "r") as file:
        resp = file.read()
    yield resp.encode('utf-8')

def unlock_image(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/plain')])
    #params = environ['params']
    with open("images/unlock.jpg", "r") as file:
        resp = file.read()
    yield resp

def lock_image(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/plain')])
    #params = environ['params']
    with open("images/lock.png", "r") as file:
        resp = file.read()
    yield resp

def unlock_image(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/plain')])
    #params = environ['params']
    with open("images/unlock.jpg", "r") as file:
        resp = file.read()
    yield resp

def get_js(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/javascript')])
    #params = environ['params']
    with open("js/index.js", "r") as file:
        resp = file.read()
    yield resp.encode("utf-8")

def get_jquery(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/javascript')])
    #params = environ['params']
    with open("js/jquery-3.2.1.js", "r") as file:
        resp = file.read()
    yield resp.encode("utf-8")

if __name__ == '__main__':
    from resty import PathDispatcher
    from wsgiref.simple_server import make_server

    # Create the dispatcher and register functions
    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/', index_page)
    dispatcher.register('GET', '/css/styles.css', get_styles)
    dispatcher.register('GET', '/images/unlock.jpg', unlock_image)
    dispatcher.register('GET', '/images/lock.png', lock_image)
    dispatcher.register('GET', '/js/index.js', get_js)
    dispatcher.register('GET', '/js/jquery-3.2.1.js', get_jquery)

    # Launch a basic server
    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080...')
    httpd.serve_forever()