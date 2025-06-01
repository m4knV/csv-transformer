import logging

_uuid_map = {}
_counter = 1


def uuid_to_int(value: str) -> int:
    """
    Converts a UUID to an integer. This function maintains a mapping of UUIDs to unique integers.
    If the UUID has not been seen before, it assigns a new unique integer to it.

    @param value: A string representing the UUID to be converted.
    @return: An integer that uniquely represents the given UUID.
    """
    global _counter
    if value not in _uuid_map:
        logging.info("New UUID detected")
        _uuid_map[value] = _counter
        _counter += 1
    logging.info(f"Converting UUID: {value} to integer: {_uuid_map[value]}")
    return _uuid_map[value]
