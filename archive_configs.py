import logging
import os
from datetime import datetime

from config import dnac_base_url, dnac_password, dnac_username, dnac_verify
from DNACModule import DNAC

# set up the logging
logging.basicConfig(level=logging.INFO)

# define the archive folder however makes sense
# for this, we'll just use the directory this script is in and create a folder called zConfigArchive
archive_path = __file__.replace(__file__.split(os.sep)[-1], 'zConfigArchive') + '\\'

logging.info(f'Archive path: {archive_path}')

# create the folder if it doesn't exist yet
if not os.path.exists(archive_path):
    os.mkdir(archive_path)

# create a folder for this particular time
t_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
archive_folder = archive_path + t_stamp + '\\'

logging.info(f'Archive folder: {archive_folder}')

# create the folder
if not os.path.exists(archive_folder):
    os.mkdir(archive_folder)

# create the DNAC object
dnac_api = DNAC(dnac_username, dnac_password, dnac_base_url, dnac_verify)

# get the device list
device_list = dnac_api.get_device_list()

for d in device_list:
    cfg = dnac_api.get_device_config(d['id'])

    with open(f"{archive_folder}{t_stamp}_{d['hostname']}_config.txt", 'wt') as f:
        f.write(cfg)

        logging.info(f'Saved config -- {d["hostname"]} -- {f.name}')

logging.info('Complete')
