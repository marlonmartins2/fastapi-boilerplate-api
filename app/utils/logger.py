import logging


class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        return (
            record.args and len(record.args) >= 3 and record.args[2] != "/health_check"
        )


# create logging formatter
logFormatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# create logger
logger = logging.getLogger("app")
logging.getLogger("uvicorn.access").addFilter(EndpointFilter())
logger.setLevel(logging.DEBUG)

# create console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(logFormatter)

# Add console handler to logger
logger.addHandler(consoleHandler)
