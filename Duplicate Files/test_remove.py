from remove import rm

import mock
import unittest

"""
At runtime, the remove module has its own os which is imported into its own local scope in the module. 
Thus, if we mock os, we won’t see the effects of the mock in the remove module.
"""


class RmTestCase(unittest.TestCase):
    # Patch 1 corresponds with attribute 2 (remove.os.path and mock_path)
    @mock.patch('remove.os.path')
    @mock.patch('remove.os')
    def test_rm(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        rm("any path")
        self.assertFalse(mock_os.remove.called,
                         "Failed to not remove the file if not present.")

        mock_path.isfile.return_value = True
        rm("any path")
        mock_os.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
