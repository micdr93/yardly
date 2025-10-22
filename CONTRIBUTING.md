# Contributing to Yardly

Thank you for your interest in contributing to Yardly! We're building a candidate-first recruitment platform, and we welcome contributions from everyone.

## Code of Conduct

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone, regardless of:
- Age, body size, disability, ethnicity
- Gender identity and expression
- Level of experience, education
- Nationality, personal appearance, race, religion
- Sexual identity and orientation

### Our Standards

**Positive behaviors**:
- Using welcoming and inclusive language
- Respecting differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy towards others

**Unacceptable behaviors**:
- Harassment, trolling, or discriminatory comments
- Personal or political attacks
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## How to Contribute

### Reporting Bugs

Before creating a bug report:
1. Check existing issues to avoid duplicates
2. Verify the bug in the latest version
3. Collect relevant information

Bug reports should include:
- **Clear title**: Descriptive summary
- **Steps to reproduce**: Numbered list
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Screenshots**: If applicable
- **Environment**: OS, Python version, Django version
- **Additional context**: Any other relevant details

### Suggesting Features

Feature suggestions are welcome! Please:
1. Check if it aligns with Yardly's candidate-first mission
2. Search existing feature requests
3. Provide clear use cases
4. Describe expected benefits
5. Consider implementation complexity

### Pull Requests

#### Before Starting

1. **Discuss major changes** in an issue first
2. **Check existing PRs** to avoid duplicates
3. **Review the roadmap** to align with project direction

#### Development Process

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/yardly.git
   cd yardly
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

3. **Set up development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   ```

4. **Make your changes**
   - Write clean, readable code
   - Follow Django best practices
   - Add comments for complex logic
   - Update documentation

5. **Test your changes**
   ```bash
   python manage.py test
   python manage.py check
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

   Commit message format:
   ```
   Type: Brief description (50 chars or less)

   More detailed explanation if needed. Wrap at 72 characters.
   Explain the problem and how your change fixes it.

   - Bullet points are okay
   - Include issue references: Fixes #123
   ```

   Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Use a clear, descriptive title
   - Reference related issues
   - Describe your changes in detail
   - Include screenshots for UI changes
   - List any breaking changes

#### PR Requirements

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts
- [ ] PR description is complete

### Code Style

#### Python/Django

Follow PEP 8 and Django coding style:

```python
# Good
def get_candidate_profile(user_id):
    """
    Retrieve candidate profile for given user.
    
    Args:
        user_id: User ID to look up
        
    Returns:
        CandidateProfile instance or None
    """
    try:
        return CandidateProfile.objects.get(user_id=user_id)
    except CandidateProfile.DoesNotExist:
        return None

# Bad - missing docstring, poor variable names
def gcp(u):
    try:
        return CandidateProfile.objects.get(user_id=u)
    except:
        return None
```

#### Model Design

```python
class YourModel(models.Model):
    """Clear description of model purpose."""
    
    # Fields with help_text
    field_name = models.CharField(
        max_length=100,
        help_text=_('Description of field')
    )
    
    class Meta:
        verbose_name = _('Your Model')
        verbose_name_plural = _('Your Models')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Meaningful representation"
```

#### Comments

```python
# Good - explains WHY
# Calculate match score using weighted factors to ensure
# salary expectations don't dominate the recommendation
score = calculate_weighted_match(factors, weights)

# Bad - explains WHAT (code already shows this)
# Set score to result of calculate_weighted_match
score = calculate_weighted_match(factors, weights)
```

## Specific Contribution Areas

### Candidate-First Features

When contributing candidate-focused features:
- Prioritize transparency and clarity
- Respect candidate time and privacy
- Provide actionable information
- Avoid dark patterns

### Ethical AI

AI-related contributions must:
- Include transparency logging
- Document bias considerations
- Provide explainable outputs
- Enable human oversight

Example:
```python
def ai_screening_decision(application):
    """Screen application with AI."""
    # Calculate score
    score = model.predict(application.features)
    
    # Log decision (REQUIRED)
    AIDecisionLog.objects.create(
        application=application,
        decision_type='screening',
        model_version=settings.AI_MODEL_VERSION,
        confidence_score=score,
        explanation=generate_explanation(application, score),
        features_used=application.features.keys()
    )
    
    # Human review required
    return {
        'score': score,
        'requires_review': True,
        'explanation': generate_explanation(application, score)
    }
```

### Feedback System

Feedback features must enforce personalization:

```python
def validate_feedback(feedback_data):
    """Ensure feedback meets personalization requirements."""
    min_lengths = {
        'strengths': 50,
        'areas_for_improvement': 50,
        'detailed_comments': 100
    }
    
    for field, min_length in min_lengths.items():
        if len(feedback_data.get(field, '')) < min_length:
            raise ValidationError(
                f"{field} must be at least {min_length} characters"
            )
```

### Community Features

Community contributions should:
- Support anonymous participation when needed
- Encourage constructive interactions
- Facilitate peer learning
- Respect privacy

## Testing

### Writing Tests

```python
from django.test import TestCase
from accounts.models import User

class CandidateProfileTestCase(TestCase):
    """Test candidate profile functionality."""
    
    def setUp(self):
        """Create test user and profile."""
        self.user = User.objects.create_user(
            username='testcandidate',
            email='test@example.com',
            user_type='candidate'
        )
    
    def test_profile_creation(self):
        """Test that profile is created correctly."""
        profile = CandidateProfile.objects.create(
            user=self.user,
            years_of_experience=5
        )
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.years_of_experience, 5)
```

### Running Tests

```bash
# All tests
python manage.py test

# Specific app
python manage.py test candidates

# Specific test
python manage.py test candidates.tests.CandidateProfileTestCase.test_profile_creation

# With coverage
coverage run --source='.' manage.py test
coverage report
```

## Documentation

### Docstrings

Use Google-style docstrings:

```python
def calculate_match_score(candidate, job):
    """
    Calculate how well a candidate matches a job posting.
    
    Args:
        candidate (CandidateProfile): Candidate to evaluate
        job (JobPosting): Job posting to match against
        
    Returns:
        float: Match score between 0 and 1
        
    Raises:
        ValueError: If candidate or job is None
        
    Example:
        >>> score = calculate_match_score(candidate, job)
        >>> print(f"Match: {score * 100}%")
    """
```

### README Updates

Update README.md when adding:
- New features
- Configuration options
- Installation steps
- New dependencies

## Review Process

### What Reviewers Look For

1. **Functionality**: Does it work as intended?
2. **Code Quality**: Is it clean and maintainable?
3. **Tests**: Are there adequate tests?
4. **Documentation**: Is it well documented?
5. **Alignment**: Does it fit Yardly's mission?
6. **Ethics**: Does it respect candidate rights?

### Review Timeline

- **Initial review**: Within 3 days
- **Follow-up**: Within 2 days of updates
- **Merge decision**: Within 1 week of approval

### Addressing Feedback

- Be open to suggestions
- Ask questions if unclear
- Make requested changes promptly
- Mark conversations as resolved when addressed

## Getting Help

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **Discussions**: General questions and ideas
- **Email**: maintainers@yardly.platform

### Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Git Best Practices](https://git-scm.com/book/en/v2)

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Celebrated in community updates

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Don't hesitate to ask! We're here to help:
- Open an issue with the `question` label
- Start a discussion
- Reach out to maintainers

Thank you for making Yardly better! 🙌
