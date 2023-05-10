from app.base import BaseAPPException


class NoCityDataException(BaseAPPException):
    message_to_user = "Sorry, we have no data for chosen city."
    status_code = 200
