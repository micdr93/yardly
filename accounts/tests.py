"""
Tests for the accounts app.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import UserPreferences

User = get_user_model()


class UserModelTests(TestCase):
    """Test custom user model."""
    
    def test_create_candidate_user(self):
        """Test creating a candidate user."""
        user = User.objects.create_user(
            username='testcandidate',
            email='candidate@example.com',
            password='testpass123',
            user_type='candidate'
        )
        self.assertEqual(user.username, 'testcandidate')
        self.assertEqual(user.email, 'candidate@example.com')
        self.assertEqual(user.user_type, 'candidate')
        self.assertTrue(user.check_password('testpass123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
    
    def test_create_recruiter_user(self):
        """Test creating a recruiter user."""
        user = User.objects.create_user(
            username='testrecruiter',
            email='recruiter@example.com',
            password='testpass123',
            user_type='recruiter'
        )
        self.assertEqual(user.user_type, 'recruiter')
    
    def test_user_str_representation(self):
        """Test string representation of user."""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            user_type='candidate'
        )
        self.assertEqual(str(user), 'testuser (Candidate)')


class UserPreferencesTests(TestCase):
    """Test user preferences model."""
    
    def setUp(self):
        """Create a test user."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            user_type='candidate'
        )
    
    def test_create_preferences(self):
        """Test creating user preferences."""
        prefs = UserPreferences.objects.create(
            user=self.user,
            receive_email_notifications=True,
            real_time_feedback_enabled=True,
            community_visibility=True
        )
        self.assertEqual(prefs.user, self.user)
        self.assertTrue(prefs.receive_email_notifications)
        self.assertTrue(prefs.real_time_feedback_enabled)
    
    def test_preferences_str_representation(self):
        """Test string representation of preferences."""
        prefs = UserPreferences.objects.create(user=self.user)
        self.assertEqual(str(prefs), f'Preferences for {self.user.username}')

