from django.test import TestCase

# Test all main website pages load


class WebPagesTestCase(TestCase):

    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_aboutpage(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_pricespage(self):
        response = self.client.get('/prices/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "prices.html")
        self.assertTemplateUsed(response, "base.html")

    def test_successpage(self):
        response = self.client.get('/successful_submission/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "successful_submission.html")
        self.assertTemplateUsed(response, "base.html")

    def test_contactpage(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "/contact.html")
        self.assertTemplateUsed(response, "base.html")

    def test_bookingpage(self):
        response = self.client.get('/booking_form/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "booking_form.html")
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
