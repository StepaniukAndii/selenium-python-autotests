import unittest

import requests


class TestApi(unittest.TestCase):

    def test_api_post_positive(self):
        response = requests.post("https://reqres.in/api/users",
                                 data={
                                     "name": "morpheus",
                                     "job": "leader"
                                 })
        assert response.status_code == 201

    def test_api_get_positive(self):
        response = requests.get("https://reqres.in/api/users?page=2")
        response_body = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body['page'], 2)

    def test_api_get_positive_id(self):
        response = requests.get("https://reqres.in/api/users/2")
        response_body = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body['data']['id'], 2)

    def test_api_get_negative(self):
        response = requests.get("https://reqres.in/api/users/23")

        self.assertEqual(response.status_code, 404)

    def test_api_get_negative_unknown(self):
        response = requests.get("https://reqres.in/api/users/unknown/23")

        self.assertEqual(response.status_code, 404)

    def test_api_delete_positive(self):
        response = requests.get("https://reqres.in/api/users/2")

        self.assertEqual(response.status_code, 200)

    def test_api_post_registration(self):
        response = requests.post('https://reqres.in/api/register',
                                 data={
                                     "email": "eve.holt@reqres.in",
                                     "password": "pistol"
                                 })
        response_body = response.json()

        self.assertEqual(response_body['token'], 'QpwL5tke4Pnpja7X4')

    def test_api_post_registration_fail(self):
        response = requests.post('https://reqres.in/api/register',
                                 data={
                                     "email": "eve.holt@reqres.in",
                                 })
        response_body = response.json()

        self.assertEqual(response_body['error'], 'Missing password')

    def test_api_post_login(self):
        response = requests.post('https://reqres.in/api/login',
                                 data={
                                     "email": "eve.holt@reqres.in",
                                     "password": "cityslicka"
                                 })
        response_body = response.json()

        self.assertEqual(response_body['token'], 'QpwL5tke4Pnpja7X4')

    def test_api_post_login_fail(self):
        response = requests.post('https://reqres.in/api/login',
                                 data={
                                     "email": "eve.holt@reqres.in",
                                 })
        response_body = response.json()

        self.assertEqual(response_body['error'], 'Missing password')