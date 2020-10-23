#A minimal script for generating secure passwords.
#Flask is app.py
import secrets
import string

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

## TODO Make it easier to copy generated password. Display the amount of PW combinations according to user input of how long the password should be.