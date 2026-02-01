from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
def check_email(email):
    k, j, d = 0, 0, 0

    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i in ["_", ".", "@"]:
                            continue
                        else:
                            d = 1

                    if k == 1 or j == 1 or d == 1:
                        return False
                    else:
                        return True
    return False


@app.route("/verify", methods=["POST"])
def verify():
    email = request.form.get("email")

    if check_email(email):
        return jsonify({"status": "success", "message": "Right email"})
    else:
        return jsonify({"status": "error", "message": "Wrong email"})


if __name__ == "__main__":
    app.run(debug=True)
