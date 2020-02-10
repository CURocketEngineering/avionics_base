
from .low_level.low_comm import Antenna

class Comm:
    def __init__(self):
        self._antenna = Antenna()

    def send(self):
        return None

    def receive(self):
        return None
