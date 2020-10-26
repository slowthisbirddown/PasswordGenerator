#A minimal script for generating secure passwords.
#Flask is app.py
## TODO Make it easier to copy generated password. Display the amount of PW combinations according to user input of how long the password should be.
import secrets
import string
from math import factorial
class PasswordGenerator:

    def generate_password(self, length = 13):
        """generate_password

        Args:
            length (int, optional): Length of password. Defaults to 13.

        Returns:
            string: Generated Password
        """
        alphabet = string.ascii_letters + string.digits + '!@#$%^&*()}{_+-='
        password = ''.join(secrets.choice(alphabet) for i in range(int(length)))
        return password