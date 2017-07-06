import socket
import os
import sys
import errno
import time
import datetime


# Endpoint methods -----------------------------
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

def get_private_key(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/json')])
    #params = environ['params']
    now = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    keyPair = generateSSHKey(now)
    regSSHKey(keyPair[1])
    with open(keyPair[0]) as privateKey:
        resp = "{'pvtKey': '" + privateKey + "'}"
    yield resp.encode("utf-8")



# Worker Methods ---------------------------------------------------

def generateSSHKey(keyName):
    try:
        print "[INFO] Starting to generate key Pair"
        os.system('ssh-keygen -t rsa -b 4096 -f /keyserver/regkey/' + str(keyName) + '.key -q -N ""')
        os.system('ssh-keygen -y -f /keyserver/regkey/' + str(keyName) + '.key > /keyserver/regkey/' + str(keyName) + '')
        print "[INFO] Key Pair was generated successfully"
    except:
        print "[ERROR] Generate key Pair failed"
    
    pubKey = "/keyserver/regkey/" + str(keyName) + ".pub"
    privateKey = '/keyserver/regkey/' + str(keyName) + '.key'
    
    keyPair = [pubKey, privateKey ]
    
    return keyPair


def regSSHKey(pubKey):
    #Writing PubKey SSH Authorized Keys
    print "[INFO] Starting to write .SSH/Authorized >"
    
    sshAuthPath = "/home/pi/.ssh/authorized_keys"
    
    file = open(pubKey, "r")
    pubKeyRSA = file.read()
    
    file = open(sshAuthPath, "a")
    file.write(pubKeyRSA)
    file.close()

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
    dispatcher.register('GET', '/privateKey', get_private_key)

    # Launch a basic server
    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080...')
    httpd.serve_forever()