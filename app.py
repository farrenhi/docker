from flask import *
app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

# Pages
@app.route("/")
def index():
    return 'Hello, World!'
	# return render_template("index.html")


app.run(host="0.0.0.0", port=3000, debug=True)