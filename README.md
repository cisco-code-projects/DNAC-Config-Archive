# Cisco DNA Center Config Archive Script

This sample script will connect to a single Cisco DNA Center server using the Python DNAC SDK and the DNA Center API.  It will programmatically download all of the device configurations to a local archive folder.

## Installation

Python 3.9 was used to create the script.  No other versions tested.

Install the dependencies defined in the requirements.txt file.

```bash
pip install -r requirements.txt
```

## Usage

Update the "config.py" file with the admin username/password and base URL for your DNA Center
```python
dnac_username = 'admin_user'
dnac_password = 'admin_password'
dnac_base_url = 'https://dnac.example.org'
dnac_verify = False
```

Execute the "archive_configs.py" script
```bash
python.exe archive_configs.py
```

A subfolder will be automatically created for the configurations based on the timestamp.  Each config will be saved as a text file within that folder.


## License
This project is licensed to you under the terms of the [Cisco Sample Code License.](https://github.com/cisco-code-projects/DNAC-Config-Archive/main/LICENSE)