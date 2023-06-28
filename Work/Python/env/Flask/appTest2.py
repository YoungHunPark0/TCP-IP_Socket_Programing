from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Flask Server Test"

@app.route('/user/<username>')
def show_username(username): # 입력으로 username을 받아함
	if username == 'on':
		return "User : %s" % username
	elif username == 'off':
		return "error"
@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "post %d" % post_id

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='8800')
