import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import inspection_processor

# inspection_manager runs its menu on import, so answer "6" (Exit) to skip it.
with patch("builtins.input", return_value="6"), redirect_stdout(io.StringIO()):
    import inspection_manager


class TestInspectionManager(unittest.TestCase):
    """Tests for score validation, average calculation and searching."""

    def setUp(self):
        fd, self.csv_path = tempfile.mkstemp(suffix=".csv")
        with os.fdopen(fd, "w", newline="") as f:
            f.write(
                "inspection_id,equipment_code,facility,technician,inspection_score,status\n"
                "INSP001,EQ-2045,Pretoria Central Clinic,Lerato Mokoena,87,Operational\n"
                "INSP002,EQ-3182,Soweto Clinic,Thabo Nkosi,73,Review\n"
            )

    def tearDown(self):
        os.remove(self.csv_path)

    def run_and_capture(self, func, *args, user_input=None):
        output = io.StringIO()
        with patch("builtins.input", return_value=user_input), redirect_stdout(output):
            func(*args)
        return output.getvalue()

    def test_valid_score(self):
        self.assertTrue(inspection_processor.validate_score("87"))

    def test_negative_score(self):
        self.assertFalse(inspection_processor.validate_score("-5"))

    def test_score_above_100(self):
        self.assertFalse(inspection_processor.validate_score("101"))

    def test_average_score(self):
        output = self.run_and_capture(
            inspection_manager.calculate_average_score, self.csv_path
        )
        self.assertIn("Average score: 80.00", output)

    def test_successful_search(self):
        output = self.run_and_capture(
            inspection_manager.find_inspection,
            self.csv_path,
            inspection_manager.FIELDNAMES,
            user_input="INSP001",
        )
        self.assertIn("EQ-2045", output)
        self.assertNotIn("No match found", output)

    def test_unsuccessful_search(self):
        output = self.run_and_capture(
            inspection_manager.find_inspection,
            self.csv_path,
            inspection_manager.FIELDNAMES,
            user_input="INSP999",
        )
        self.assertIn("No match found", output)


if __name__ == "__main__":
    unittest.main()
