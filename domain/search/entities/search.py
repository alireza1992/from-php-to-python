from typing import Optional
from dataclasses import dataclass
from domain.search.enums.status import SearchStatus


@dataclass(eq=False, kw_only=True, slots=True)
class Search:
    id: Optional[int] = None
    xp_level: int
    status: SearchStatus = SearchStatus.REQUESTED
    user_id: int

    def __eq__(self, other: object) -> bool:
        return (
                isinstance(other, self.__class__) and
                self.id == other.id
        )

    def __hash__(self) -> int:
        return hash((self.__class__, self.id))
