from flask import Blueprint, render_template, request, redirect

from models.ticket import Ticket

import services.ticket_service as ticket_service
from services.ticket_service import (
    adicionar_ticket,
    listar_tickets,
    buscar_ticket,
    responsavel_menos_ocupado,
)

ticket_bp = Blueprint("ticket", __name__)

@ticket_bp.route("/tickets")
def listar_tickets_view():
    return render_template(
        "index.html",
        tickets=listar_tickets(),
    )

@ticket_bp.route("/tickets/create", methods=["GET", "POST"])
def criar_ticket():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        priority = request.form.get("priority")
        requester = request.form.get("requester_name")
        department = request.form.get("department")
        responsible = request.form.get("responsible")

        if responsible == "AUTO":
            responsible = ticket_service.get_least_busy_responsible(
                ticket_service.get_all()
            )

        novo_ticket = Ticket(
            id=len(listar_tickets()) + 1,
            title=title,
            description=description,
            priority=priority,
            requester=requester,
            department=department,
            status="Aberto",
            responsible=responsible,
        )
        adicionar_ticket(novo_ticket)
        return redirect("/tickets")

    return render_template("create_ticket.html")

@ticket_bp.route("/tickets/<int:id>")
def detalhar_ticket(id):
    ticket = buscar_ticket(id)
    return render_template(
        "details.html",
        ticket=ticket
    )

@ticket_bp.route("/tickets/<int:id>/edit", methods=["GET", "POST"])
def editar_ticket(id):
    ticket = buscar_ticket(id)
    if not ticket:
        return "Chamado não encontrado", 404

    if request.method == "POST":
        ticket.title = request.form.get("title")
        ticket.description = request.form.get("description")
        ticket.priority = request.form.get("priority")
        ticket.requester = request.form.get("requester_name")
        ticket.department = request.form.get("department")
        status = request.form.get("status")
        if status is not None:
            ticket.status = status
        return redirect(f"/tickets/{id}")

    return render_template("edit_ticket.html", ticket=ticket)
