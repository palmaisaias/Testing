import unittest
from app import app
from faker import Faker


class TestAPI(unittest.TestCase): #inherits test case fucntionality from unittest

    def setUp(self):
        self.app = app.test_client() #makes its own tiny server so that the test can run

    #these are the tests were creating

    def test_sum(self):
        payload = {'num1': 2, 'num2': 3}
        response = self.app.post('/sum', json=payload) #sending a mock post request to our apps testing client's/sum route with the payload
        data = response.get_json()
        self.assertEqual(data['result'],5)

    def test_random_sum(self):
        fake = Faker()
        num1 = fake.random_number(digits=3)
        num2 = fake.random_number(digits=3)
        payload = {'num1': num1, 'num2': num2}
        response = self.app.post('/sum', json=payload) #sending a mock post request to our apps testing client's/sum route with the payload
        data = response.get_json()
        self.assertEqual(data['result'], num1+num2)

if __name__ == '__main__':
    unittest.main()