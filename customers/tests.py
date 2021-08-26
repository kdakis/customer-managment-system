from django.test import TestCase
from django.urls import reverse

from customers.models import Customer, User


class CustomerFieldTest(TestCase):

    def setUp(self):
        self.customer = Customer(
            name='Kazım', surname='Akiş', ssn='12345678901',
            phone='5056255859', city='İzmir', district='Karabağlar'
            )

    def test_field_tc(self):
        field_label = self.customer._meta.get_field('ssn').verbose_name
        self.assertEqual(field_label, "ssn")

    def test_field_name(self):
        field_label = self.customer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_field_surname(self):
        field_label = self.customer._meta.get_field('surname').verbose_name
        self.assertEqual(field_label, "surname")

    def test_object_name(self):
        expected_object = f'{self.customer.name} {self.customer.surname}'
        self.assertEqual(str(self.customer), expected_object)


class LandingPageTest(TestCase):

    def test_landing_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_landing_page_url_name(self):
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing_page.html")


class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='testpassword', email='test@test.com')

    def test_login(self):
        self.client.login(username='test', password='testpassword')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response)


class CustomerCreatePageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='testpassword', email='test@test.com')
        self.client.login(username='test', password='testpassword')

    def test_customer_create_page_status_code(self):
        response = self.client.get(reverse('customers:customer-create'))
        self.assertEqual(response.status_code, 200)

    def test_customer_create_page_url_name(self):
        response = self.client.get(reverse('customers:customer-create'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('customers:customer-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "customers/customer_create.html")


class CustomerUpdatePageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='testpassword', email='test@test.com')
        self.client.login(username='test', password='testpassword')
        self.customer = Customer.objects.create(
            name='Kazım', surname='Akiş', ssn='12345678901',
            phone='5056255859', city='İzmir', district='Karabağlar'
            )

    def test_update_page_url_name(self):
        response = self.client.get(reverse('customers:customer-update', args=(self.customer.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('customers:customer-update', args=(self.customer.pk,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "customers/customer_update.html")
