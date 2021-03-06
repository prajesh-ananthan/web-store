__author__ = "Prajesh Ananthan"


class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotExistsError(UserError):
    pass


class IncorrectPasswordError(UserError):
    pass

class InvalidEmailError(UserError):
    pass

class UserAlreadyRegisteredError(UserError):
    pass
