# 1.5 Group multiple tests in a class

class TestClass():
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello test'
        # the function hasattr judge if the attribute is in the object
        assert hasattr(x,'split')
