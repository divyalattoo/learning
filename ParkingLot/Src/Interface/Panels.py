from ParkingLot.Src.DataTransferObjects.TicketRequest import TicketRequest
from ParkingLot.Src.DataTransferObjects.TicketResponse import TicketResponse
from ParkingLot.Src.Services.TicketService import TicketService


class TicketPanel:
    def __init__(self,ticket_service : TicketService):
        self.ticket_service = ticket_service

    def issue_ticket(self, request : TicketRequest) -> TicketResponse:
        response = TicketResponse()
        try:
            ticket  = self.ticket_service.generate_ticket(request.vehicle_num, request.gate_id,
                                                  request.vehicle_type, request.owner_name)

            response = response.generate_response(ticket)
            return response
        except Exception as e:
            response.status = "Failed" + " " + str(e)
            return response

class design_lot:




class AdminPanel(TicketPanel):
    def __init__(self, ticket_service: TicketService):
        super().__init__(ticket_service)

    def issue_ticket(self, request: TicketRequest) -> TicketResponse:
        response = super().issue_ticket(request)
        if response.status == "Failed":
            print(f"Error issuing ticket: {response.status}")
        else:
            print(f"Ticket issued successfully: {response}")
        return response