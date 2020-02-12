# pytest --setup-show xxx.py
# pytest -s -q --tb=no test_5_7_fixture_yield.py

import pytest
import smtplib

#@pytest.fixture(scope='module')
@pytest.fixture
#@pytest.fixture
def smtp_connection():
    with smtplib.SMTP('smtp.sina.com',25,timeout=5) as smtp_connection:
        yield smtp_connection  # provide the fixture value
    print('teardown smtp')
    smtp_connection.close()
     
def test_ehlo(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert response == 250

def test_noop(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert b'sina' in msg
