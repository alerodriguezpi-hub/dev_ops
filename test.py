import unittest
import json
from main import app

class FlaskApiTestCase(unittest,TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_suma(self):
        response = self.app.get('/suma?a=2&b=3')
        data = json.load(response.data)
        self.asserEqual(data['resultado',5])

    def test_multiplica(self):
        response = self.app.post('/multiplicar',json={'a':4,'b':5})
        self.asserEqual(data['resultado'],20)

if __name__ == '__main_':
    unittest.main()

