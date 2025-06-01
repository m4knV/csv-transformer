import logging

from dateutil import parser
from dateutil.tz import gettz


def convert_timestamp(value: str) -> str:
    """
    Converts a timestamp string into a standardized date format (YYYY-MM-DD).

    @param value: The timestamp value that needs to be converted. It can be in various formats.
    @type value: str

    @return: A string representing the date in the format YYYY-MM-DD. If the input cannot be parsed, the original value is returned.
    """
    try:
        # Timezones Mapping
        tzinfos = {
            "CET": gettz("Europe/Paris"),  # Central European Time
        }

        # Parse the timestamp with timezone information
        parsed_dt = parser.parse(value, tzinfos=tzinfos)

        # Convert the parsed timestamp to the desired format
        converted_dt = parsed_dt.strftime("%Y-%m-%d")
        logging.info(f"Converting timestamp: {value} to {converted_dt}")

        return converted_dt
    except (ValueError, TypeError):
        # Return the original value if conversion fails
        logging.error(f"Failed to convert timestamp: {value}")
        return value
