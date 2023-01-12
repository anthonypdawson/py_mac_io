import json

import requests
from urllib3.util import parse_url, Url
from requests import Request, Response

from pymacio.mac_io_environment import MacIoEnvironment


class PyMacIo:

    def __init__(self, **kwargs):
        self.environment = MacIoEnvironment(**kwargs)

    def check_mac_address(self, mac_addresses):
        pass

    def make_requests(self, *addresses):
        pass

    def make_request(self, address):
        params = self._build_params(address)
        req: Request = self._build_request(params)
        response: Response = None

        with requests.Session as session:
            response = session.send(request=req.prepare())
            session.close()

        if not response.ok:
            pass    # Failure condition

        print(f"Mac address: {address}")
        json_data = response.text
        json.loads(json_data)
        print(f"Info: {response.text}")

    def _build_params(self, mac_address):
        return {"apiKey": self.environment.api_key,
                "output": self.environment.output_format,
                "search": mac_address}

    def _build_request(self, params=None):
        url: Url = parse_url(self.environment.api_url)
        req = Request(method="POST", url=url)
        if params:
            req.params = params
        return req
