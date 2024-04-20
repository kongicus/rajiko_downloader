from config import get_config
import datetime
import logging
import argparse

from crawler import crawler
from mv_files import rename_and_move_file

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('--radio-name', type=str)


def get_last_saturday() -> datetime.date:
    today = datetime.date.today()

    # Calculate the difference in days to the previous Saturday
    days_to_last_saturday = (today.weekday() - 5) % 7

    # Subtract the difference to get the date of the last Saturday
    last_saturday = today - datetime.timedelta(days=days_to_last_saturday)
    return last_saturday


def main():
    args = parser.parse_args()
    config = get_config(args.radio_name)
    downloaded_file = crawler(config, get_last_saturday())
    rename_and_move_file(config, downloaded_file)


if __name__ == '__main__':
    main()
