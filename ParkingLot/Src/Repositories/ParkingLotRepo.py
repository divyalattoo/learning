class ParkingLotRepo:
    def __init__(self):
        self.parking_lots = {}
        self.count = 0

    def add_parking_lot(self, parking_lot):
        id_generated = self.count + 1
        parking_lot.id = id_generated
        self.count += 1
        self.parking_lots[parking_lot.id] = parking_lot
        return parking_lot

    def get_parking_lot(self, parking_lot_id):
        return self.parking_lots.get(parking_lot_id)

    def remove_parking_lot(self, parking_lot_id):
        if parking_lot_id in self.parking_lots:
            del self.parking_lots[parking_lot_id]