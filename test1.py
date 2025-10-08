# test_log_generator.py
import unittest
import log_generator  # make sure this matches your filename

class TestLogGenerator(unittest.TestCase):
    def test_log_count(self):
        self.assertEqual(len(log_generator.logs), 10000)

    def test_log_structure(self):
        sample = log_generator.logs[0]
        self.assertIn('timestamp', sample)
        self.assertIn('level', sample)
        self.assertIn('message', sample)

if __name__ == '__main__':
    unittest.main()
