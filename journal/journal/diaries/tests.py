from django.http.response import HttpResponseNotAllowed
from django.test.client import Client
from django.utils import unittest
import ujson as json


class CreateDiaryTest(unittest.TestCase):

    def test_01_create_diary(self):
        self.c = Client()
        response = self.c.get('/diaries/diary/')
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 100)
        response = self.c.post('/diaries/diary/')
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 100)

        # Create and login a writer
        response = self.c.post('/accounts/writer/',{'username':'prateeks','password':'psehgal','email':'prateek.sehgal2@gmail.com','phone':'9980311998', 'role':'["entrepreneur", "poet"]'})
        response = self.c.post('/accounts/session/',{'username':'prateeks','password':'psehgal'})
        resp = json.loads(response.content)
        sess_key = resp['data']['jour_session_key']

        response = self.c.post('/diaries/diary/',{})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 0)

        response = self.c.post('/diaries/diary/',{'title':'Today was a good day','content':'I actually went ahead and coded some', 'place':'Bangalore'})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 0)

        # Logout the writer
        response = self.c.delete('/accounts/session/{0}/'.format(sess_key))

        response = self.c.post('/diaries/diary/',{})
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 100)

    def test_02_get_diary(self):
        self.c = Client()
        response = self.c.get('/diaries/')
        resp = json.loads(response.content)
        self.assertEqual(resp['status'], 100)

        response = self.c.post('/accounts/session/',{'username':'prateeks','password':'psehgal'})
        resp = json.loads(response.content)
        sess_key = resp['data']['jour_session_key']

        response = self.c.get('/diaries/')
        resp = json.loads(response.content)
        diary_ids = resp['data']
        for id in diary_ids:
            response = self.c.get('/diaries/diary/{0}/'.format(id))
            resp = json.loads(response.content)
            print resp

