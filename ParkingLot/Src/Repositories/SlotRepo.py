class SlotRepo:
    def __init__(self):
        self.slot_repo = {}
        self.count = -1

    def find_slot_byid(self, slot_id):
        return self.slot_repo.get(slot_id, None)

    def add_slot(self, slot):
        if slot.id in self.slot_repo:
            raise ValueError(f"Slot with id {slot.id} already exists.")
        id_generated = self.count + 1
        slot.id = id_generated
        slot.slot_number = id_generated
        self.count += 1
        self.slot_repo[slot.id] = slot
        return slot

    def update_slot(self, slot):
        if slot.id not in self.slot_repo:
            raise ValueError(f"Slot with id {slot.id} does not exist.")
        self.slot_repo[slot.id] = slot

    def delete_slot(self, slot_id):
        if slot_id not in self.slot_repo:
            raise ValueError(f"Slot with id {slot_id} does not exist.")
        del self.slot_repo[slot_id]