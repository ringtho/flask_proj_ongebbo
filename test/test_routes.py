import unittest
from api.routes import app
import json

class TestRedFlags(unittest.TestCase):

    def setUp(self):
        """initialise test client"""
        self.test_client = app.test_client()

    # def test_users_inputs(self):
    #     input_users = {"firstname": "Smith", "lastname": "Ringtho",
    #     "othernames":"J", "email": "sringtho@gmail.com", "phoneNumber": "778339655",
    #     "username":"sringtho"}
    #     self.test_client.post("/api/v101/users", json=input_users)
    #
    #     response = self.test_client.get("/api/v101/users")
    #     print(response)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(len(data["users_list"]), 1)

    def test_all_products_when_empty(self):
        response = self.test_client.get("/api/v101/users")
        print(response)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("no users", data["message"])



if __name__ == '__main__':
    unittest.main()
