'''Performs basic unittest on core''' # pylint: disable=cyclic-import

#################
#### Imports ####
#################

from wagtail.tests.utils import WagtailPageTests
from django.test import TestCase, Client
from django.urls import reverse

class BasicTestCase(WagtailPageTests, TestCase):

    '''Includes unittest core functions'''

    # Executed prior to each test
    def setUp(self):
        self.client = Client()

    # Executed after each test
    def tearDown(self):
        pass

    ###############
    #### Tests ####
    ###############

    def test_index(self):

        '''Test index routes for homepage'''

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

        # if form.is_valid = true
        self.client.post(
            '/',
            data=dict(
                firstname='John',
                lastname='Doe',
                email='example@example.com',
                subject='Testing the contact form',
                message='This is a test message.'
            ), follow_redirects=True
        )

        # if form.is_valid = false
        return self.client.post(
            '/',
            data=dict(
                firstname='John',
                lastname='Doe',
                email='example@example.com',
                subject='Testing the contact form',
            ), follow_redirects=True
        )
