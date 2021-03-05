from flask import Flask, request, render_template
from keras.models import load_model
import numpy as np
import tensorflow as tf
from tensorflow.python.eager.def_function import run_functions_eagerly

global model,graph
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
   tf.config.experimental.set_memory_growth(physical_devices[0], True)

#graph = tf.compat.v1.get_default_graph()
model = load_model("regressor.h5")

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")
    #Now we render html page when visited localhost

@app.route("/login",methods=["POST"])

def login():
    markspend = float(request.form["ms"])
    adminspend = float(request.form["ad"])
    rdspend = float(request.form["rd"])
    state = request.form["State"]
    num1 = 0
    num2 = 0
    if state == "newyork":
        num1,num2 = 0,1
    elif state == "california":
        num1,num2 = 0,0
    else:
        num1,num2 = 1,0
    
    inputs = [[num1,num2,markspend,adminspend,rdspend]]
    
    
    y_pred = model.predict(np.array(inputs))[0][0]

    
    return render_template("index.html",abc = y_pred)
if __name__ == "__main__":
    app.run(debug=True)
