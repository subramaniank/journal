from django.http.response import HttpResponseNotAllowed
from django.test.client import Client
from django.utils import unittest
import ujson as json

# Create your tests here.

REQUIRED_ERROR = u'This field is required.'
USERNAME_NOT_AVAILABLE = u'Username not available'
INVALID_USERNAME = u'Invalid username'
INVALID_PASSWORD = u'Invalid password'


class Test_01_AccountsUser(unittest.TestCase):

    def test_01_user_creation(self):
        # Create user without password
        self.c = Client()
        response = self.c.get('/accounts/writer/')
        self.assertEqual(response.status_code, HttpResponseNotAllowed.status_code)
        response = self.c.post('/accounts/writer/', {'username':'vivekb'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 2)
        self.assertIn(REQUIRED_ERROR,resp['data']['password'])
        #Create user without username
        response = self.c.post('/accounts/writer/', {'password':'vivekb'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 2)
        self.assertIn(REQUIRED_ERROR,resp['data']['username'])

        # Create user without username and password
        response = self.c.post('/accounts/writer/',{'username':'vivekb','password':'vbhutani'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 0)
        self.assertEqual(resp['data']['username'],'vivekb')

        # Create duplicate user
        response = self.c.post('/accounts/writer/',{'username':'vivekb','password':'vbhutani','email':'vivek.bhutani@yahoo.com','phone':'9591418090'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 2)
        self.assertEqual(resp['data']['username'],[USERNAME_NOT_AVAILABLE])

        # Create user with email, phone, first and last name
        response = self.c.post('/accounts/writer/',{'username':'prateeks','password':'psehgal','email':'prateek.sehgal2@gmail.com','phone':'9980311998', 'role':'["entrepreneur", "poet"]'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 0)
        self.assertEqual(resp['data']['username'],'prateeks')
        self.assertEqual(resp['data']['email'],'prateek.sehgal2@gmail.com')
        self.assertEqual(resp['data']['phone'],'9980311998')

class Test_02_AccountsSession(unittest.TestCase):

    def test_01_login_user(self):
        self.c = Client()
        # Create a user first
        response = self.c.post('/accounts/writer/',{'username':'prateeks','password':'psehgal','email':'prateek.sehgal2@gmail.com','phone':'9980311998'})
        # Login without username/password and GET method
        response = self.c.get('/accounts/session/')
        self.assertEqual(response.status_code, HttpResponseNotAllowed.status_code)

        # Login without password
        response = self.c.post('/accounts/session/',{'username':'prateeks'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 2)
        self.assertEqual(resp['data']['password'],[REQUIRED_ERROR])

        # Login with wrong username
        response = self.c.post('/accounts/session/',{'username':'prateeksahab'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 2)
        self.assertEqual(resp['data']['username'],[INVALID_USERNAME])
        self.assertEqual(resp['data']['password'],[REQUIRED_ERROR])

        #Login with wrong password
        response = self.c.post('/accounts/session/',{'username':'prateeks','password':'psehgal1'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 2)
        self.assertEqual(resp['data']['password'],[INVALID_PASSWORD])

        # Login correctly with username and password
        response = self.c.post('/accounts/session/',{'username':'prateeks','password':'psehgal'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 0)
        self.assertEqual(resp['data']['username'],'prateeks')
        self.assertIsNotNone(resp['data']['jour_session_key'])
        sess_key = resp['data']['jour_session_key']


        # Logout a logged in client
        response = self.c.delete('/accounts/session/{0}/'.format(sess_key))
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 0)

        # Logout an already logged out client.
        response = self.c.delete('/accounts/session/{0}/'.format(sess_key))
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 101)
