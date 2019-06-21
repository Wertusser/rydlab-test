#!/usr/bin/env bash
while true; do
    python3 create_db.py
    if [ $? -eq 0 ]; then
        echo 'Database successfully initialized'
        break
    fi

    echo 'Database initialization failed, retrying in 5 seconds...'
    sleep 5
done
gunicorn -c gunicorn.conf.py gist.app:app
