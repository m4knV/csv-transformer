import unittest

from transformers.uuid_to_int import uuid_to_int


class TestUUIDToInt(unittest.TestCase):
    def test_uuid_to_int(self):
        uuid1 = "123e4567-e89b-12d3-a456-426614174000"
        int1 = uuid_to_int(uuid1)
        self.assertEqual(int1, 1)

        int2 = uuid_to_int(uuid1)
        self.assertEqual(int2, 1)

        uuid2 = "123e4567-e89b-12d3-a456-426614174001"
        int3 = uuid_to_int(uuid2)
        self.assertEqual(int3, 2)


if __name__ == "__main__":
    unittest.main()
