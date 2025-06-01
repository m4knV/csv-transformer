import unittest

import pandas as pd

from processor import transform_columns


class TestTransformColumns(unittest.TestCase):
    def test_transform_columns(self):
        df = pd.DataFrame(
            {"user_id": ["123e4567-e89b-12d3-a456-426614174000"], "name": ["John Doe"]}
        )
        transform_config = {"user_id": "uuid_to_int", "name": "redact"}
        transformed_df = transform_columns(df, transform_config)
        self.assertEqual(transformed_df["user_id"].iloc[0], 1)
        self.assertNotEqual(transformed_df["name"].iloc[0], "John Doe")


if __name__ == "__main__":
    unittest.main()
