import pickle
import numpy as np

clf_new = pickle.load(open("my_model.sav", "rb"))
print(clf_new.predict([[0.3]]))

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/predict/<my_input>")
def my_predict(my_input: float):
    val = np.array(my_input, dtype=float).reshape(-1, 1)
    result = clf_new.predict(val)
    return f"The prediction is {result}"

app.run()