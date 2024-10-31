# tests/test_main.py
import unittest
from unittest import mock
import mock  # mockを直接インポート
import main


class TestMain(unittest.TestCase):  # TestCaseを継承
    def test_example(self):  # テストメソッドはtest_で始まる必要がある
        # ここにテストコードを追加
        self.assertEqual(1, 1)  
    # テスト用
    # のデータを準備
main.bookname_entry = mock.Mock()
main.authorname_entry = mock.Mock()
main.price_entry = mock.Mock()
# ... existing code ...