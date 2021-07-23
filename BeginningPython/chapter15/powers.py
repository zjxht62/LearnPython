from flask import Flask
app = Flask(__name__)

@app.route('/')
def powers(n = 10):
    return ', '.join(str(2**i) for i in range(n))


@app.route('/<int:n>')
def powers2(n = 10):
    return ', '.join(str(2**i) for i in range(n))

# http://127.0.0.1:5000/5
# 1, 2, 4, 8, 16

@app.route('/input/<s>')
def getInput(s = 'hello'):
    return "获取到的输入是:{}".format(s)

# http://127.0.0.1:5000/input/hahd
# 获取到的输入是:hahd