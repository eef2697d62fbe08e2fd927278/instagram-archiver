import json
from pathlib import Path

import instaloader

ROOT = Path(__file__).parents[1]
settings = json.loads(Path(ROOT / 'settings.json').read_text('UTF-8'))
save_path = settings['save_path']


def main():
    loader = instaloader.Instaloader()
    loader.interactive_login(settings['account'])

    for username in settings['usernames']:
        profile = instaloader.Profile.from_username(loader.context, username)
        for post in profile.get_posts():
            time = post.date_utc
            loader.download_post(post, username)


if __name__ == '__main__':
    main()
