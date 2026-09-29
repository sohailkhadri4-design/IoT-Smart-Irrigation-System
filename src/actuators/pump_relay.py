from dataclasses import dataclass

@dataclass
class SimulatedRelay:
    energized:bool=False
    def set(self,enabled): self.energized=enabled

class PumpRelay:
    def __init__(self,relay): self.relay=relay
    def set_pump(self,enabled): self.relay.set(enabled)
    @property
    def pump_on(self): return self.relay.energized
