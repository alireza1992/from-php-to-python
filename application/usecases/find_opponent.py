from application.contracts.player import PlayerProtocol


class FindAnOpponent:
    def __init__(self, player_repository: PlayerProtocol):
        self.player_repository = player_repository

    async def execute(self, player_id: int, xp_level: int):
        player = await self.player_repository.get_by_id(player_id)
        print(player.username, xp_level)
