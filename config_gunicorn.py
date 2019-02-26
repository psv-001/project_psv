#!/usr/bin/env python3.4

"""
This file contains the settings for gunicorn
"""

bind = '0.0.0.0:8000'
workers = 3
timeout = 500
