from Beetroot_homeworks.module_2.hw_8.task_2.phonebook_file import search_by_full_name
import unittest


class Test_PhoneBook(unittest.TestCase):
    # Если тестируете например 'Maxim Kostenko', то все функции кроме test_full_name_user_4, должны быть закоментированы
    def test_full_name_user_1(self):
        self.assertEqual(search_by_full_name(), "\nName: John\nSurname: Doe\nTelephone number: 1234567890\n"
                                                "City: New York\nState: NY")

    def test_full_name_user_2(self):
        self.assertEqual(search_by_full_name(), "\nName: Jane\nSurname: Smith\nTelephone number: 9876543210\n"
                                                "City: Los Angeles\nState: CA")

    def test_full_name_user_3(self):
        self.assertEqual(search_by_full_name(), "\nName: David\nSurname: Johnson\nTelephone number: 5551234567\n"
                                                "City: Chicago\nState: IL")

    def test_full_name_user_4(self):
        self.assertEqual(search_by_full_name(), "\nName: Maxim\nSurname: Kostenko\nTelephone number: 0501413163\n"
                                                "City: Kherson\nState: KH")

    def test_full_name_user_5(self):
        self.assertEqual(search_by_full_name(), "\nName: Yura\nSurname: Perepelko\nTelephone number: 0500823183\n"
                                                "City: Kherson\nState: KH")


if __name__ == "__main__":
    unittest.main()
