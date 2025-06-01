from enum import Enum

from .convert_timestamp import convert_timestamp
from .redact import redact
from .uuid_to_int import uuid_to_int


class TransformType(str, Enum):
    UUID_TO_INT = "uuid_to_int"
    REDACT = "redact"
    CONVERT_TIMESTAMP = "convert_timestamp"


TRANSFORM_FUNCTIONS = {
    TransformType.UUID_TO_INT: uuid_to_int,
    TransformType.REDACT: redact,
    TransformType.CONVERT_TIMESTAMP: convert_timestamp,
}

