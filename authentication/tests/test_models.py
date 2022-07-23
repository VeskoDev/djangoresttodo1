from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):
    


    def test_cretes_user(self):
        user = User.objects.create_user('vesko', 'vesko@gmail.com', 'password123')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'vesko@gmail.com')

    
    # def test_cretes_super_user(self):
    #     user = User.objects.create_superuser('vesko', 'vesko@gmail.com', 'password123')
    #     self.assertIsInstance(user, User)
    #     self.assertTrue(user.is_staff)
    #     self.assertEqual(user.email, 'vesko@gmail.com')
    
    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username ='', email = 'vesko@gmail.com', password ='password123')
        self.assertRaises(ValueError, "The given username must be set")
    
    
    def test_raises_error_with_message_when_no_username_is_supplied(self):

        with self.assertRaisesMessage(ValueError, "The given username must be set"):
            User.objects.create_user(username ='', email = 'vesko@gmail.com', password = 'passord1234')
        # self.assertRaises(ValueError, User.objects.create_user, username ='', email = 'vesko@gmail.com', password ='password123')
        # self.assertRaises(ValueError, "The given username must be set")

        # user = User.objects.create_user()
        # self.assertIsInstance(user, User)
        # self.assertTrue(user.is_staff)
        # self.assertEqual(user.email, 'vesko@gmail.com')