import unittest
from todo_task import TodoTask

class taskTest(unittest.TestCase):
    def setUp(self):
        self.complete_task = TodoTask(complete=True, description="Get milk")
        self.incomplete_task = TodoTask(complete=False, description="Get milk")

    def test_task_correct_str_conversion_if_complete(self):
        self.assertEqual(str(self.complete_task), "[x] Get milk")

    def test_task_correct_str_conversion_if_incomplete(self):
        self.assertEqual(str(self.incomplete_task), "[] Get milk")


if __name__ == "__main__":
    unittest.main()
    