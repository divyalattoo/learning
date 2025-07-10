from ParkingLot.Src.Models.Models import SlotStrategy
from ParkingLot.Src.Helpers.Strategies.SlotFinder import SlotFinderFirst


class SlotFactory:

    @staticmethod
    def find_slot(slot_strategy: SlotStrategy):
        if slot_strategy == SlotStrategy.FIRST_AVAILABLE:
            return SlotFinderFirst()
        elif slot_strategy == SlotStrategy.NEAREST_ENTRY:
            pass
        elif slot_strategy == SlotStrategy.NEAREST_EXIT:
            pass
        else:
            raise ValueError(f"Invalid slot strategy: {slot_strategy}")
        return None