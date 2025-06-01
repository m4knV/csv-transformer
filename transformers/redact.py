import logging
import re

from faker import Faker

faker = Faker()


def redact(value: str) -> str:
    """
    Redacts sensitive information from the input value by replacing it with fake data.

    @param value: The input value that may contain sensitive information such as an email, phone number, or name.
    @type value: str

    @return: A string with the sensitive information replaced by a fake email, phone number, or name.

    The function performs the following redactions
    - If the input contains an '@' symbol, it is assumed to be an email and is replaced with a fake email.
    - If the input is a string without a '@' symbol and matches the regex for a name, it is replaced with a fake name.
    - Otherwise, the input is returned unchanged.
    """
    # Convert the input value to a string
    value = str(value)

    # Check for email and return a fake email
    if "@" in value:
        fake_email = faker.email()
        logging.info(f"Redacting email: {value} with fake email: {fake_email}")
        return fake_email
    # Check for name and return a fake name
    elif "@" not in value and re.match(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$", value):
        fake_name = faker.name()
        logging.info(f"Redacting name: {value} with fake name: {fake_name}")
        return fake_name
    # Return original value otherwise
    logging.info(f"Returning original value: {value}")
    return value
