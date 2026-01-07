from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "nf": "S-CSCF",
        "status": "UP"
    })

@app.route("/sip/invite", methods=["POST"])
def sip_invite():
    return jsonify({
        "call": "CONNECTED"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6060)
