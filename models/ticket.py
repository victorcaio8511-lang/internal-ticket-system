from datetime import datetime
from zoneinfo import ZoneInfo


class Ticket:
    def __init__(
        self,
        id,
        title,
        description,
        priority,
        requester="",
        department="",
        status="Aberto",
        responsible="Não atribuído",
    ):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.requester = requester
        self.department = department
        self.status = status
        self.responsible = responsible
        self.created_at = datetime.now(ZoneInfo("America/Sao_Paulo"))

