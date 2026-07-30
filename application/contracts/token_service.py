from typing import Protocol

class TokenService(Protocol):
    def issue(self, player_id: int):
        ...