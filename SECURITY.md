# Security Policy

## Supported Versions

Currently supported versions of Yardly:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously at Yardly. If you discover a security vulnerability, please follow these steps:

### 1. Do NOT Create a Public Issue

Please do not create a public GitHub issue for security vulnerabilities. This could put users at risk.

### 2. Report Privately

Send an email to: **security@yardly.platform** (or create a private security advisory on GitHub)

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### 3. Wait for Response

We will:
- Acknowledge receipt within 24 hours
- Provide an initial assessment within 72 hours
- Keep you updated on progress
- Credit you in the fix (unless you prefer to remain anonymous)

## Security Best Practices

### For Developers

1. **Dependencies**: Keep all dependencies up to date
   ```bash
   pip list --outdated
   pip install -U package_name
   ```

2. **Secrets**: Never commit secrets to the repository
   - Use environment variables
   - Add `.env` to `.gitignore`
   - Use `python-decouple` for configuration

3. **Input Validation**: Always validate and sanitize user input
   - Use Django's built-in form validation
   - Sanitize HTML with `bleach`
   - Validate file uploads

4. **Authentication**: Use Django's built-in authentication
   - Never store passwords in plain text
   - Use Django's password validation
   - Implement rate limiting for login attempts

5. **Authorization**: Check permissions properly
   - Use `@login_required` decorator
   - Check object-level permissions
   - Validate user has access to resources

### For Deployers

1. **Environment**:
   ```bash
   DEBUG = False  # NEVER set to True in production
   SECRET_KEY = 'random-50+-character-string'
   ALLOWED_HOSTS = ['yourdomain.com']
   ```

2. **HTTPS**: Always use HTTPS in production
   ```python
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

3. **Database**: Use strong credentials
   - Random password (20+ characters)
   - Limit database user permissions
   - Use connection encryption

4. **Firewall**: Configure proper firewall rules
   - Only expose necessary ports (80, 443)
   - Restrict SSH access
   - Use fail2ban for brute force protection

5. **Backups**: Regular automated backups
   - Database backups daily
   - Media files backups
   - Test restore procedures

6. **Monitoring**: Set up security monitoring
   - Log analysis
   - Intrusion detection
   - Uptime monitoring

## Security Features

### Built-in Protections

Yardly includes:

1. **CSRF Protection**: Enabled by default
2. **XSS Protection**: Template auto-escaping
3. **SQL Injection**: Django ORM prevents SQL injection
4. **Clickjacking**: X-Frame-Options middleware
5. **SSL/HTTPS**: Redirect middleware available

### Data Privacy

1. **User Data**: Minimal data collection
2. **Consent**: Explicit consent required
3. **Access Logging**: All data access is logged
4. **Right to Deletion**: Users can request data deletion
5. **Encryption**: Sensitive data encrypted at rest

### AI Security

1. **Transparency**: All AI decisions logged
2. **Bias Monitoring**: Regular audits
3. **Human Oversight**: Required for all decisions
4. **Explainability**: Clear explanations provided

## Known Security Considerations

### Django Admin

- Change the default `/admin/` URL
- Use strong admin passwords
- Enable two-factor authentication
- Limit admin access by IP (optional)

### File Uploads

- Validate file types
- Scan for malware
- Limit file sizes
- Store outside web root

### Rate Limiting

Consider implementing rate limiting for:
- Login attempts
- Password reset requests
- API endpoints
- File uploads

Example using `django-ratelimit`:
```python
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m')
def login_view(request):
    # Login logic
    pass
```

### Session Security

```python
SESSION_COOKIE_AGE = 3600  # 1 hour
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True  # HTTPS only
SESSION_COOKIE_SAMESITE = 'Strict'
```

## Compliance

Yardly is designed with compliance in mind:

- **GDPR**: Data privacy and user rights
- **CCPA**: California privacy requirements
- **EEOC**: Fair hiring practices
- **SOC 2**: Security controls (roadmap)

## Security Checklist

Before deploying to production:

- [ ] `DEBUG = False`
- [ ] Strong `SECRET_KEY` (random, 50+ chars)
- [ ] `ALLOWED_HOSTS` configured
- [ ] HTTPS enabled
- [ ] Database using strong password
- [ ] Static/media files properly configured
- [ ] Firewall rules in place
- [ ] Backups configured
- [ ] Monitoring enabled
- [ ] Security headers configured
- [ ] Dependencies up to date
- [ ] Admin URL changed (optional)
- [ ] Rate limiting implemented
- [ ] Log rotation configured
- [ ] Error reporting configured

## Security Updates

We will:
- Monitor dependencies for vulnerabilities
- Provide security updates promptly
- Announce security issues in release notes
- Maintain a security changelog

## Responsible Disclosure

We follow responsible disclosure practices:

1. **Private Disclosure**: Report vulnerabilities privately
2. **Fix Development**: We develop and test a fix
3. **Coordinated Release**: We coordinate release timing
4. **Public Disclosure**: We disclose after fix is available
5. **Credit**: We credit reporters (with permission)

## Contact

- **Security Issues**: security@yardly.platform
- **General Questions**: maintainers@yardly.platform
- **GitHub**: https://github.com/micdr93/yardly/security

## Hall of Fame

We recognize security researchers who help keep Yardly secure:

<!-- Researchers will be listed here -->

Thank you for helping keep Yardly and our users safe!

---

Last Updated: October 2025
Version: 1.0
