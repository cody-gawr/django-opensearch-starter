#!/bin/sh

set -e

# Wait for MySQL to be ready
echo "⏳ Waiting for database..."

until mysqladmin ping -h"$DB_HOST" --silent; do
  echo "⌛ Still waiting for DB at $DB_HOST..."
  sleep 2
done

echo "✅ Database is up!"

# Run migrations
echo "📦 Running migrations..."
python manage.py migrate

# Optional: seed data
# echo "🌱 Seeding data..."
# python manage.py seed_products --count=10

# Start the app
echo "🚀 Starting server..."
exec "$@"
