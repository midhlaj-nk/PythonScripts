from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def log_ip():
    # Log IP address
    ip_address = request.remote_addr
    print(f"IP address {ip_address} accessed /login endpoint.")
    return "Logged IP address."

if __name__ == '__main__':
    app.run(debug=True)
