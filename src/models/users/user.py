import uuid

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors

__author__ = "Prajesh Ananthan"


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def isLoginValid(email, password):
        """
        This method verifies the email/password combo is valid or not.
        Checks if the email exists, and the password associated is correct.
        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """

        user = Database.find_one("users", {"email": email})
        if user is None:
            # Tell the user that their email does not exist
            raise UserErrors.UserNotExistsError("User does not exist!")

        if not Utils.check_hashed_password(password, user['password']):
            # Tell the user the password is wrong
            raise UserErrors.IncorrectPasswordError("Invalid password!")

        return True
