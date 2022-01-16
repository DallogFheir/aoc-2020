import unittest
from passport import Passport
from pathlib import Path

class TestPassport(unittest.TestCase):
    def test_validate_data(self):
        path = Path("tests", "data")

        with open(path / "valid.txt") as f:
            valid = Passport.parse_passports(f)

        with open(path / "invalid.txt") as f:
            invalid = Passport.parse_passports(f)

        for pport in valid:
            self.assertTrue(pport.validate())
        
        for pport in invalid:
            self.assertFalse(pport.validate())
