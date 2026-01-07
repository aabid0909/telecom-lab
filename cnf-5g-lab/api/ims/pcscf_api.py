from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "nf": "P-CSCF",
        "status": "UP"
    })

@app.route("/sip/register", methods=["POST"])
def sip_register():
    return jsonify({
        "result": "REGISTER_OK"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5060)
