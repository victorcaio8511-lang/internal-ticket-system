from flask import Flask, redirect
from routes.ticket_routes import ticket_bp

app = Flask(__name__)

app.register_blueprint(ticket_bp)

@app.route("/")
def home():
    return redirect("/tickets")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)