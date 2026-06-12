tickets = []

RESPONSIBLES = [
    "João",
    "Maria",
    "Carlos",
]

def listar_tickets():
    return tickets


def get_all():
    return tickets


def adicionar_ticket(ticket):
    tickets.append(ticket)


def buscar_ticket(id):
    for ticket in tickets:
        if ticket.id == id:
            return ticket
    return None


def get_least_busy_responsible(tickets):
    counts = {}

    for name in RESPONSIBLES:
        counts[name] = 0

    for ticket in tickets:
        if ticket.status != "Resolvido" and ticket.status != "Fechado":
            counts[ticket.responsible] += 1

    return min(counts, key=counts.get)


def responsavel_menos_ocupado():
    contador = {}

    for r in RESPONSIBLES:
        contador[r] = 0

    for ticket in tickets:
        if ticket.status not in ["Resolvido", "Fechado"]:
            contador[ticket.responsible] += 1

    return min(contador, key=contador.get)
