# manage files folders etc.
import os

from . import metadata


def create_folders(settings: metadata.Settings):
    """idempotent folder creation of all archived users"""
    for username in settings.usernames:
        os.makedirs(settings.save_path / username, exist_ok=True)


def months():
    """maybe; return list of each month like '01-jan', '10-oct', etc. """
    pass
