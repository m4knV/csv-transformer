import unittest

from transformers.redact import redact


class TestRedact(unittest.TestCase):
    def test_redact_email(self):
        email = "test@example.com"
        redacted_email = redact(email)
        self.assertNotEqual(redacted_email, email)
        self.assertIn("@", redacted_email)

    def test_redact_name(self):
        name = "John Doe"
        redacted_name = redact(name)
        self.assertNotEqual(redacted_name, name)

    def test_no_redaction(self):
        text = "No sensitive info"
        self.assertEqual(redact(text), text)


if __name__ == "__main__":
    unittest.main()
