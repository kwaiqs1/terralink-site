#!/usr/bin/env python
"""
Database setup script for TerraLink site.
Run this after initial project setup to create migrations and load initial data.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terralink_site.settings')
django.setup()

from django.core.management import call_command
from django.db import connection

def setup_database():
    """Create migrations, migrate, and load initial data"""
    print("=" * 60)
    print("TerraLink Database Setup")
    print("=" * 60)
    
    # Check if database exists
    db_path = 'db.sqlite3'
    db_exists = os.path.exists(db_path)
    
    if db_exists:
        print(f"\nDatabase file exists: {db_path}")
        response = input("Delete existing database and start fresh? (yes/no): ")
        if response.lower() == 'yes':
            os.remove(db_path)
            print("Database deleted.")
        else:
            print("Using existing database.")
    
    # Make migrations
    print("\n1. Creating migrations...")
    try:
        call_command('makemigrations')
        print("✓ Migrations created successfully")
    except Exception as e:
        print(f"✗ Error creating migrations: {e}")
        return False
    
    # Run migrations
    print("\n2. Running migrations...")
    try:
        call_command('migrate', verbosity=1)
        print("✓ Migrations applied successfully")
    except Exception as e:
        print(f"✗ Error running migrations: {e}")
        return False
    
    # Load initial data
    print("\n3. Loading initial data...")
    fixture_path = 'fixtures/initial_data.json'
    if os.path.exists(fixture_path):
        try:
            call_command('loaddata', fixture_path, verbosity=1)
            print("✓ Initial data loaded successfully")
        except Exception as e:
            print(f"✗ Error loading initial data: {e}")
            print("  (This is OK if data already exists)")
    else:
        print(f"⚠ Fixture file not found: {fixture_path}")
    
    print("\n" + "=" * 60)
    print("Database setup complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Create a superuser: python manage.py createsuperuser")
    print("2. Run the server: python manage.py runserver")
    print("3. Visit: http://127.0.0.1:8000/")
    
    return True

if __name__ == '__main__':
    success = setup_database()
    sys.exit(0 if success else 1)

