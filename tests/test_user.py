import unittest
from app.models import User

class User_Test:
    def setUp(self):
        self.user_charity = User(username = 'charity',email ='charitynyanchera@gmail.com',password="123")

    def test_password_setter(self):
        self.assertTrue(self.user_charity.password is not None)

  

   
