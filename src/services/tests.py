import unittest

from django.test import TestCase
from django.test import Client

from services.models import Service


class TestService(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        Service.objects.create(name="File Protection", price=3.33,
                               os_platform="android")
        Service.objects.create(name="Isolate Download", price=15.00,
                               os_platform="windows")

    def test_view_service(self):
        uri = '/service/{id}/'
        # get the first service
        response = self.client.get(uri.format(id=1))
        content = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn("File Protection", content)
        # make sure second service not appear
        self.assertNotIn("Isolate Download", content)

        # get the second service
        response = self.client.get(uri.format(id=2))
        content = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Isolate Download", content)
        # make sure first service not appear
        self.assertNotIn("File Protection", content)

    def test_search_service(self):
        uri = '/service/?q={q}'
        # get the first service
        response = self.client.get(uri.format(q='ProtecT'))
        content = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn("File Protection", content)
        # make sure second service not appear
        self.assertNotIn("Isolate Download", content)

        # get the second service
        response = self.client.get(uri.format(q='isolATe'))
        content = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Isolate Download", content)
        # make sure first service not appear
        self.assertNotIn("File Protection", content)
