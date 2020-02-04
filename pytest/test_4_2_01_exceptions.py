import pytest

def test_zero_division():
    '''In order to write assertions about raised exceptions
    you can use pytest.raises as a context manager like this'''

    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_recursion_depth():
    # access to the actual exception info
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()
        f()
    print(f'--type:{excinfo.type}--value:{excinfo.value}--trackback:{excinfo.traceback[0]}---')
    # excinfo is a ExceptionInfo instance, which is a wrapper around the actual exception raised. 
    # The main attributes of interest are .type, .value and .traceback  of interest are .type, .value and .traceback.
    assert "maximum recursion" in str(excinfo.value)

def myfunc():
    raise ValueError("Exception 123 raised")
    
def test_match():
    # pass a match key word parameter to the context-manager to test that a regular expression matches on the string representation of an exception
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()

