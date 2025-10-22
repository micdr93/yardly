"""
Tests for the feedback app - forced personalization features.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from candidates.models import Application, CandidateProfile
from jobs.models import Company, JobPosting
from feedback.models import ApplicationFeedback

User = get_user_model()


class ForcedPersonalizationTests(TestCase):
    """Test forced personalization in feedback."""
    
    def setUp(self):
        """Set up test data."""
        # Create users
        self.candidate = User.objects.create_user(
            username='candidate',
            email='candidate@example.com',
            user_type='candidate'
        )
        self.recruiter = User.objects.create_user(
            username='recruiter',
            email='recruiter@example.com',
            user_type='recruiter'
        )
        
        # Create company and job
        self.company = Company.objects.create(
            name='Test Corp',
            description='Test company'
        )
        self.job = JobPosting.objects.create(
            company=self.company,
            recruiter=self.recruiter,
            title='Test Position',
            description='Test job description',
            responsibilities='Test responsibilities',
            requirements='Test requirements'
        )
        
        # Create application
        self.application = Application.objects.create(
            candidate=self.candidate,
            job=self.job,
            cover_letter='Test cover letter'
        )
    
    def test_feedback_requires_minimum_length(self):
        """Test that feedback enforces minimum character requirements."""
        # This should raise ValueError due to short feedback
        with self.assertRaises(ValueError):
            ApplicationFeedback.objects.create(
                application=self.application,
                feedback_type='screening',
                provided_by=self.recruiter,
                strengths='Too short',
                areas_for_improvement='Also too short',
                detailed_comments='Not detailed enough'
            )
    
    def test_valid_personalized_feedback(self):
        """Test that properly personalized feedback is accepted."""
        feedback = ApplicationFeedback.objects.create(
            application=self.application,
            feedback_type='interview',
            provided_by=self.recruiter,
            strengths='The candidate demonstrated excellent technical knowledge, particularly in Python and Django frameworks. Their experience with scaling web applications was very impressive.',
            areas_for_improvement='While technical skills are strong, I recommend focusing more on communication skills and team collaboration. Consider preparing examples of past teamwork experiences.',
            detailed_comments='Overall, this was a strong interview. The candidate showed deep understanding of the role requirements and provided thoughtful answers to all technical questions. Their passion for the field was evident throughout the conversation.',
            rating=4
        )
        self.assertEqual(feedback.application, self.application)
        self.assertTrue(feedback.is_visible_to_candidate)

