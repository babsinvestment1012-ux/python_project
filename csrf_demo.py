from flask import Flask, request, render_template_string, make_response, redirect
import uuid

app = Flask(__name__)

users = {
    "alice": {"password": "pass123", "balance": 10000, "session_token": None},
    "bob":   {"password": "pass456", "balance": 500,   "session_token": None},
}

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Vulnerable National Bank</title></head>
<body style="font-family: Arial; max-width: 400px; margin: 50px auto;">
  <h2>Vulnerable National Bank - Login</h2>
  <form method="POST" action="/login">
    <input type="text" name="username" placeholder="Username" required/><br/><br/>
    <input type="password" name="password" placeholder="Password" required/><br/><br/>
    <button type="submit">Login</button>
  </form>
  <p style="color:red;">!! NO CSRF PROTECTION !!</p>
  <p>Test accounts: alice/pass123 (balance: $10,000), bob/pass456 (balance: $500)</p>
</body>
</html>
"""

ACCOUNT_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Account Dashboard</title></head>
<body style="font-family: Arial; max-width: 600px; margin: 50px auto;">
  <h2>Welcome, {{ username }}!</h2>
  <p>Balance: <strong>${{ "%.2f"|format(balance) }}</strong></p>
  <hr/>
  <h3>Transfer Funds</h3>
  <form method="POST" action="/transfer">
    <label>To Account: <input type="text" name="to_account" placeholder="bob" required/></label><br/><br/>
    <label>Amount ($): <input type="number" name="amount" min="1" required/></label><br/><br/>
    <button type="submit">Send Transfer</button>
  </form>
  <hr/>
  <h3>Your Cookie (visible for demo)</h3>
  <p id="cookies" style="background:#f4f4f4; padding:10px; word-break:break-all;"></p>
  <script>document.getElementById('cookies').innerText = document.cookie || '(no cookies visible from JS)';</script>
  <hr/>
  <p><a href="/check">Check all balances</a></p>
  <p style="color:red;">WARNING: Accepts GET and POST. No CSRF token. No SameSite cookie.</p>
</body>
</html>
"""

def get_session_user():
    session_id = request.cookies.get("session_id")
    if session_id:
        for user, data in users.items():
            if data["session_token"] == session_id:
                return user, data
    return None, None

@app.route("/")
def home():
    user, data = get_session_user()
    if user:
        return render_template_string(ACCOUNT_PAGE, username=user, balance=data["balance"])
    return LOGIN_PAGE

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in users and users[username]["password"] == password:
        session_id = str(uuid.uuid4())
        users[username]["session_token"] = session_id
        resp = make_response(redirect("/"))
        # VULNERABLE: no SameSite=Strict, no HttpOnly
        resp.set_cookie("session_id", session_id)
        return resp
    return "Login failed", 401

@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    user, data = get_session_user()
    if not user:
        return "Not authenticated (no valid session cookie)", 401

    to_account = request.form.get("to_account") or request.args.get("to_account", "")
    try:
        amount_str = request.form.get("amount") or request.args.get("amount", "0")
        amount = float(amount_str)
    except (ValueError, TypeError):
        return "Invalid amount", 400

    if amount <= 0:
        return "Amount must be positive", 400
    if amount > data["balance"]:
        return "Insufficient funds", 400
    if to_account not in users:
        return "Recipient account not found", 400

    data["balance"] -= amount
    users[to_account]["balance"] += amount

    return f"""
    <h2>Transfer Successful!</h2>
    <p>Method: {request.method}</p>
    <p>Transferred <strong>${amount:.2f}</strong> from <strong>{user}</strong> to <strong>{to_account}</strong></p>
    <p>Your new balance: <strong>${data['balance']:.2f}</strong></p>
    <p><a href="/">Dashboard</a> | <a href="/check">All balances</a></p>
    """

@app.route("/check")
def check():
    html = "<h2>All Account Balances</h2><table border='1' cellpadding='8'><tr><th>User</th><th>Balance</th></tr>"
    for u, d in users.items():
        html += f"<tr><td>{u}</td><td>${d['balance']:.2f}</td></tr>"
    html += "</table><br/><a href='/'>Back</a>"
    return html

if __name__ == "__main__":
    print("""
    ==========================================
    Vulnerable National Bank (CSRF Demo)
    ==========================================
    Visit: http://127.0.0.1:5000
    Login with: alice / pass123
    ==========================================
    """)
    app.run(host="127.0.0.1", port=5000, debug=True)