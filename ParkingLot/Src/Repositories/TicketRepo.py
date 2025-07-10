class TicketRepo:

    def __init__(self):
        self.tickets = {}
        self.count = 0

    def add_ticket(self, ticket):
        if ticket.id in self.tickets:
            raise ValueError(f"Ticket with id {ticket.id} already exists.")
        id_generated = self.count + 1
        ticket.id = id_generated
        ticket.token_num = id_generated
        self.count += 1
        self.tickets[ticket.id] = ticket
        return ticket

    def get_ticket(self, ticket_id):
        return self.tickets.get(ticket_id, None)

    def update_ticket(self, ticket):
        if ticket.id not in self.tickets:
            raise ValueError(f"Ticket with id {ticket.id} does not exist.")
        self.tickets[ticket.id] = ticket

    def delete_ticket(self, ticket_id):
        if ticket_id not in self.tickets:
            raise ValueError(f"Ticket with id {ticket_id} does not exist.")
        del self.tickets[ticket_id]
