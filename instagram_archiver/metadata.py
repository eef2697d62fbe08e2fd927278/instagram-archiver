# read metadata and similar etc.
import datetime
import os
import json
from typing import List
from pathlib import Path

from instagram_archiver import DATE_FORMAT


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


class AccountMetadata:
    FILENAME = 'meta.json'

    def __init__(self, username: str, last_scraped_date: datetime.datetime):
        self.username = username
        self.last_scraped_date = last_scraped_date

    @classmethod
    def load(cls, save_path: Path, username: str):
        with open(save_path / username / cls.FILENAME, mode='r', encoding='UTF-8') as file:
            data = json.loads(file.read())

        return AccountMetadata(username, data['last_scraped'])

    def save(self, save_path: Path):
        data = {'last_scraped': self.last_scraped_date.strftime(DATE_FORMAT)}

        with open(save_path / self.username / self.FILENAME, mode='w', encoding='UTF-8') as file:
            file.write(json.dumps(data))
