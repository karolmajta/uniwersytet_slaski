import unittest

from main import find_user_by_id


class UserUtilitiesTestCase(unittest.TestCase):
    def setUp(self):
        self.users = {
            43: 'Janis Joplin',
            60: 'Bruce Willis'
        }
    
    def test_find_user_by_id_when_user_found(self):
        self.assertEqual(find_user_by_id(self.users, 43), 'Janis Joplin') 
    
    
    def test_find_user_by_id_when_user_not_found(self):
        with self.assertRaises(KeyError):
            find_user_by_id(self.users, 500)