# pytest --setup-show xxx.py
# pytest -s -q --tb=no xxx.py
# pytest --collect-only test_5_11_fixture_parametrize.py
# Fixture functions can accept the request object to introspect the “requesting” test function, class or module context.
import pytest
import smtplib

#@pytest.fixture(scope='module')
@pytest.fixture(scope='module',params=['smtp.sina.com','mail.python.org'],ids=['sina','python'])
#@pytest.fixture
def smtp_connection(request):
    print(request)
    print(request.module)
    server = getattr(request.module,'smtpserver','smtp.sina.com')
    print(server)

    with smtplib.SMTP(request.param,25,timeout=5) as smtp_connection:
        yield smtp_connection  # provide the fixture value
    print('finalizing {})'.format(smtp_connection))
    smtp_connection.close()
     
#smtpserver = 'mail.python.org'

def test_ehlo(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert response == 250
    assert b'python' in msg

def test_noop(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert response == 250
    assert b'sina' in msg
