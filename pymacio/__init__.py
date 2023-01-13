import logging
import os

from pymacio.py_mac_io import PyMacIo
import argparse

LOG_LEVEL = logging.INFO

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Query macaddress.io for company name for a given mac address")
    parser.add_argument("address", type=str, metavar='str', help="MAC address with optional colons")
    parser.add_argument("--key", type=str, default=None, required=False,
                        help="Override macaddress.io API key from .env")
    parser.add_argument("--full", action="store_true", default=False,
                        help="Display full information instead of only company name")
    parser.add_argument("-v", "--verbose", action="store_true", default=False)
    args: argparse.Namespace = parser.parse_args()

    if args.verbose:
        LOG_LEVEL = logging.DEBUG
        logger.setLevel(LOG_LEVEL)

    logger.debug(args)
    pymacio: PyMacIo = PyMacIo(args.address, api_key=args.key)
    print(f"Company name: {pymacio.get_company_name()}")
    if args.full:
        print(f"{os.linesep}")
        print(f"Full details: {pymacio.get_full_details()}")
