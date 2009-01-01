from juno import *

@get(['/', '/index'])
def index(web):
    body = '''
        <html>
            <head> <title>index</title> </head>
            <body> index </body>
        </html>'''
    return JunoResponse(response_body=body, status=200)

@get('/wildcard/*:name/')
def wildcard(web, name): return str(name)

@get('/x/:a/:b/:c/')
def x(web, a, b, c):
    return str(a) + str(b) + str(c)

@get()
def query(web):
    return 'Query: %s' %web.input()

@route()
def form(web):
    return '''
        <form action='/post_test' name='form_test' method='post'>
            <input type='text' name='word' />   <br />
            <input type='text' name='two' />    <br />
            <input type='text' name='three' />  <br />
            <input type='submit' value='test' />
        </form>'''

@post()
def post_test(web): return 'value of "word": %s' %web.post('word')

@get('/json_test/')
def json(web):
    j = JunoResponse()
    j['Content-Type'] = 'text/json'
    return j.append('''{'main': ['a': 5, 'b': 1]}''')

@get('/ua/')
def user_agent(web):
    return 'User Agent: %s' %web.headers['HTTP_USER_AGENT']

@get()
def implicit(web):
    respond(response_body='Hi there')

@get()
def html_chain(web):
    html().                                         \
        head().title('juno html test').endhead().   \
        body().                                     \
            div().text('asdf').enddiv().            \
        endbody().                                  \
    endhtml()

if __name__ == '__main__':
    run()
