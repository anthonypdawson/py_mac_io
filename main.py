import logging

from pymacio import LOG_LEVEL
from pymacio.py_mac_io import PyMacIo
import argparse
logging.info("Started")
logger = logging.getLogger(__name__)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mac_address = ""
    parser = argparse.ArgumentParser(description="Interact with the macaddress.io API")
    parser.add_argument("addresses", type=str, metavar='str', nargs="+")
    parser.add_argument("--key", type=str, default=None, required=False)
    parser.add_argument("-v", "--verbose", action="store_true", default=False)
    args: argparse.Namespace = parser.parse_args()

    if args.verbose:
        LOG_LEVEL=logging.DEBUG
        logger.setLevel(LOG_LEVEL)

    logger.debug(args)
    logger.info(f"Checking addresses: {args.addresses}")
    pymacio: PyMacIo = PyMacIo(api_key=args.key)
    pymacio.make_request(args.addresses)
