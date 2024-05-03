from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import CustomUser  # Assuming CustomUser is the model for Alumni

class DeleteAlumniTestCase(TestCase):
    def setUp(self):
        # Create a test alumni
        self.alumni = CustomUser.objects.create(username='test_alumni', email='test@example.com', password='password123')
        self.alumni_id = self.alumni.id

    def test_delete_alumni(self):
        # Make a POST request to the DELETE_ALUMNI view
        response = self.client.post(reverse('DELETE_ALUMNI', kwargs={'admin': self.alumni_id}))

        # Check if the alumni is deleted
        self.assertFalse(CustomUser.objects.filter(id=self.alumni_id).exists())

        # Check if the response is a redirect
        self.assertRedirects(response, reverse('view_alumni'))

        # Check if success message is displayed
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn("Record Are Succesfully Deleted!", messages)

    def tearDown(self):
        # Clean up after the test
        CustomUser.objects.filter(id=self.alumni_id).delete()
 