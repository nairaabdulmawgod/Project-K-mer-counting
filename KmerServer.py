from flask import Flask, request
from flask_cors import CORS, cross_origin

# pip install flask flask-cors

app = Flask(__name__)
CORS(app)


@app.route('/')
def cMers():
    return "Hi, Server is running fine!"


@app.route('/cMers/', methods=['POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        Tseq = request.form["genome"]
        k = int(request.form["K"])
        kFreq = {}
        for i in range(0, len(Tseq) - k + 1):
            kmer = Tseq[i:i + k]
            if kmer in kFreq:
                kFreq[kmer] += 1
            else:
                kFreq[kmer] = 1
    return kFreq



if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=5000)