import unittest
from unittest.mock import MagicMock
from e164_python.e164 import E164
from e164_python.response import Response

class TestE164(unittest.TestCase):

    def setUp(self):
        self.mock_client = MagicMock()
        self.e164 = E164(client=self.mock_client)

    def test_lookup_valid_number(self):
        # Mock response data
        mock_response_data = {
            "prefix": "44113391",
            "calling_code": "44",
            "iso3": "GBR",
            "tadig": None,
            "mccmnc": "234",
            "type": "GEOGRAPHIC",
            "location": None,
            "operator_brand": "BT",
            "operator_company": "BT",
            "total_length_min": "12",
            "total_length_max": "12",
            "weight": "11",
            "source": "e164.com",
        }
        mock_response = MagicMock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = MagicMock()
        self.mock_client.get.return_value = mock_response

        # Call the method
        result = self.e164.lookup("441133910781")

        # Assertions
        self.mock_client.get.assert_called_once_with("https://e164.com/441133910781")
        self.assertIsInstance(result, Response)
        self.assertEqual(result.prefix, "44113391")
        self.assertEqual(result.calling_code, "44")
        self.assertEqual(result.iso3, "GBR")
        self.assertIsNone(result.tadig)
        self.assertEqual(result.mccmnc, "234")
        self.assertEqual(result.type, "GEOGRAPHIC")
        self.assertIsNone(result.location)
        self.assertEqual(result.operator_brand, "BT")
        self.assertEqual(result.operator_company, "BT")
        self.assertEqual(result.total_length_min, "12")
        self.assertEqual(result.total_length_max, "12")
        self.assertEqual(result.weight, "11")
        self.assertEqual(result.source, "e164.com")

    def test_lookup_invalid_number(self):
        # Mock response with empty data
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = MagicMock()
        self.mock_client.get.return_value = mock_response

        # Call the method and assert exception
        with self.assertRaises(ValueError) as context:
            self.e164.lookup("000000000")
        self.assertIn("Invalid phone number", str(context.exception))

    def test_lookup_http_error(self):
        # Mock HTTP error
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("HTTP Error")
        self.mock_client.get.return_value = mock_response

        # Call the method and assert exception
        with self.assertRaises(ValueError) as context:
            self.e164.lookup("+1234567890")
        self.assertIn("Error during lookup", str(context.exception))

if __name__ == "__main__":
    unittest.main()
