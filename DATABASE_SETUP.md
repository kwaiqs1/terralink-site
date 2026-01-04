# Database Setup Instructions

## Quick Setup

After cloning the repository, you must initialize the database before the site will work.

### Option 1: Using the Setup Script (Recommended)

```bash
python setup_database.py
```

This script will:
1. Create all migrations
2. Apply migrations to create database tables
3. Load initial demo data

### Option 2: Manual Setup

```bash
# 1. Create migrations
python manage.py makemigrations

# 2. Apply migrations
python manage.py migrate

# 3. Load initial data
python manage.py loaddata fixtures/initial_data.json

# 4. Create admin user
python manage.py createsuperuser
```

## What Gets Created

After running migrations, the following tables are created:
- `products_product` - Product information
- `products_pricingplan` - Pricing plans
- `team_teammember` - Team member profiles
- `pilot_pilot` - Pilot program information
- `contact_contactrequest` - Contact form submissions
- Plus Django's built-in tables (users, sessions, etc.)

## Initial Data

The `fixtures/initial_data.json` file contains:
- 2 sample products (TerraLink Greenhouse AI, TerraLink Drone Validator)
- 2 pricing plans (AI Subscription, Drone Service)
- 1 pilot program entry

You can add more data via the admin interface at `/admin/`.

## Troubleshooting

### "no such table" errors
- **Solution:** Run migrations: `python manage.py migrate`

### "fixture not found" errors
- **Solution:** Ensure you're in the `terralink_site` directory and the `fixtures/initial_data.json` file exists

### Database locked errors (SQLite)
- **Solution:** Close any other processes using the database (other Django instances, DB browsers, etc.)

### Migration conflicts
- **Solution:** If you have conflicting migrations, you can reset:
  ```bash
  # Delete db.sqlite3 and all migration files (except __init__.py)
  # Then recreate:
  python manage.py makemigrations
  python manage.py migrate
  ```

## Safe Mode

The site is designed to work even if the database is empty or tables don't exist. Pages will show "coming soon" messages instead of crashing. However, for full functionality, you should run migrations and load initial data.

