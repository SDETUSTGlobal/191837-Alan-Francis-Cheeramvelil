import sys

import pytest
from _pytest import logging
from assertpy import assert_that
from pytest_reportportal import RPLogger, RPLogHandler
from reportportal_client import client
import requests



@pytest.fixture(scope="session")
def logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)

        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)

    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger


def test_read_all_has_kent(logger):
    """
    Test on hitting People GET API, we get a user named kent in the list of people
    """
    response = client.read_all_persons()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    logger.info("User successfully read")
    assert_people_have_person_with_first_name(response, first_name='Kent')