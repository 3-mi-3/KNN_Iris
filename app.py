from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("knn_model.pkl")


@app.route("/", methods=["GET", "POST"])
def predict():
    species = None
    sl = sw = pl = pw = ""
    if request.method == "POST":
        try:
            sl = request.form["sl"]
            sw = request.form["sw"]
            pl = request.form["pl"]
            pw = request.form["pw"]
            sample = np.array([[float(sl), float(sw), float(pl), float(pw)]])
            species = model.predict(sample)[0]
        except:
            species = "❌ Lỗi: Vui lòng nhập đúng định dạng số!"
    return render_template("index.html", species=species, sl=sl, sw=sw, pl=pl, pw=pw)

if __name__ == "__main__":
    app.run(debug=True)
