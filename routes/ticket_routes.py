from flask import Blueprint

ticket_bp = Blueprint("ticket", __name__)

@ticket_bp.route("/tickets")
def listar_tickets():
    return "Lista de chamados"