import datetime
import json

from mv_files import rename_doya, rename_fmb
from common.types import ConfigDict


with open("config.json") as f:
    _config = json.loads(f.read())


base_config: ConfigDict = _config["base"]

config: dict[str, ConfigDict] = {
    'doya': _config['doya'],
    'fmb': _config['fmb']
}
config['doya']['renamer'] = rename_doya
config['fmb']['renamer'] = rename_fmb


def get_config(radio_name: str) -> ConfigDict:
    base_config.update(config[radio_name])
    return base_config


def get_url(cfg: ConfigDict, date: datetime.date) -> str:
    return cfg['url_template'].replace('{date}', date.strftime('%Y%m%d'))
