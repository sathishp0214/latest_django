from django.test import TestCase
# Create your tests here.
from django.urls import reverse

class test_app(TestCase):
    def test_login(self):
        login = self.client.login(username='sathish', password='Comodo@123')
        response = self.client.get(reverse('home'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'sathish')
        # Check that we got a http 200 response
        self.assertEqual(response.status_code, 200)
        print ('hhhh')
        # Check we used correct template
        self.assertTemplateUsed(response, 'home.html')
        print('PPPPP')