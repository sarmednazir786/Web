from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
@app.route('/success/subscribed')

def success():
	return render_template('subscribed.html', sites=sanitized_value)
#	return 'Hello %s' % sanitized_value
	
@app.route('/login', methods=['POST', 'GET'])

def login():
	if request.method == 'POST':
		global value
		global sanitized_value
		
		value = request.form['nm']
		sanitized_value = value.replace('<script>', '').replace('</script>', '')
		return redirect(url_for('success'))
	else:
		user = request.args.get('nm')
		return redirect (url_for('success'))
	
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
