import logging
import pytest


logging.basicConfig(filename="test.log", level=logging.DEBUG)
def test_TheSaidTest():

    logging.warning("warning message")
    logging.info("info message")
    logging.error("error message")
    assert 5>10
    