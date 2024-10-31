
import  mock 
from unittest import mock
import main
import unittest

class TestMain(unittest.TestCase):  # TestCaseを継承
    def test_example(self):  # テストメソッドはtest_で始まる必要がある
        # ここにテストコードを追加
        self.assertEqual(1, 1)  
        
    # テスト用のデータを準備
main.bookname_entry = mock.Mock()
main.authorname_entry = mock.Mock()
main.price_entry = mock.Mock()