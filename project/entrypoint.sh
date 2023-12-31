#!/usr/bin/env bash

until python3 manage.py makemigrations menu --no-input && python3 manage.py migrate --no-input
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python3 manage.py runserver 0.0.0.0:8000