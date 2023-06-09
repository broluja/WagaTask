"""Base APP Exception class"""


class BaseAPPException(Exception):
    message_to_user = "Something went wrong."
    status_code = 400

    def __init__(self, *args):
        if args:
            self.message_to_user = args[0]
        super().__init__(self.message_to_user)
