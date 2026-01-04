# TerraLink AI Website - Setup Guide

## Quick Start Checklist

1. ✅ **Project structure created**
2. ✅ **All models defined** (Product, TeamMember, Pilot, PricingPlan, ContactRequest)
3. ✅ **All views and URLs configured**
4. ✅ **Templates created** (base, home, products, team, contact, pilot, etc.)
5. ✅ **Admin interface configured**
6. ✅ **API endpoints created**
7. ✅ **Fixtures with initial data**
8. ✅ **Docker configuration**
9. ✅ **Tests written**

## Next Steps to Run the Project

### 1. Install Dependencies

```bash
cd terralink_site
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the `terralink_site` directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=noreply@terralink.org
CONTACT_EMAIL=bekai4ik@gmail.com
```

### 3. Initialize Database

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures/initial_data.json
```

### 4. Run Server

```bash
python manage.py runserver
```

Visit:
- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Key Files Created

### Models
- `products/models.py` - Product, PricingPlan
- `team/models.py` - TeamMember
- `pilot/models.py` - Pilot
- `contact/models.py` - ContactRequest

### Views & URLs
- `core/views.py` - Home, How It Works, Technology, Privacy, Terms
- `products/views.py` - Product list, detail, pricing
- `team/views.py` - Team list
- `contact/views.py` - Contact form with spam protection
- `pilot/views.py` - Pilot status

### Templates
- `templates/base.html` - Base template with navigation
- `templates/core/home.html` - Hero and homepage
- `templates/products/*.html` - Product pages
- `templates/contact/form.html` - Contact form
- `templates/team/list.html` - Team page
- `templates/pilot/status.html` - Pilot status
- Plus privacy, terms, how-it-works, technology templates

### API
- `core/api_views.py` - API endpoints
- `core/api_urls.py` - API URL routing

### Configuration
- `README.md` - Comprehensive documentation
- `Dockerfile` - Docker configuration
- `docker-compose.yml` - Docker Compose setup
- `fixtures/initial_data.json` - Initial data

## Features Implemented

✅ Mobile-first responsive design
✅ Tailwind CSS styling
✅ Alpine.js for interactivity
✅ Contact form with honeypot + rate limiting
✅ Email notifications
✅ Admin interface
✅ REST API endpoints
✅ SEO (sitemaps, meta tags, robots.txt)
✅ Tests for core functionality
✅ Docker support
✅ Fixtures for initial data

## Notes

- All copy and pricing information is based on the requirements provided
- SVG placeholders are used for images (replace with actual images)
- Email backend defaults to console for development
- Contact email: bekai4ik@gmail.com
- Social media: @terralink_org (configure in templates if needed)

## Production Deployment

See README.md for detailed production deployment instructions including:
- PostgreSQL setup
- S3 for media/static files
- Gunicorn configuration
- Nginx setup
- Environment variables

