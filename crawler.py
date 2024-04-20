import os
import time
import datetime
import logging

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import ConfigDict, get_url

logger = logging.getLogger(__name__)


def wait_until_aac_downloaded(download_dir: str) -> str:
    while True:
        files = os.listdir(download_dir)
        for file_name in files:
            if file_name.endswith(".aac"):
                return os.path.join(download_dir, file_name)
        time.sleep(3)


def crawler(config: ConfigDict, date: datetime.date) -> str:
    chrome_options = Options()

    extension_path = os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)
        ), config['radiko_extension_path']
    )

    chrome_options.add_argument(f"--disable-extensions-except={extension_path}")
    chrome_options.add_argument(f"--load-extension={extension_path}")

    driver = webdriver.Chrome(options=chrome_options)

    url = get_url(config, date)

    driver.get(url)

    driver.maximize_window()

    # # Wait for some time to ensure page loading
    # driver.implicitly_wait(15)

    # Function for clicking extension button
    def click(name):
        x, y = config['mouse_positions'][name]
        pyautogui.click(x, y)
        logging.info(f"clicking {name}")
        time.sleep(1)

    click('click chrome extension button')
    click('pin rajiko')
    click('click rajiko')
    click('click download')

    return wait_until_aac_downloaded(config['src_dir'])

# Example usage:
# crawler('https://radiko.jp/#!/ts/BAYFM78/20240413220000', 'radiko_extension_path')
