# pytest --setup-show xxx.py
# pytest -s -q --tb=no xxx.py
# Fixture functions can accept the request object to introspect the “requesting” test function, class or module context.
import pytest
import smtplib

@pytest.fixture(scope='module')
#@pytest.fixture
def smtp_connection(request):
    print(request)
    print(dir(request.module))
    server = getattr(request.module,'smtpserver','smtp.sina.com')
    print(server)

    with smtplib.SMTP('smtp.sina.com',25,timeout=5) as smtp_connection:
        yield smtp_connection  # provide the fixture value
    print('finalizing {} ({})'.format(smtp_connection,server))
    smtp_connection.close()
     
smtpserver = 'mail.python.org'

def test_ehlo(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert response == 250

def test_noop(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert b'sina' in msg
