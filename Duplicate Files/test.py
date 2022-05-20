from main import rm

import unittest
from unittest.mock import patch


class RmTestCase(unittest.TestCase):

    @patch('main.os')
    def test_delete_no_files(self, mock_os):
        # We are testing an empty directory
        mock_os.walk.return_value = []
        rm("any path")
        mock_os.remove.assert_not_called()

    @patch('main.os.path')
    @patch('main.hashlib')
    @patch('main.os')
    def test_delete_no_duplicate_files(self, mock_os, mock_hashlib, mock_os_path):
        mock_os.walk.return_value = [('./', [], ['file1.py', 'file2.py', ])]
        mock_hashlib.md5.return_value.hexdigest.side_effect = ['a', 'b']
        rm("any path")
        mock_os.remove.assert_not_called()

    @patch('builtins.open')
    @patch('main.os.path')
    @patch('main.hashlib')
    @patch('main.os')
    def test_delete_one_matching_file(self, mock_os, mock_hashlib, mock_os_path, mock_open):
        print("s")
        mock_os.walk.return_value = [('./', [], ['file1.py', 'file2.py', ])]
        mock_hashlib.md5.return_value.hexdigest.side_effect = ['a', 'a']
        rm("any path")
        mock_os.remove.assert_called()
        self.assertEqual(mock_os.remove.call_count, 1)

        @patch('builtins.open')
        @patch('main.hashlib')
        @patch('main.os.path')
        @patch('main.os')
        def test_delete_two_matching_file(self, mock_os, mock_os_path, mock_hashlib, mock_open):
            mock_os.walk.return_value = [
                ('./', [], ['file1.py', 'file2.py', 'file3.py'])]
            mock_hashlib.md5.return_value.hexdigest.side_effect = [
                'a', 'a', 'a']
            rm("any path")
            mock_os.remove.assert_called()
            self.assertEqual(mock_os.remove.call_count, 2)


if __name__ == '__main__':
    unittest.main()
