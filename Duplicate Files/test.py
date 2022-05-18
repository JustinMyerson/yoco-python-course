from main import rm

import unittest
from unittest.mock import patch


class RmTestCase(unittest.TestCase):
    @patch('main.rm')
    @patch('main.os.path')
    @patch('main.os.remove')
    def test_rm_empty_directory(self, mock_rm):
        # TODO: Make an empty directory
        fake_directory = "./fake_directory"

        # TODO: Run function on that directory
        rm(fake_directory)

        # TODO: Assert that mock of main.rm() is never called
        mock_rm.remove.assert_not_called()

    @patch('main.rm')
    def test_rm_one_duplicate(self, mock_rm):
        # TODO: Make a directory
        fake_directory = "./fake_directory"

        mock_rm.listdir.return_value = ["file1", "file2", "file3"]

        mock_rm.path.isfile.return_value = True


if __name__ == '__main__':
    unittest.main()
