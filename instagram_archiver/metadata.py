# read metadata and similar etc.
import os
import json
from typing import List
from pathlib import Path


class Settings:
    def __init__(self, account: str, usernames: List[int], save_path: str):
        self.account = account
        self.usernames = usernames
        self.save_path = Path(save_path)

        os.makedirs(self.save_path, exist_ok=True)


def get_settings(file_path):
    settings = json.loads(Path(file_path).read_text('UTF-8'))
    return Settings(
        account=settings['account'],
        usernames=settings['usernames'],
        save_path=settings['save_path']
    )


# TODO: create mechanism that saves the datetime when last was scraped,
#  so it will only scrape images newer than said date
