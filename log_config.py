LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "app": {
            "format": "%(levelname)s | %(message)s | %(asctime)s | %(name)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "infra": {
            "format": "%(levelname)s | %(message)s | %(asctime)s | %(name)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "app": {"formatter": "app", "class": "logging.StreamHandler", "stream": "ext://sys.stdout"},
        "infra": {"formatter": "infra", "class": "logging.StreamHandler", "stream": "ext://sys.stdout"},
    },
    "loggers": {
        "main": {"handlers": ["app"], "level": "INFO", "propagate": False},
        "application": {"handlers": ["app"], "level": "INFO", "propagate": False},
        "infrastructure": {"handlers": ["infra"], "level": "WARNING", "propagate": False},
    },
}
