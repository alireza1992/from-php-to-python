from typing import Protocol

class TokenProtocol(Protocol):
    def issue(self, player_id: int):
        ...