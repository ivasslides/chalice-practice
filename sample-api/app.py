from chalice import Chalice

app = Chalice(app_name='sample-api')


@app.route('/')
def index():
    return {'hello': 'iliana'}


#name that's inserted in url is then passed as variable
@app.route('/hello/{name}')
def hello_name(name):
    # '/hello/james' -> {"hello": "james"}
    return {'howdy': name}
