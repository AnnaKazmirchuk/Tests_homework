import unittest
from unittest.mock import patch

import main
from main import request_doc_number, request_doc_shelf, add_new_doc, documents, directories

class TestFunctions(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    @patch('main.input')
    def test_request_doc_number(self, mock_input):
        mock_input.return_value = "10006"
        self.assertEqual(request_doc_number(documents), "Аристарх Павлов")

    @patch('main.input')
    def test_request_doc_shelf(self, mock_input):
        mock_input.return_value = "11-2"
        self.assertIn(request_doc_shelf(documents), 'Номер полки 1')

    @patch('main.input')
    def test_add_new_doc(self, mock_input):
        mock_input.side_effect = ["invoice", "111", "Anna", '3']
        self.assertTrue(add_new_doc(documents))


if __name__ == '__main__':
    unittest.main()