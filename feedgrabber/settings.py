"""Settings for feedgrabber"""
from django.conf import settings

PAGINATION = getattr(settings, 'FEEDGRABBER_PAGINATION', 20)
UPDATE_HOUR_LIMIT = getattr(settings, 'FEEDGRABBER_UPDATE_HOUR_LIMIT', 24)
RECENT_HOUR_LIMIT = getattr(settings, 'FEEDGRABBER_RECENT_HOUR_LIMIT', 48)
USER_AGENT = getattr(settings, 'FEEDGRABBER_USER_AGENT', 'FeedGrabber/0.1b')
