from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/<width>/<height>')
def  index(width, height):
	return render_template("index.html", width=int(width), height=int(height))
app.run(debug=True)