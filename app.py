from flask import Flask, request
import requests

app = Flask(__name__)

# ---------------------------
# 🏠 HOME
# ---------------------------
@app.route("/")
def home():
    return "Flask Security Demo"


# ---------------------------
# 🌐 SSRF (FETCH ONLY)
# ---------------------------
@app.route("/remote")
def remote():
    url = request.args.get("url")

    if not url:
        return "No URL provided"

    try:
        response = requests.get(url)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


# ---------------------------
# 💣 RFI (FETCH + EXECUTE + SHOW OUTPUT)
# ---------------------------
@app.route("/rfi")
def rfi():
    url = request.args.get("url")

    if not url:
        return "No URL provided"

    try:
        code = requests.get(url).text

        # 🔥 Capture output
        import io
        import sys

        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        exec(code)

        sys.stdout = old_stdout

        return buffer.getvalue()

    except Exception as e:
        return f"Error: {str(e)}"


# ---------------------------
# ▶ RUN APP
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)