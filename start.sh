#!/bin/bash
import multiprocessing
# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn SNR.wsgi:application \
    --bind 0.0.0.0:8000 \
    --timeout 120 \
    --workers 3
