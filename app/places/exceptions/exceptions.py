from app.base import BaseAPPException


class NoCityDifferencesException(BaseAPPException):
    message_to_user = "No data to compare for chosen city."
    status_code = 200
