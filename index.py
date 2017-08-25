import os
from flask imnport Flask, request

token = os.environ.get('FB_ACCESS_TOKEN')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
	return 'Nothing'

if __name__ == '__main__':
	app.run(debug=true)

def webhook():
    if request.method == 'POST':
        pass
    elif request.method == 'GET': # Para a verificação inicial
        if request.args.get('hub.verify_token') == os.environ.get('FB_VERIFY_TOKEN'):
            return request.args.get('hub.challenge')
        return "Wrong Verify Token"
    return "Nothing"
