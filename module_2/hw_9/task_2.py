from task_1.task_1 import ContextManager
import unittest


class TestContextManager(unittest.TestCase):
    list_of_mods = ["w", "r", "a", "b", "x", "t", "r+", "w+", "a+", "rb", "wb", "ab"]

    def setUp(self) -> None:
        self.context_manager = ContextManager("task_1.txt", "w")

    def test_type_of_filename(self):
        self.assertEqual(self.context_manager.file_name, "task_1.txt")

    def test_mode_is_valid(self):
        self.assertIn(self.context_manager.mode, self.list_of_mods)


if __name__ == "__main__":
    unittest.main()
