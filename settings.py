"""Settings for feedgrabber"""
from django.conf import settings

UPDATE_HOUR_LIMIT = getattr(settings, 'FEEDGRABBER_UPDATE_HOUR_LIMIT', 24)
RECENT_HOUR_LIMIT = getattr(settings, 'FEEDGRABBER_RECENT_HOUR_LIMIT', 48)
USER_AGENT = getattr(settings, 'FEEDGRABBER_USER_AGENT', 'FeedGrabber/0.1b')
