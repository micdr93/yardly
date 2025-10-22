# Deployment Guide for Yardly

This guide covers deploying Yardly to production environments.

## Prerequisites

- Python 3.12+
- PostgreSQL 14+ (recommended for production)
- Redis (for caching and real-time features)
- Web server (Nginx recommended)
- WSGI server (Gunicorn recommended)

## Environment Variables

Create a `.env` file with the following variables:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/yardly

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Redis (for caching and Channels)
REDIS_URL=redis://localhost:6379/0

# File Storage (for production)
USE_S3=True
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
AWS_STORAGE_BUCKET_NAME=yardly-media
AWS_S3_REGION_NAME=us-east-1

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## PostgreSQL Setup

1. Install PostgreSQL:
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install postgresql postgresql-contrib
   
   # macOS
   brew install postgresql
   ```

2. Create database and user:
   ```sql
   CREATE DATABASE yardly;
   CREATE USER yardly_user WITH PASSWORD 'secure_password';
   GRANT ALL PRIVILEGES ON DATABASE yardly TO yardly_user;
   ```

3. Update settings.py to use environment variables:
   ```python
   import os
   from decouple import config
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': config('DB_NAME', default='yardly'),
           'USER': config('DB_USER', default='yardly_user'),
           'PASSWORD': config('DB_PASSWORD'),
           'HOST': config('DB_HOST', default='localhost'),
           'PORT': config('DB_PORT', default='5432'),
       }
   }
   ```

## Deployment Steps

### 1. Prepare the Server

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade

# Install dependencies
sudo apt-get install python3-pip python3-venv nginx postgresql redis-server

# Create application user
sudo useradd -m -s /bin/bash yardly
sudo su - yardly
```

### 2. Clone and Setup Application

```bash
# Clone repository
git clone https://github.com/micdr93/yardly.git
cd yardly

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# Create .env file
nano .env
# Add your environment variables
```

### 3. Configure Django

```bash
# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 4. Configure Gunicorn

Create `/etc/systemd/system/yardly.service`:

```ini
[Unit]
Description=Yardly Gunicorn daemon
After=network.target

[Service]
User=yardly
Group=www-data
WorkingDirectory=/home/yardly/yardly
Environment="PATH=/home/yardly/yardly/venv/bin"
ExecStart=/home/yardly/yardly/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/yardly/yardly/gunicorn.sock \
          yardly_platform.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start Gunicorn:
```bash
sudo systemctl start yardly
sudo systemctl enable yardly
```

### 5. Configure Nginx

Create `/etc/nginx/sites-available/yardly`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /home/yardly/yardly/staticfiles/;
    }
    
    location /media/ {
        alias /home/yardly/yardly/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/yardly/yardly/gunicorn.sock;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/yardly /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 6. SSL/HTTPS Setup with Let's Encrypt

```bash
# Install certbot
sudo apt-get install certbot python3-certbot-nginx

# Obtain certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal is configured automatically
```

## Monitoring and Maintenance

### Application Logs

```bash
# Gunicorn logs
sudo journalctl -u yardly -f

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Database Backup

```bash
# Create backup script
cat > /home/yardly/backup.sh << 'EOF'
#!/bin/bash
BACKUP_DIR=/home/yardly/backups
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -U yardly_user yardly > $BACKUP_DIR/yardly_$DATE.sql
find $BACKUP_DIR -name "yardly_*.sql" -mtime +7 -delete
EOF

chmod +x /home/yardly/backup.sh

# Add to crontab (daily at 2 AM)
crontab -e
0 2 * * * /home/yardly/backup.sh
```

### Updates and Maintenance

```bash
# Update application
cd /home/yardly/yardly
git pull origin main
source venv/bin/activate
pip install -r requirements.txt --upgrade
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart yardly
```

## Performance Optimization

### Redis Caching

Add to settings.py:
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': config('REDIS_URL', default='redis://127.0.0.1:6379/1'),
    }
}
```

### Database Connection Pooling

```python
DATABASES = {
    'default': {
        # ... other settings ...
        'CONN_MAX_AGE': 600,  # Connection pooling
    }
}
```

### Static File CDN

Consider using AWS CloudFront or similar CDN for static files.

## Security Checklist

- [ ] SECRET_KEY is random and secure
- [ ] DEBUG = False in production
- [ ] ALLOWED_HOSTS properly configured
- [ ] Database uses strong password
- [ ] SSL/HTTPS enabled
- [ ] Security middleware enabled
- [ ] CSRF protection enabled
- [ ] XSS protection enabled
- [ ] Regular security updates applied
- [ ] Firewall configured (UFW or similar)
- [ ] Rate limiting implemented
- [ ] Backup strategy in place

## Scaling Considerations

### Horizontal Scaling

- Use load balancer (AWS ELB, DigitalOcean Load Balancer)
- Multiple application servers
- Shared media storage (S3, DigitalOcean Spaces)
- Database replication for read scaling

### Vertical Scaling

- Increase server resources (CPU, RAM)
- Optimize database queries
- Implement caching strategy
- Use database indexes effectively

## Troubleshooting

### Application won't start

```bash
# Check Gunicorn status
sudo systemctl status yardly

# Check logs
sudo journalctl -u yardly -n 50

# Test Gunicorn manually
cd /home/yardly/yardly
source venv/bin/activate
gunicorn --bind 0.0.0.0:8000 yardly_platform.wsgi:application
```

### Static files not loading

```bash
# Ensure static files are collected
python manage.py collectstatic --noinput

# Check Nginx configuration
sudo nginx -t

# Check file permissions
ls -la /home/yardly/yardly/staticfiles/
```

### Database connection errors

```bash
# Test database connection
psql -U yardly_user -d yardly -h localhost

# Check PostgreSQL status
sudo systemctl status postgresql
```

## Support

For deployment issues:
- Check documentation: https://docs.djangoproject.com/en/stable/howto/deployment/
- Open an issue: https://github.com/micdr93/yardly/issues

## Production Best Practices

1. **Use environment variables** for all sensitive data
2. **Regular backups** of database and media files
3. **Monitor application** with tools like Sentry
4. **Update dependencies** regularly for security
5. **Use a CDN** for static files
6. **Implement rate limiting** to prevent abuse
7. **Set up monitoring** and alerting
8. **Document your deployment** process
9. **Test in staging** before production deployment
10. **Have a rollback plan** ready
