# manage files folders etc.
import os
from pathlib import Path

from instaloader import Post

from instagram_archiver import metadata, MONTH_FORMAT, TIME_IN_FILENAME_FORMAT


def create_folders(settings: metadata.Settings):
    """idempotent folder creation of all archived users"""
    for username in settings.usernames:
        os.makedirs(settings.save_path / username, exist_ok=True)


def get_save_path(post: Post, settings: metadata.Settings) -> Path:
    time = post.date_utc
    month_name = time.strftime(MONTH_FORMAT).lower()
    filename = '{}_{}'.format(time.strftime(TIME_IN_FILENAME_FORMAT), post.pcaption)
    return Path(settings.save_path / post.owner_username / month_name / filename)
