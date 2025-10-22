# Quick Start Guide for Yardly

Get up and running with Yardly in under 10 minutes!

## Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git

## Step 1: Clone the Repository

```bash
git clone https://github.com/micdr93/yardly.git
cd yardly
```

## Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run Migrations

```bash
python manage.py migrate
```

## Step 5: Load Sample Data (Optional but Recommended)

```bash
python manage.py populate_sample_data
```

This creates:
- 3 demo users (2 candidates, 1 recruiter)
- 2 companies
- 2 job postings
- Candidate profiles
- Sample applications with personalized feedback
- Community posts and resources
- Ethical AI guidelines

**Demo Credentials:**
- Username: `recruiter_jane` | Password: `demo123` (Recruiter)
- Username: `alice_candidate` | Password: `demo123` (Candidate)
- Username: `bob_candidate` | Password: `demo123` (Candidate)

## Step 6: Create Your Admin User (If not using sample data)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

## Step 7: Start the Development Server

```bash
python manage.py runserver
```

## Step 8: Access Yardly

Open your browser and navigate to:

- **Admin Panel**: http://localhost:8000/admin/
- **Main Application**: http://localhost:8000/

Log in with your credentials!

## What to Explore

### As a Recruiter (recruiter_jane)

1. **Companies**: Manage company profiles
2. **Job Postings**: Create jobs with transparent salary ranges
3. **Applications**: Review candidate applications
4. **Feedback**: Provide personalized feedback (required!)
5. **AI Decisions**: View AI transparency logs

### As a Candidate (alice_candidate or bob_candidate)

1. **Profile**: Complete your candidate profile
2. **Jobs**: Browse job postings with full transparency
3. **Applications**: Track your applications
4. **Feedback**: View detailed, personalized feedback
5. **Community**: Share experiences and learn from others

### Key Features to Check Out

#### 🎯 Candidate-First Features
- Browse Jobs → Notice salary ranges are visible
- View Applications → See transparent status tracking
- Check Feedback → All feedback is detailed and personalized

#### 💬 Forced Personalization
- Try creating feedback → System enforces minimum character counts
- Generic feedback is rejected
- Templates require customization

#### 🤝 Community
- Community Posts → Share interview experiences
- Resource Sharing → Learn from peer recommendations
- Mentorship → Connect with others in your field

#### 🤖 Ethical AI
- AI Decision Logs → Complete transparency
- Bias Audits → Regular fairness monitoring
- Human Oversight → All AI decisions reviewed

## Understanding the Models

### User Types
- **Candidate**: Job seekers
- **Recruiter**: Hiring managers
- **Admin**: Platform administrators

### Application Statuses
1. Draft
2. Submitted
3. Under Review
4. Screening
5. Interviewing
6. Offer Extended
7. Offer Accepted
8. Rejected
9. Withdrawn

### Feedback Types
1. Screening Feedback
2. Interview Feedback
3. Technical Assessment Feedback
4. Final Decision Feedback

## Next Steps

### Customize Your Instance

1. **Update Settings**: Edit `yardly_platform/settings.py`
   - Change SECRET_KEY
   - Configure email settings
   - Set up database (PostgreSQL recommended)

2. **Add Your Branding**: 
   - Upload company logos
   - Customize templates (future work)
   - Configure domain settings

3. **Configure Notifications**:
   - Set up email backend
   - Configure SMS (optional)
   - Enable real-time updates

### Development Workflow

1. Make changes to code
2. Run tests: `python manage.py test`
3. Check for issues: `python manage.py check`
4. Run migrations if models changed: `python manage.py makemigrations && python manage.py migrate`

### Common Commands

```bash
# Create new app
python manage.py startapp app_name

# Run specific tests
python manage.py test app_name.tests.TestClassName

# Shell access
python manage.py shell

# Check deployment readiness
python manage.py check --deploy

# Collect static files (for production)
python manage.py collectstatic
```

## Troubleshooting

### "No module named 'PIL'"
```bash
pip install Pillow
```

### Port 8000 already in use
```bash
# Use a different port
python manage.py runserver 8080
```

### Database errors
```bash
# Delete and recreate database
rm db.sqlite3
python manage.py migrate
python manage.py populate_sample_data
```

### Import errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall dependencies
pip install -r requirements.txt
```

## Getting Help

- **Documentation**: Check README.md and other .md files
- **Code Examples**: Look at populated sample data
- **Tests**: Review test files for usage examples
- **Issues**: https://github.com/micdr93/yardly/issues

## Contributing

Want to contribute? Check out CONTRIBUTING.md for guidelines!

## What's Next?

Explore the codebase:
- `accounts/models.py` - User and profile models
- `candidates/models.py` - Candidate and application models
- `jobs/models.py` - Job posting models
- `feedback/models.py` - Feedback system (forced personalization!)
- `community/models.py` - Community features
- `ai_ethics/models.py` - Ethical AI framework

Read the guides:
- `README.md` - Complete overview
- `ETHICAL_AI.md` - AI ethics principles
- `CONTRIBUTING.md` - How to contribute
- `DEPLOYMENT.md` - Production deployment

---

**Welcome to Yardly - where candidates come first!** 🎉
