import unittest
from unittest.mock import patch
from main import check_document_existance, delete_doc, get_all_doc_owners_names, get_doc_owner_name, get_doc_shelf, move_doc_to_shelf, \
    remove_doc_from_shelf, add_new_doc, add_new_shelf, append_doc_to_shelf, directories, show_all_docs_info, show_document_info, documents


class TestSecretaryProgram(unittest.TestCase):

    def test_check_document_existance(self):
        self.assertTrue(check_document_existance("2207 876234"))
        self.assertTrue(check_document_existance("11-2"))
        self.assertFalse(check_document_existance("12345"))

    def test_get_all_docs_owner_names(self):
        user_list = ["Василий Гупкин", "Геннадий Покемонов",
                     "Аристарх Павлов", "Алексей Кузин"]
        self.assertEqual(get_all_doc_owners_names(), set(user_list))

    @patch('builtins.input', lambda *args: "2207 876234")
    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name(), "Василий Гупкин")

    @patch('builtins.input', lambda *args: "2207 876234")
    def test_get_doc_shelf_eq(self):
        self.assertEqual(get_doc_shelf(), '1')

    @patch('builtins.input', lambda *args: "12345")
    def test_get_doc_shelf_not_eq(self):
        self.assertEqual(get_doc_shelf(), None)

    def test_remove_doc_from_shelf(self):
        updated_shelf = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': [],
            '3': ['4510 123123'],
            '4': ['4510 123123'],
            '5': []
        }
        self.assertEqual(remove_doc_from_shelf('10006'), None)
        remove_doc_from_shelf('10006')
        self.assertEqual(directories, updated_shelf)

    @patch('builtins.input', side_effect=['4510 123123', 'passport', 'Алексей Кузин', '4'])
    def test_add_new_doc(self, mock_inputs):
        self.assertEqual(add_new_doc(), '4')

    @patch('builtins.input', lambda *args: '4510 123123')
    def test_append_doc_to_shelf(self):
        append_doc_to_shelf('4510 123123', '3')
        self.assertEqual(get_doc_shelf(), '3')

    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf('4'), ('4', False))
        self.assertEqual(add_new_shelf('5'), ('5', True))

    @patch('builtins.input', side_effect=['4510 111111', 'passport', 'Виктор Цой', '3', '4510 111111'])
    def test_delete_doc(self, mock_inputs):
        add_new_doc()
        self.assertEqual(delete_doc(), ('4510 111111', True))

    @patch('builtins.input', side_effect=['4510 111111', 'passport', 'Виктор Цой', '2', '4510 111111', '5', '4510 111111'])
    def test_move_doc_to_shelf(self, mock_inputs):
        add_new_doc()
        move_doc_to_shelf()
        self.assertEqual(get_doc_shelf(), '5')
        remove_doc_from_shelf('4510 111111')

    @patch('builtins.input', side_effect=['4510 111111', 'passport', 'Виктор Цой', '2', '4510 111111'])
    def test_show_document_info(self, mock_inputs):
        add_new_doc()
        self.assertEqual(show_document_info(
            documents[-1]), ('passport', '4510 111111', 'Виктор Цой'))
        delete_doc()

    def test_show_all_docs_info(self):
        self.assertEqual(show_all_docs_info(), documents)