import unittest
from unittest.mock import patch
from assignmentpkg.analysis import Analysis

class TestAnalysisMethods(unittest.TestCase):

    @patch('assignmentpkg.analysis.requests.get')
    def test_load_data_success(self, mock_get):
        # Mock response setup
        mock_get.return_value.json.return_value = {"response": {"docs": []}}
        mock_get.return_value.status_code = 200

        # Instantiate Analysis object with the path to the config file
        analysis = Analysis('config/config.yml')

        # Call the load_data method
        analysis.load_data()

        # Check if requests.get was called
        if mock_get.call_args:
            actual_url_called = mock_get.call_args[0][0]

            # encoding spaces
            api_settings = analysis.config['api_settings']
            expected_url = f"{api_settings['base_url']}?q={api_settings['topic']}&api-key={api_settings['api_key']}"

            # correct URL
            self.assertEqual(actual_url_called, expected_url)
        else:
            self.fail("No API call was made.")

if __name__ == '__main__':
    unittest.main()
