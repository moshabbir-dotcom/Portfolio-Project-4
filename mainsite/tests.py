from django.test import TestCase

# Test all main website pages load


class WebPagesTestCase(TestCase):

    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mainsite/home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_aboutpage(self):
        response = self.client.get('/about.html/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                "mainsite/about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_pricespage(self):
        response = self.client.get('/prices.html/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mainsite/prices.html")
        self.assertTemplateUsed(response, "base.html")

    def test_successpage(self):
        response = self.client.get('/successful_submission.html/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                "mainsite/successful_submission.html")
        self.assertTemplateUsed(response, "base.html")

    def test_contactpage(self):
        response = self.client.get('/contact.html/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mainsite/contact.html")
        self.assertTemplateUsed(response, "base.html")

    def test_bookingpage(self):
        response = self.client.get('/booking_form.html/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mainsite/booking_form.html")
        self.assertTemplateUsed(response, "base.html")


# Test loading of login and signup pages and redirects
class UserTests(TestCase):

    def test_signup_page_load(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_load(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout_page_load(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)
