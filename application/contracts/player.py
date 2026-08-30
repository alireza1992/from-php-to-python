from typing import Protocol


class PlayerProtocol(Protocol):
    async def get_by_id(self):
        ...