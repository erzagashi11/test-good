import unittest

from gradebook.core import StudentRecord
from gradebook.report import format_report


class FormatReportTests(unittest.TestCase):
    def test_lists_students_in_rank_order_with_average(self):
        report = format_report([StudentRecord("Besa", 70, 70, 70), StudentRecord("Arta", 90, 90, 90)])
        lines = report.splitlines()
        self.assertIn("Arta", lines[1])
        self.assertIn("Besa", lines[2])
        self.assertEqual(lines[-1], "Class average: 80.0")

    def test_empty_class_has_no_average(self):
        self.assertNotIn("average", format_report([]))


if __name__ == "__main__":
    unittest.main()
