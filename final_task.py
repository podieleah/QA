# write an application that checks the strength of a password.
# Requirements:
#
# Write a class that has a method that checks the password strength.
# Use factors like length, upper/lower case and if it has a number and special character.
# ratings should be very weak - weak - moderate - strong - very strong
# Check against a list of common passwords 10-20 common password = very weak
# User input that loops until the user quits
# A dictionary that returns a history of passwords/strengths whilst in the loop.

# stretch goal - add feedback to the user to advise on improving their password.

# Write tests to check your code logic.
# Achieve a high score with pylint.

# All to push to repos
# 12.15 deadline



import re

COMMON_PASSWORDS = [
    "password", "123456", "123456789", "12345678", "12345", "1234567", "qwerty",
    "abc123", "password1", "admin", "welcome"
]

class PasswordChecker:
    def __init__(self):
        self.history = {}

    def check_strength(self, password):
        if password in COMMON_PASSWORDS:
            return "very weak"


        length_criteria = len(password) >= 8
        upper_criteria = re.search(r"[A-Z]", password) is not None
        lower_criteria = re.search(r"[a-z]", password) is not None
        digit_criteria = re.search(r"\d", password) is not None
        special_char_criteria = re.search(r"\W", password) is not None


        score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_char_criteria])

        if score == 0:
            return "very weak"
        elif score == 1:
            return "weak"
        elif score == 2:
            return "moderate"
        elif score == 3:
            return "strong"
        else:
            return "very strong"

    def run(self):
        while True:
            password = input("Enter your password (or type 'quit' to exit): ")
            if password.lower() == 'quit':
                break

            strength = self.check_strength(password)
            self.history[password] = strength

            print(f"Password strength: {strength}")

        print("\nPassword Strength History:")
        for pwd, strength in self.history.items():
            print(f"Password: {pwd}, Strength: {strength}")

PasswordChecker().run()