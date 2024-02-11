#!/bin/bash

# Apply database migrations
python auctionsonline/manage.py migrate

# Apply make migrations (if needed)
python auctionsonline/manage.py makemigrations

# Start the Django development server
python auctionsonline/manage.py runserver 0.0.0.0:8000
