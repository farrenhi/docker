from flask import *
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()  # Load variables from .env file

app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

greet = os.getenv('greet')
port_number = os.getenv('port_number')

print("greet:", greet)
print("port_number:", port_number)


# Pages
@app.route("/")
def index():
    print("greet:", greet)
    print("port_number:", port_number)
    return port_number
    return "Hello Docker! Yessssss" + port_number
	# return render_template("index.html")

app.run(host="0.0.0.0")

# , port=5000 , debug=True