import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(password = 'Samfan01')
        
    def test_password(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    