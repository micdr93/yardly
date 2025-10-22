# Yardly

**Candidate-first recruitment and ATS platform with real-time feedback, forced personalization, and a community-first approach.**

## Overview

Yardly is a Django-based recruitment and Applicant Tracking System (ATS) that puts candidates first. Unlike traditional ATS platforms that prioritize employers, Yardly is built on principles of transparency, personalization, and community support.

## Key Features

### 🎯 Candidate-First Approach
- **Transparent Application Process**: Candidates always know where they stand
- **Equal Information Access**: Job postings include salary ranges and complete details
- **Respect for Time**: Guaranteed response times and clear communication
- **Profile Ownership**: Candidates control their data and privacy settings

### 💬 Real-Time Feedback
- **Instant Notifications**: Get updates as soon as decisions are made
- **Detailed Feedback**: Every decision comes with actionable, personalized feedback
- **Two-Way Communication**: Candidates can respond to feedback and ask questions
- **Learning Opportunities**: Feedback designed to help candidates grow

### ✨ Forced Personalization
- **No Generic Rejections**: All feedback must be detailed and specific (minimum character requirements)
- **Custom Cover Letters**: Applications require personalized responses
- **Meaningful Interactions**: Templates are starting points, not final messages
- **Quality Over Quantity**: Encourages thoughtful, human connections

### 🤝 Community-First Features
- **Peer Mentorship**: Connect with others in your field
- **Experience Sharing**: Learn from others' interview experiences
- **Resource Library**: Community-curated learning materials
- **Anonymous Support**: Share and seek advice anonymously when needed

### 🤖 Ethical AI
- **Transparency**: All AI decisions are logged and explainable
- **Bias Monitoring**: Regular audits for fairness across demographics
- **Human Oversight**: AI recommendations require human review
- **Privacy Protection**: Comprehensive data access logging
- **Explainable Decisions**: Clear explanations of how AI makes recommendations

## Technology Stack

- **Framework**: Django 5.0+
- **Language**: Python 3.12+
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Features**: REST API ready, Real-time notifications ready, Community features

## Project Structure

```
yardly/
├── accounts/           # User authentication and profiles
├── candidates/         # Candidate profiles and applications
├── jobs/              # Job postings and company profiles
├── feedback/          # Real-time feedback system
├── community/         # Community forums and mentorship
├── ai_ethics/         # AI transparency and bias monitoring
└── yardly_platform/   # Main Django project settings
```

## Models Overview

### Accounts App
- **User**: Custom user model supporting candidates, recruiters, and admins
- **UserPreferences**: Personalization and notification preferences

### Candidates App
- **CandidateProfile**: Comprehensive candidate information
- **Application**: Job applications with transparent status tracking

### Jobs App
- **Company**: Company profiles for recruiters
- **JobPosting**: Job listings with mandatory transparency (salary ranges, etc.)

### Feedback App
- **ApplicationFeedback**: Forced personalized feedback (minimum character requirements)
- **FeedbackResponse**: Two-way communication between candidates and recruiters
- **FeedbackTemplate**: Starting templates that must be customized

### Community App
- **CommunityPost**: Forum discussions and experience sharing
- **CommunityComment**: Community engagement
- **MentorshipRequest**: Peer-to-peer mentorship connections
- **ResourceShare**: Community learning resources

### AI Ethics App
- **AIDecisionLog**: Complete transparency of AI decisions
- **BiasAuditLog**: Regular bias monitoring and audits
- **EthicalAIGuideline**: Documented AI ethics principles
- **DataPrivacyLog**: Comprehensive data access logging

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/micdr93/yardly.git
   cd yardly
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

## Configuration

Key settings in `yardly_platform/settings.py`:

```python
# Candidate-first features
CANDIDATE_RESPONSE_TIME_SLA = 24  # hours
REQUIRE_PERSONALIZED_FEEDBACK = True
ENABLE_REAL_TIME_FEEDBACK = True
ANONYMOUS_FEEDBACK_ENABLED = True

# Community features
ENABLE_COMMUNITY_FORUMS = True
ENABLE_PEER_REVIEWS = True
ENABLE_CANDIDATE_NETWORKING = True

# Ethical AI settings
AI_TRANSPARENCY_REQUIRED = True
AI_BIAS_MONITORING = True
HUMAN_REVIEW_REQUIRED = True
EXPLAINABLE_AI_ENABLED = True
```

## Core Principles

1. **Transparency First**: Candidates deserve to know everything about the process
2. **Respect for Time**: Fast responses and clear communication
3. **Human Touch**: Technology enhances, not replaces, human interaction
4. **Fair Treatment**: Equal opportunity and bias monitoring
5. **Community Support**: Candidates helping candidates succeed
6. **Continuous Learning**: Feedback that helps people grow
7. **Privacy Protection**: Candidates control their own data

## Development Roadmap

- [x] Core Django project structure
- [x] User authentication and profiles
- [x] Candidate profiles and applications
- [x] Job posting system
- [x] Real-time feedback system
- [x] Community features
- [x] Ethical AI framework
- [ ] REST API implementation
- [ ] Real-time notifications (WebSockets)
- [ ] Email integration
- [ ] SMS notifications
- [ ] File upload and resume parsing
- [ ] Advanced search and filtering
- [ ] Analytics dashboard
- [ ] Mobile responsiveness
- [ ] Internationalization

## Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Tags

`django` `recruitment` `human-first` `ats` `career-tech` `yardly` `ethical-ai` `community`

## Contact

- **Repository**: https://github.com/micdr93/yardly
- **Issues**: https://github.com/micdr93/yardly/issues

---

Built with ❤️ for candidates by candidates
