from django.shortcuts import make_toast
from django.test import SimpleCaseTest

class MakeToastTests(SimpleCaseTest):
    def test_make_toast(self):
        self.assertEqual(make_toast(), 'toast')
