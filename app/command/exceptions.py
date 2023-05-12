"""User Input Exceptions"""


class UserInputException(Exception):
    """Base exception class."""
    message_to_user = "Something went wrong."

    def __init__(self, *args):
        if args:
            self.message_to_user = args[0]
        super().__init__(self.message_to_user)


class InvalidDateFormat(UserInputException):
    """Exception is raised on wrong date format input."""
    message_to_user = "Wrong date format. Please use format YYYY-MM-DD"


class InvalidEndDateException(UserInputException):
    """Exception is raised when user's end date is before start date."""
    message_to_user = "End date can not be before start date."


class LowerBoundDateException(UserInputException):
    """Exception is raised when user asks for data that exceeds sources limit."""
    message_to_user = "Start date can not be before 2022-06-08."


class UpperBoundDateException(UserInputException):
    """Exception is raised when user asks for a forecast latter than 16 days in the future."""
    message_to_user = "End date can not be more than 15 days from today."


class UnsuccessfulConnectionError(UserInputException):
    """Exception is raised on poor connection."""
    message_to_user = "Connection to source failed. Check your internet connection."
