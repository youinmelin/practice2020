#import pytest
#
#@pytest.fixture
#def smtp_connection():
#    import smtplib
#
#    return smtplib.SMTP('smtp.sina.com',25,timeout=5)

# pytest --setup-show test_5_3_fixture_conftest.py
# fixture code is in the file conftest.py
def test_ehlo(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert response == 250

def test_noop(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert b'sina' in msg
