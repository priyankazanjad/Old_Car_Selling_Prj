from django.contrib.auth import logout,authenticate,login,get_user_model
from django.test import TestCase

class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='mike@example.org', password='mikeymike123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='mike@example.org', password='mikeymike123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
