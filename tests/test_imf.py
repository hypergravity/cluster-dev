import unittest

from mock_cmd.imf import sample_imf_new


class TestIMF(unittest.TestCase):
    def test_sample_imf(self):
        result = sample_imf_new()
        self.assertEqual(result, 1, "result should be 1")
