import re

from passlib.hash import pbkdf2_sha512

__author__ = "Prajesh Ananthan"

EMAIL_PATTERN = '^[\w-]+@([\w-]+\.)+[\w]+$'


class Utils(object):

    def hash_password(password):
        """
        Hashes the password using pbkdf2_sha512
        :return: A sha512 -> pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password that the user sent matches that of the database.
        The database password is encrypted more than the user's password at this stage
        :param hashed_password:
        :return:
        """

        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def email_is_valid(email):
        # Checks for valid email format
        email_address_matcher = re.compile(EMAIL_PATTERN)
        return True if email_address_matcher.match(email) else False
