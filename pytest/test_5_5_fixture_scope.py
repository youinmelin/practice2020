# pytest --setup-show xxx.py
import pytest

@pytest.fixture(scope='module')
#@pytest.fixture
def smtp_connection():
    import smtplib

    return smtplib.SMTP('smtp.sina.com',25,timeout=5)

def test_ehlo(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert response == 250

def test_noop(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert b'sina' in msg
