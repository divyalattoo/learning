class IssueTicketRequest:
    def __init__(self, vehicle_number: str, gate_id):
        self.vehicle_number = vehicle_number
        self.gate_id = gate_id

    def __str__(self):
        return f"IssueTicketRequest(vehicle_number={self.vehicle_number}, Gate_ID={self.gate_id})"