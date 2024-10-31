import unittest

class TestMain(unittest.TestCase):  # TestCaseを継承
    def test_example(self):  # テストメソッドはtest_で始まる必要がある
        self.assertEqual(1, 1)  