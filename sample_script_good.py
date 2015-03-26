"""
This scripts demonstrates a collection of best practices for production-ready
Python scripts.
"""

import argparse
import logging
import os
import random
import time


def configure_logging():  # pragma: no cover
    script_name = os.path.basename(__file__)
    f = '%(asctime)s | {} | %(levelname)s | %(message)s'.format(script_name)
    logging.basicConfig(format=f, level='INFO')


def get_arguments():  # pragma: no cover
    parser = argparse.ArgumentParser(description='Sample script.')
    parser.add_argument('offset', help='Integer for sample action.', type=int)
    return parser.parse_args()


def run(offset):
    result = offset + random.randint(0, 9)
    if result < 10:
        logging.info('Computed {}. Acting.'.format(result))
        time.sleep(2)  # Simulate a delay while the script works.
        logging.info('Action complete.')
    else:
        logging.warn('Computed a number too large. Not acting.')
    return result


if __name__ == '__main__':  # pragma: no cover
    configure_logging()
    args = get_arguments()
    run(offset=args.offset)
