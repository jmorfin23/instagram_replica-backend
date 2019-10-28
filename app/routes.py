from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'This is a test.'


@app.route('/api/register')
def register():
    pass


@app.route('/api/login')
def login():
    pass
