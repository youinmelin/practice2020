import pytest

@pytest.fixture(scope='module')
def smtp_connection():
    import smtplib

    return smtplib.SMTP('smtp.sina.com',25,timeout=5)
