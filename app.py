import logging

from sanic import Request, Sanic, json

# from sanic.exceptions import SanicException
# from sanic.log import LOGGING_CONFIG_DEFAULTS


# LOGGING_FORMAT = (
#     "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: " "%(request_id)s %(request)s %(message)s %(status)d %(byte)d"
# )

# old_factory = logging.getLogRecordFactory()


# def record_factory(*args, **kwargs):
#     record = old_factory(*args, **kwargs)
#     record.request_id = ""

#     try:
#         request = Request.get_current()
#     except SanicException:
#         ...
#     else:
#         record.request_id = str(request.id)

#     return record


# logging.setLogRecordFactory(record_factory)

# LOGGING_CONFIG_DEFAULTS["formatters"]["access"]["format"] = LOGGING_FORMAT

# app = Sanic("forum_checker", log_config=LOGGING_CONFIG_DEFAULTS)
app = Sanic("forum_checker")

app.static("/static/", "/static/")

# Отключаем доки для API
app.config.OAS = False
