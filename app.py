from flask import Flask
from routes.ticket_routes import ticket_bp

app = Flask(__name__)
app.register_blueprint(ticket_bp)

@app.route("/")
def home():
    return "Sistema de Controle de Chamados"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)