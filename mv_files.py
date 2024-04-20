from datetime import datetime, timedelta
import os
import shutil
import logging

from common.types import ConfigDict


logger = logging.getLogger(__name__)


def rename_doya(old_filename: str):
    # Log the start of the function
    logger.info("Starting rename_doya function.")

    # old_filename e.g. QRR_20240420013000_20240420020000.aac
    # Get the date part
    date_string = old_filename.split("_")[1][:8]
    date_format = "%Y%m%d"
    date = datetime.strptime(date_string, date_format)

    # Move the date back by one day
    previous_date = date - timedelta(days=1)
    new_date = previous_date.strftime(date_format)
    new_filename = f'{new_date} doya.aac'

    # Log the end of the function
    logger.info("rename_doya function completed successfully.")

    return new_filename


def rename_fmb(old_filename: str):
    # Log the start of the function
    logger.info("Starting rename_fmb function.")
    # old_filename e.g. BAYFM78_20240413220000_20240413223000.aac
    # get date part
    date_string = old_filename.split("_")[1][:8]
    new_filename = f'{date_string} fmb.aac'

    # Log the end of the function
    logger.info("rename_fmb function completed successfully.")
    return new_filename


def rename_and_move_file(config: ConfigDict, file_path: str):
    renamer = config['renamer']

    old_file_name = os.path.basename(file_path)
    new_file_name = renamer(old_file_name)
    new_file_path = os.path.join(config['dst_dir'], new_file_name)

    # Move the file to the target directory
    old_file_path = file_path
    shutil.move(old_file_path, new_file_path)
    logger.info(f"File moved from {old_file_path} to {new_file_path}")
