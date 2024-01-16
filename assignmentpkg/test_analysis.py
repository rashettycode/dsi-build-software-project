import unittest
from assignmentpkg.analysis import Analysis

class TestAnalysis(unittest.TestCase):
    def setUp(self):
        config_paths = ['configs/system_config.yml', 'configs/user_config.yml']
        self.analysis = Analysis(config_paths)

    def test_load_data(self):
        data = self.analysis.load_data()
        self.assertIsNotNone(data)

    def test_calculate_mean(self):
        self.analysis.load_data()
        mean_word_count = self.analysis.calculate_mean('word_count')
        self.assertIsInstance(mean_word_count, float)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

