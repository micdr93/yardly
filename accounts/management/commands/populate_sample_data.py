"""
Management command to populate the database with sample data.
This demonstrates Yardly's candidate-first features.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from jobs.models import Company, JobPosting
from candidates.models import CandidateProfile, Application
from feedback.models import ApplicationFeedback, FeedbackTemplate
from community.models import CommunityPost, ResourceShare
from ai_ethics.models import EthicalAIGuideline, BiasAuditLog

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate database with sample data for demonstration'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating Yardly with sample data...\n')

        # Create users
        self.stdout.write('Creating users...')
        
        # Create candidate users
        candidate1 = User.objects.create_user(
            username='alice_candidate',
            email='alice@example.com',
            password='demo123',
            user_type='candidate',
            first_name='Alice',
            last_name='Johnson',
            bio='Passionate software engineer with 5 years of Python/Django experience.',
            location='San Francisco, CA'
        )
        
        candidate2 = User.objects.create_user(
            username='bob_candidate',
            email='bob@example.com',
            password='demo123',
            user_type='candidate',
            first_name='Bob',
            last_name='Smith',
            bio='Full-stack developer specializing in web applications.',
            location='New York, NY'
        )
        
        # Create recruiter user
        recruiter = User.objects.create_user(
            username='recruiter_jane',
            email='jane@techcorp.com',
            password='demo123',
            user_type='recruiter',
            first_name='Jane',
            last_name='Recruiter',
            bio='Technical recruiter at TechCorp Inc.',
            location='Austin, TX'
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created 3 users'))

        # Create companies
        self.stdout.write('Creating companies...')
        
        techcorp = Company.objects.create(
            name='TechCorp Inc.',
            description='Leading technology company building innovative solutions.',
            website='https://techcorp.example.com',
            industry='Technology',
            size='201-500',
            location='Austin, TX'
        )
        
        startup = Company.objects.create(
            name='StartupXYZ',
            description='Fast-growing startup revolutionizing the recruitment space.',
            website='https://startupxyz.example.com',
            industry='HR Tech',
            size='11-50',
            location='San Francisco, CA'
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created 2 companies'))

        # Create job postings
        self.stdout.write('Creating job postings...')
        
        job1 = JobPosting.objects.create(
            company=techcorp,
            recruiter=recruiter,
            title='Senior Django Developer',
            description='We are looking for an experienced Django developer to join our team.',
            responsibilities='- Build scalable web applications\n- Lead technical discussions\n- Mentor junior developers',
            requirements='- 5+ years Python experience\n- 3+ years Django experience\n- Strong database skills',
            preferred_qualifications='- Experience with REST APIs\n- Cloud deployment experience',
            location='Austin, TX',
            remote_type='hybrid',
            employment_type='full_time',
            salary_min=120000,
            salary_max=160000,
            salary_currency='USD',
            benefits='Health insurance, 401k, unlimited PTO, remote work flexibility',
            skills_required=['Python', 'Django', 'PostgreSQL', 'REST APIs'],
            skills_preferred=['Docker', 'AWS', 'React'],
            experience_min=5,
            experience_max=10,
            status='active',
            requires_cover_letter=True,
            custom_questions=[
                {'question': 'Tell us about your most challenging Django project.', 'required': True},
                {'question': 'What interests you about TechCorp?', 'required': True}
            ]
        )
        
        job2 = JobPosting.objects.create(
            company=startup,
            recruiter=recruiter,
            title='Full Stack Engineer',
            description='Join our mission to transform recruitment with technology.',
            responsibilities='- Develop new features\n- Collaborate with product team\n- Participate in code reviews',
            requirements='- 3+ years web development experience\n- JavaScript and Python proficiency',
            location='San Francisco, CA',
            remote_type='remote',
            employment_type='full_time',
            salary_min=100000,
            salary_max=140000,
            salary_currency='USD',
            benefits='Equity, health insurance, flexible hours, home office stipend',
            skills_required=['JavaScript', 'Python', 'React', 'Node.js'],
            skills_preferred=['TypeScript', 'GraphQL'],
            experience_min=3,
            status='active'
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created 2 job postings'))

        # Create candidate profiles
        self.stdout.write('Creating candidate profiles...')
        
        profile1 = CandidateProfile.objects.create(
            user=candidate1,
            years_of_experience=5,
            current_title='Software Engineer',
            current_company='Tech Solutions LLC',
            salary_expectation_min=130000,
            salary_expectation_max=150000,
            preferred_locations=['San Francisco, CA', 'Austin, TX', 'Remote'],
            remote_preference='hybrid',
            skills=['Python', 'Django', 'PostgreSQL', 'Redis', 'Docker', 'AWS'],
            languages=[
                {'language': 'English', 'proficiency': 'Native'},
                {'language': 'Spanish', 'proficiency': 'Intermediate'}
            ],
            education=[
                {'degree': 'BS Computer Science', 'school': 'UC Berkeley', 'year': 2019}
            ]
        )
        
        profile2 = CandidateProfile.objects.create(
            user=candidate2,
            years_of_experience=3,
            current_title='Web Developer',
            current_company='Digital Agency',
            salary_expectation_min=110000,
            salary_expectation_max=130000,
            remote_preference='remote',
            skills=['JavaScript', 'React', 'Node.js', 'Python', 'MongoDB'],
            languages=[
                {'language': 'English', 'proficiency': 'Native'}
            ],
            education=[
                {'degree': 'BS Software Engineering', 'school': 'MIT', 'year': 2021}
            ]
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created 2 candidate profiles'))

        # Create applications
        self.stdout.write('Creating applications...')
        
        app1 = Application.objects.create(
            candidate=candidate1,
            job=job1,
            status='interviewing',
            cover_letter='Dear Hiring Manager,\n\nI am excited to apply for the Senior Django Developer position...',
            ai_match_score=0.87,
            ai_match_explanation='Strong match: Candidate has 5 years Python experience and 4 years Django experience. Skills align well with requirements.'
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created 1 application'))

        # Create feedback (demonstrating forced personalization)
        self.stdout.write('Creating personalized feedback...')
        
        ApplicationFeedback.objects.create(
            application=app1,
            feedback_type='interview',
            provided_by=recruiter,
            strengths='Alice demonstrated excellent understanding of Django ORM and database optimization. Her experience with scaling web applications was impressive, particularly the work she described on handling 1M+ requests per day.',
            areas_for_improvement='While technical skills are strong, I would recommend focusing on leadership communication skills for the senior role. Consider preparing more examples of mentoring and team collaboration.',
            detailed_comments='Overall, Alice is a strong candidate. The interview went well, and she showed deep technical knowledge. Her answers to system design questions were thorough and well-reasoned. We particularly liked her approach to database optimization. Next steps: Schedule a final round with the engineering director.',
            rating=4,
            next_steps='We will schedule a final round interview with our engineering director within the next week.',
            is_visible_to_candidate=True
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created personalized feedback'))

        # Create feedback templates
        self.stdout.write('Creating feedback templates...')
        
        FeedbackTemplate.objects.create(
            name='Technical Interview Feedback',
            feedback_type='interview',
            strengths_template='[CUSTOMIZE: Specific technical strengths observed, with examples]',
            improvement_template='[CUSTOMIZE: Specific areas where candidate can improve, with actionable advice]',
            comments_template='[CUSTOMIZE: Overall assessment, key observations, and clear next steps]',
            created_by=recruiter,
            is_active=True
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created feedback template'))

        # Create community posts
        self.stdout.write('Creating community content...')
        
        CommunityPost.objects.create(
            author=candidate1,
            title='Tips for Django Interview Success',
            content='Just finished an interview and wanted to share what helped me prepare:\n\n1. Review Django ORM deeply\n2. Practice system design questions\n3. Be ready to discuss scalability\n\nHappy to answer questions!',
            post_type='advice',
            tags=['django', 'interviews', 'tips']
        )
        
        ResourceShare.objects.create(
            shared_by=candidate2,
            title='Django Best Practices Guide',
            description='Comprehensive guide to Django development best practices',
            resource_type='article',
            url='https://docs.djangoproject.com/en/stable/misc/design-philosophies/',
            tags=['django', 'best-practices', 'documentation'],
            upvotes=5
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created community content'))

        # Create ethical AI guidelines
        self.stdout.write('Creating ethical AI guidelines...')
        
        EthicalAIGuideline.objects.create(
            title='Transparency in Candidate Screening',
            description='All AI-based screening decisions must be transparent and explainable to candidates.',
            principle='Transparency',
            implementation_details='We log all AI decisions in AIDecisionLog with explanations. Candidates can see their match scores and understand the reasoning.',
            version='1.0',
            is_active=True
        )
        
        EthicalAIGuideline.objects.create(
            title='Bias Prevention in Matching',
            description='AI matching algorithms must not discriminate based on protected characteristics.',
            principle='Fairness',
            implementation_details='Regular bias audits are conducted. Protected characteristics are excluded from AI models. Demographic parity is monitored.',
            version='1.0',
            is_active=True
        )
        
        EthicalAIGuideline.objects.create(
            title='Human Review Requirement',
            description='AI recommendations must be reviewed by humans before making final decisions.',
            principle='Human Oversight',
            implementation_details='All AI decisions have human_reviewed flag. Reviewers are identified. Override capability with justification required.',
            version='1.0',
            is_active=True
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created 3 ethical AI guidelines'))

        # Create bias audit log
        BiasAuditLog.objects.create(
            audit_type='comprehensive',
            audit_date='2025-10-01',
            model_version='v1.0.0',
            sample_size=1000,
            findings='Initial bias audit shows no significant disparities across demographic groups. All metrics within acceptable ranges.',
            bias_detected=False,
            bias_severity='none',
            metrics={
                'gender_parity': 0.98,
                'geographic_parity': 0.95,
                'age_distribution': 'balanced',
                'false_positive_rate_variance': 0.02
            },
            audited_by=recruiter
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Created bias audit log'))

        self.stdout.write(self.style.SUCCESS('\n✓ Sample data population complete!'))
        self.stdout.write('\nYou can now:')
        self.stdout.write('  - Log in to admin: http://localhost:8000/admin/')
        self.stdout.write('  - Username: recruiter_jane / alice_candidate / bob_candidate')
        self.stdout.write('  - Password: demo123')
