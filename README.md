# TerraLink AI Greenhouse Website

Production-ready, mobile-first Django website for TerraLink AI Greenhouse - AI-powered decision intelligence for greenhouse crops.

## Features

- **Full-featured Django application** with SQLite (dev) and Postgres (prod) support
- **Mobile-first responsive design** using Tailwind CSS
- **All core pages**: Home, Products, How It Works, Technology, Pricing, Team, Pilot Status, Contact
- **Contact form** with spam protection (honeypot + rate limiting)
- **REST API endpoints** for products and contact
- **Admin interface** for content management
- **SEO-friendly** with sitemaps and meta tags
- **Docker support** for easy deployment

## Quick Start

### Local Development (SQLite)

1. **Create and activate virtual environment:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env with your settings (optional for local dev)
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Load initial data:**
```bash
python manage.py loaddata fixtures/initial_data.json
```

7. **Run development server:**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the site and `http://127.0.0.1:8000/admin/` for the admin interface.

## Docker Development

1. **Build and run:**
```bash
docker-compose up --build
```

2. **Run migrations:**
```bash
docker-compose exec web python manage.py migrate
```

3. **Create superuser:**
```bash
docker-compose exec web python manage.py createsuperuser
```

4. **Load initial data:**
```bash
docker-compose exec web python manage.py loaddata fixtures/initial_data.json
```

The site will be available at `http://localhost:8000/`

## Project Structure

```
terralink_site/
├── core/              # Core app (home, how-it-works, technology pages)
├── products/          # Products and pricing
├── team/              # Team members
├── contact/           # Contact form
├── pilot/             # Pilot program status
├── templates/         # Django templates
├── static/            # Static files (CSS, JS, images)
├── fixtures/          # Initial data fixtures
├── media/             # User uploads (created at runtime)
├── manage.py
├── requirements.txt
└── README.md
```

## Environment Variables

Create a `.env` file in the project root (see `.env.example`):

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (for production - SQLite used by default)
DATABASE_URL=postgresql://user:password@localhost:5432/terralink

# Email (for production)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
DEFAULT_FROM_EMAIL=noreply@terralink.org
CONTACT_EMAIL=bekai4ik@gmail.com
```

## Running Tests

```bash
python manage.py test
```

## Production Deployment

### Using Docker (Recommended)

1. **Set environment variables** in production (use your hosting platform's env vars)

2. **Build and deploy:**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Manual Deployment

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Collect static files:**
```bash
python manage.py collectstatic --noinput
```

3. **Run migrations:**
```bash
python manage.py migrate
```

4. **Load initial data:**
```bash
python manage.py loaddata fixtures/initial_data.json
```

5. **Run with Gunicorn:**
```bash
gunicorn terralink_site.wsgi:application --bind 0.0.0.0:8000
```

6. **Configure Nginx** to serve static files and proxy to Gunicorn

### Database Setup (Production)

For production, use PostgreSQL:

```bash
# Install PostgreSQL dependencies
pip install psycopg2-binary

# Update DATABASES in settings.py or use DATABASE_URL environment variable
```

### Static Files & Media (Production)

For production, use S3 or similar:

1. Install `django-storages` and `boto3`
2. Configure in settings.py:
```python
AWS_ACCESS_KEY_ID = 'your-key'
AWS_SECRET_ACCESS_KEY = 'your-secret'
AWS_STORAGE_BUCKET_NAME = 'your-bucket'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
```

## Admin Interface

Access the admin at `/admin/` after creating a superuser.

**Models available:**
- Products (Product, PricingPlan)
- Team (TeamMember)
- Pilot (Pilot)
- Contact (ContactRequest)

## API Endpoints

- `GET /api/products/` - List all products
- `GET /api/products/<slug>/` - Product detail
- `POST /api/contact/` - Submit contact form
- `GET /api/pilot-status/` - Get pilot status

## Replacing Placeholder Images

1. **Team photos:** Upload photos via admin at `/admin/team/teammember/`
2. **Product icons:** Edit SVG in admin or replace in templates
3. **Hero images:** Replace SVG placeholders in `templates/core/home.html`

**Recommended stock photo keywords:**
- Greenhouse interior
- Agritech drone
- Plant closeup
- Agricultural technology
- Precision farming

## Content Management

All content can be managed through the Django admin interface:

1. Log in at `/admin/`
2. Navigate to the relevant model (Products, Team, Pilot, etc.)
3. Add/edit content as needed

## Contact Form

The contact form includes:
- **Spam protection:** Honeypot field + rate limiting (5 requests per hour per IP)
- **Email notifications:** Sent to `CONTACT_EMAIL` (configured in settings)
- **File uploads:** Optional file attachments
- **Product interest tracking:** Links to specific products

## Troubleshooting

### Database errors
- Ensure migrations are run: `python manage.py migrate`
- Check database permissions and connection

### Static files not loading
- Run `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` in settings
- Ensure WhiteNoise is configured correctly

### Email not sending
- Check `EMAIL_*` settings in `.env`
- For development, use console backend (default)
- For production, configure SMTP or SendGrid

### Images not displaying
- Check `MEDIA_ROOT` and `MEDIA_URL` settings
- Ensure media directory is writable
- In production, configure media file storage (S3 recommended)

## License

Proprietary - All rights reserved

## Contact

For questions or support, contact: bekai4ik@gmail.com

