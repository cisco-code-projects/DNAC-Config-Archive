import logging

from dnacentersdk import DNACenterAPI
from dnacentersdk.exceptions import ApiError


class DNAC():

    def __init__(self, username, password, base_url, verify):

        self.api = DNACenterAPI(
            base_url=base_url,
            username=username,
            password=password,
            verify=verify
        )

    def get_device_list(self):

        device_list = self.api.devices.get_device_list()

        logging.info(f'Number of devices retrieved from DNAC: {len(device_list["response"]):,}')

        return [{'hostname': x['hostname'], 'id': x['id']} for x in device_list['response'] if x['hostname']]

    def get_device_config(self, d_id):

        try:

            d = self.api.devices.get_device_config_by_id(d_id)

            return d['response']

        except ApiError as e:

            if e.status_code == 501:
                logging.warning(f'ApiError getting config: {e}')
                return None
