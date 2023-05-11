"""User Input Exceptions"""


class UserInputException(Exception):
    message_to_user = "Something went wrong. Please try again later."

    def __init__(self, *args):
        if args:
            self.message_to_user = args[0]
        super().__init__(self.message_to_user)


class InvalidDateFormat(UserInputException):
    message_to_user = "Wrong date format. Please use format YYYY-MM-DD"


class InvalidEndDateException(UserInputException):
    message_to_user = "End date can not be before start date."


class LowerBoundDateException(UserInputException):
    message_to_user = "Start date can not be before 2022-06-08."


class UpperBoundDateException(UserInputException):
    message_to_user = "End date can not be more than 15 days from today."


class UnsuccessfulConnectionError(UserInputException):
    message_to_user = "Connection to source failed. Check your internet connection."
