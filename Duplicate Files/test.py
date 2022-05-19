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

    @patch('builtins.open')
    @patch('main.os.path')
    @patch('main.hashlib')
    @patch('main.os')
    def test_delete_no_duplicate_files(self, mock_os, mock_hashlib, mock_os_path, mock_builtins_open):
        mock_os.walk.return_value = [('./', ['__pycache__'], ['test copy 2.txt',
                                      '.DS_Store', 'remove.py', 'test.py', 'main.py', 'test_remove.py'])]
        mock_hashlib.md5.hexdigest.side_effect = iter(
            ['a', 'b', 'c', 'd', 'e'])
        rm("any path")
        mock_os.remove.assert_not_called()


    # @patch('main.hashlib')
    # @patch('main.os')
    # def test_delete_no_duplicate_files(self, mock_os, mock_hashlib):
    #     mock_hashlib.md5.return_value = False
    #     mock_os.listdir.return_value = ['file1', 'file2']
    #     rm("any path")
    #     mock_os.remove.assert_not_called()
    # @patch('main.hashlib')
    # @patch('main.os.path')
    # @patch('main.os')
    # def test_delete_one_matching_file(self, mock_os, mock_os_path, mock_hashlib):
    #     mock_hashlib.md5.return_value = True
    #     mock_os.listdir.return_value = ['file1', 'file2']
    #     mock_os.path.exists.side_effect = [True, False]
    #     mock_os.mock_os_path.exists.side_effect = [True, False]
    #     rm("any path")
    #     mock_os.remove.assert_not_called()
    # @patch('main.hashlib')
    # @patch('main.os.path')
    # @patch('main.os')
    # def test_delete_two_matching_file(self, mock_os, mock_os_path, mock_hashlib):
    #     mock_hashlib.md5.return_value = True
    #     mock_os.listdir.return_value = ['file1', 'file2']
    #     mock_os.path.exists.side_effect = [True, True]
    #     mock_os.mock_os_path.exists.side_effect = [True, True]
    #     rm("any path")
    #     mock_os.remove.assert_called()
if __name__ == '__main__':
    unittest.main()
