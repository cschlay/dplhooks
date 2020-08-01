from unittest import TestCase

from django.test import SimpleTestCase, Client

from dplhooks import settings


class APITestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client(
            AUTHORIZATION=settings.API_BEARER
        )
