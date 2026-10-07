import os
import tempfile
import unittest

from gradebook.core import (
    WEIGHTS,
    StudentRecord,
    letter_grade,
    load_records,
    rank_students,
    weighted_final_score,
)


class WeightedScoreTests(unittest.TestCase):
    def test_weights_sum_to_one(self):
        self.assertAlmostEqual(sum(WEIGHTS.values()), 1.0)

    def test_each_part_is_weighted(self):
        record = StudentRecord("Ana", homework=100, midterm=50, final=75)
        self.assertEqual(weighted_final_score(record), 75.0)


class LetterGradeTests(unittest.TestCase):
    def test_bounds_are_inclusive(self):
        self.assertEqual(letter_grade(90), "A")
        self.assertEqual(letter_grade(89.9), "B")
        self.assertEqual(letter_grade(60), "D")

    def test_below_sixty_fails(self):
        self.assertEqual(letter_grade(59.9), "F")


class RankingTests(unittest.TestCase):
    def test_highest_first_and_ties_alphabetical(self):
        records = [
            StudentRecord("Zana", 80, 80, 80),
            StudentRecord("Besa", 80, 80, 80),
            StudentRecord("Arta", 95, 95, 95),
        ]
        names = [name for _, name in rank_students(records)]
        self.assertEqual(names, ["Arta", "Besa", "Zana"])


class LoadRecordsTests(unittest.TestCase):
    def _write(self, text):
        handle = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
        handle.write(text)
        handle.close()
        self.addCleanup(os.remove, handle.name)
        return handle.name

    def test_reads_rows(self):
        path = self._write("name,homework,midterm,final\n Ana ,90,80,70\n")
        records = load_records(path)
        self.assertEqual(records, [StudentRecord("Ana", 90.0, 80.0, 70.0)])

    def test_rejects_scores_out_of_range(self):
        path = self._write("name,homework,midterm,final\nAna,101,80,70\n")
        with self.assertRaises(ValueError):
            load_records(path)


if __name__ == "__main__":
    unittest.main()
