CONTENT = 'content'


def test_create_file(tmp_path):
    # tmp_path : Return a temporary directory path object
    # Path对象可以使用/操作符代替常用的os.path.join()的方法
    d = tmp_path / 'sub'
    print('\ntmp_path:',tmp_path)
    print('d:',type(d))
    d.mkdir()
    p = d / 'hello.txt'  # p: <class 'pathlib.WindowsPath'>
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    # assert 0
