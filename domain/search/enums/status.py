from enum import Enum

class SearchStatus(Enum):
    REQUESTED = 1
    MATCHED   = 2
    CANCELED  = 3
    ENDED     = 5
    UNFINISHED= 6
