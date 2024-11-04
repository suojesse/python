from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def alkuluku(luku):
    if luku > 1:

        for i in range(2, (luku // 2) + 1):

            if (luku % i) == 0:
                return False
        else:
            return True
    else:
        return False
@app.route('/alkuluku/<int:nmr>', methods = ['GET'])
def tarkista(nmr):
    result = {
        "Numero": nmr,
        "isPrime": alkuluku(nmr)

    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)




