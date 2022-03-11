from os.path import exists
import argparse

import instaloader

from . import files, metadata


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--settings', help='Path to the settings json file')
    args = parser.parse_args()
    if not args['--settings']:
        raise RuntimeError
    if not exists(args['--settings']):
        raise FileNotFoundError

    settings = metadata.get_settings(args['--settings'])

    loader = instaloader.Instaloader()
    loader.interactive_login(settings.account)

    for username in settings.usernames:
        profile = instaloader.Profile.from_username(loader.context, username)
        for post in profile.get_posts():
            time = post.date_utc
            loader.download_post(post, username)


if __name__ == '__main__':
    main()
