from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def tes():
    n = ''

    if request.method=="POST":
        jk = float(request.form.get("jenis"))
        um = float(request.form.get("umur"))
        hyp = float(request.form.get("hipertensi"))
        hea = float(request.form.get("jantung"))
        marr = float(request.form.get("nikah"))
        work = float(request.form.get("pekerjaan"))
        res = float(request.form.get("daerah"))
        gluc = float(request.form.get("glukosa"))
        bmi = float(request.form.get("bmi"))
        smo = float(request.form.get("rokok"))

        hasil = [jk, um, hyp, hea, marr, work, res, gluc, bmi, smo]
        model = pickle.load(open('stroke.pkl', 'rb'))
        pred = model.predict([hasil])

        if pred == 1:
            n = 'ada risiko terkena stroke'
        else:
            n = 'tidak ada risiko terkena stroke'

    return render_template("index.html", n=n)

if __name__ == "__main__":
    app.run(debug=True)