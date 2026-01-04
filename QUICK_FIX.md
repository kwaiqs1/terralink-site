# Quick Fix Guide - Database Error

## The Problem
You're seeing: `OperationalError: no such table: products_product`

This happens because the database tables haven't been created yet.

## The Solution

Run these commands in order:

```bash
cd terralink_site

# 1. Create migrations
python manage.py makemigrations

# 2. Apply migrations (creates tables)
python manage.py migrate

# 3. Load initial demo data (optional but recommended)
python manage.py loaddata fixtures/initial_data.json

# 4. Create admin user (optional)
python manage.py createsuperuser

# 5. Start server
python manage.py runserver
```

## What Changed

The site is now **safe** to run even before migrations - it will show "coming soon" messages instead of crashing. However, for full functionality, you still need to run migrations.

## After Running Migrations

The site will work fully with:
- Product pages showing data
- Pricing information
- Team pages
- Pilot status
- All features functional

## Alternative: Use Setup Script

```bash
python setup_database.py
```

This script automates steps 1-3 above.

