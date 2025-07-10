import datetime

from ParkingLot.Src.repo.TicketRepo import TicketRepo
from ParkingLot.Src.repo.SlotRepo import SlotRepo
from ParkingLot.Src.repo.GateRepo import GateRepo
from ParkingLot.Src.repo.VehicleRepo import VehicleRepo
from ParkingLot.Src.repo.ParkingLotRepo import ParkingLotRepo

from ParkingLot.Src.Models.Models import Vehicle
from ParkingLot.Src.Models.Models import Ticket
from ParkingLot.Src.Models.Models import SlotStatus
from ParkingLot.Src.Models.Models import Owner

from ParkingLot.Src.DataTransferObjects.TicketRequest import TicketRequest
from ParkingLot.Src.DataTransferObjects.TicketResponse import TicketResponse

from ParkingLot.Src.Helpers.Factories.SlotFactory import SlotFactory
class TicketPanel:
    def __init__(self, TicketRepo, SlotRepo, GateRepo, VehicleRepo, ParkingLotRepo):
        self.ticket_repo = TicketRepo()
        self.slot_repo = SlotRepo()
        self.gate_repo = GateRepo()
        self.vehicle_repo = VehicleRepo()
        self.parking_lot_repo = ParkingLotRepo()

    def issue_ticket(self, request : 'TicketRequest') -> 'TicketResponse':
        # Creating ticket with info in request
        tkt = Ticket( id = -1, token_num = -1, entry_time = datetime.datetime.now(), vehicle = None, gate = None, slot = None)

        # Getting vehicle and gate from repositories and creating if not exists
        if request.vehicle_num in self.vehicle_repo.vehicles:
            vehicle = self.vehicle_repo.get_vehicle(request.vehicle_num)
        else:
            owner = Owner(-1, request.owner_name)
            vehicle = Vehicle(request.vehicle_num, request.vehicle_type, owner)
            self.vehicle_repo.add_vehicle(request.vehicle_num, vehicle)
        # Assigning vehicle to ticket
        tkt.vehicle = vehicle

        # Getting gate from repository and creating if not exists

        if request.gate_id in self.gate_repo.gates:
            gate = self.gate_repo.get_gate(request.gate_id)
        else:
            raise ValueError(f"Gate with id {request.gate_id} does not exist.")

        # Assigning gate to ticket
        tkt.gate = gate

        # Getting parking lot and slot finder function from Factory using slot strategy in parking lot
        parking_lot = self.parking_lot_repo.get_parking_lot_by_id(tkt.gate.parking_lot_id)
        slot_finder = SlotFactory.find_slot(parking_lot.slot_strategy)

        # Getting slot using slot finder strategy
        if slot_finder is None:
            raise ValueError("No slot finder strategy found for the parking lot.")
        else:
            slot = slot_finder.get_slot(request.vehicle_type. parking_lot)

        if slot is None:
            raise ValueError("No available slots found.")

        # Assigning slot to ticket and updating slot status
        tkt.slot = slot
        tkt.slot.status = SlotStatus.OCCUPIED
        self.slot_repo.update_slot(slot)

        # Adding ticket to repository and returning ticket
        return self.ticket_repo.add_ticket(tkt)





