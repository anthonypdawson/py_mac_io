
import logging
import os
import re

import requests
from urllib3.util import parse_url, Url
from requests import Request, Response, JSONDecodeError

from pymacio.mac_io_environment import MacIoEnvironment

logger = logging.getLogger(__name__)


class PyMacIo:
    mac_pattern = r'^([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}$'

    def __init__(self, mac_address: str, **kwargs):
        self.environment = MacIoEnvironment(**kwargs)
        self.mac_address = mac_address
        self._mac_details: dict = None

    @property
    def mac_details(self):
        if not self._mac_details:
            self._mac_details = self.make_request(self.mac_address)
        return self._mac_details

    def print_all_details(self):
        if self.mac_details:
            print(self.mac_details)
        else:
            print("Details not found")

    def print_company_name(self):
        company_name = self.get_company_name()
        print(f"Company name: {company_name}")

    def is_valid_mac_address(self, mac_address: str) -> bool:
        return re.match(self.mac_pattern, mac_address)

    def make_request(self, mac_address=None) -> dict:
        if not mac_address:
            mac_address = self.mac_address

        if not self.is_valid_mac_address(mac_address):
            logger.error(f"Invalid mac address: {mac_address}")
            exit(1)

        params = self._build_params(mac_address)
        req: Request = self._build_request(params)
        logger.debug(req)

        with requests.Session() as session:
            response = session.send(request=req.prepare())
            session.close()

        if not response.ok:
            logger.warning(
                f"Response reported not ok{os.linesep}"
                f"Status: {response.status_code}{os.linesep}"
                f"Text: {response.text}")
            response.raise_for_status()

        return self.parse_response(response)

    def parse_response(self, response: Response) -> dict:
        try:
            resp_dict = response.json()
            return resp_dict
        except JSONDecodeError as ex:
            logger.error(f"JSON decoding error: {ex}")
            # Raising to console
            raise ex

    def get_full_details(self) -> str:
        if self.mac_details:
            return str(self.mac_details)
        else:
            return None

    def get_company_name(self):
        company_name = None
        if self.mac_details:
            vendor_details = self.mac_details.get('vendorDetails', None)
            if vendor_details:
                company_name = vendor_details.get("companyName", None)
        return company_name

    def _build_params(self, mac_address=None):
        if not mac_address:
            mac_address = self.mac_address
        return {"apiKey": self.environment.api_key,
                "output": self.environment.output_format,
                "search": mac_address}

    def _build_request(self, params=None):
        url: Url = parse_url(self.environment.api_url)
        req = Request(method="POST", url=url)
        if params:
            req.params = params
        return req
