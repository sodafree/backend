"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import LiveServerTestCase
from selenium import webdriver
#from django.test import TestCase



class SimpleTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

    # def test_basic_addition(self):
    #     """
    #     Tests that 1 + 1 always equals 2.
    #     """
    #     self.assertEqual(1 + 1, 2)

	def test_can_see_the_admin_site(self):
		self.browser.get(self.live_server_url + '/admin/')

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)