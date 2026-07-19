from enum import Enum


class DeactivationReason(Enum):
    """
    Why user is deactivating her account.
    """
    TECHNICAL_ISSUES = 1000
    BAD_UX = 1001
    LOST_INTEREST = 1002
    LOW_ONLINE_USERS = 1003
    NO_TIME_TO_PLAY = 1004
    BAD_SUPPORT = 1005
    BAD_SCORING_SYSTEM = 1006