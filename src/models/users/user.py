import uuid

import src.models.users.errors as UserErrors
from src.common.database import Database
from src.common.utils import Utils

__author__ = "Prajesh Ananthan"


class User(object):
    COLLECTION = "users"

    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies the email/password combo is valid or not.
        Checks if the email exists, and the password associated is correct.
        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """

        user = Database.find_one(User.COLLECTION, {"email": email})
        if user is None:
            # Tell the user that their email does not exist
            raise UserErrors.UserNotExistsError("User does not exist!")

        if not Utils.check_hashed_password(password, user['password']):
            # Tell the user the password is wrong
            raise UserErrors.IncorrectPasswordError("Invalid password!")

        return True

    @staticmethod
    def register_user(email, password):
        """
        Registers user in the system.
        :param email: The user's email
        :param password: The user's password
        :return: Returns true if the registration is successful or False otherwise
        """

        user_data = Database.find_one("%s" % User.COLLECTION, {"email": email})

        if user_data is not None:
            # Tell user they are already registered
            raise UserErrors.UserAlreadyRegisteredError("User already registered!")

        if not Utils.email_is_valid(email):
            # Tell the user email is not constructed properly
            raise UserErrors.InvalidEmailError("Invalid email format!")

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert(User.COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }
