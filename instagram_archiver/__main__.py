import argparse
import time
from os.path import exists

import instaloader

from instagram_archiver import files, metadata, DATE_FORMAT


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--settings', help='Path to the settings json file')
    args = parser.parse_args()
    if not args.settings:
        raise RuntimeError('-h for help')
    if not exists(args.settings):
        raise FileNotFoundError

    settings = metadata.get_settings(args.settings)

    loader = instaloader.Instaloader()
    loader.interactive_login(settings.account)

    for username in settings.usernames:
        profile = instaloader.Profile.from_username(loader.context, username)
        try:
            old_metadata = metadata.AccountMetadata.load(settings.save_path, username)
        except FileNotFoundError:
            print('trying to scrape all files')
        else:
            print('scraping images since {}'.format(time.strftime(DATE_FORMAT, time)))
        for post in profile.get_posts():
            if old_metadata:
                if post.date_utc < old_metadata.last_scraped_date:
                    continue

            loader.download_post(post, files.get_save_path(post, settings))

        new_metadata = metadata.AccountMetadata(username, last_scraped_date=time)
        new_metadata.save(settings.save_path)


if __name__ == '__main__':
    main()
