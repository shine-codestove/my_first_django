import json
from django.test import TestCase

# Create your tests here.
import unittest
from django.test import Client

from myapp.models.person import Person


class TestPersonMethods(unittest.TestCase):
    client = Client()

    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_person_view_get(self):
        response = self.client.get("/myapp/person/")
        print(response.json())
        self.assertTrue(len(response.json()) > 0)

    def test_person_view_post(self):
        data = {"first_name": "aaa", "last_name": "bbb", "age": "10", "sex": "female"}
        response = self.client.post(
            "/myapp/person/",
            data,
            "application/json",
        )
        print(response.json())
        self.assertTrue(response.status_code == 200)

    def test_person_model(self):
        person_list = Person.objects.all()
        self.assertIsNotNone(person_list)
