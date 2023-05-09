"""User Input Exceptions"""
from app.base import BaseAPPException


class InvalidDateFormat(BaseAPPException):
    message_to_user = "Wrong date format. Please use format YYYY-MM-DD"


class InvalidEndDateException(BaseAPPException):
    message_to_user = "End date can not be before start date."


class LowerBoundDateException(BaseAPPException):
    message_to_user = "Start date can not be before 2022-06-08."


class UpperBoundDateException(BaseAPPException):
    message_to_user = "End date can not be more than 16 days from today."
