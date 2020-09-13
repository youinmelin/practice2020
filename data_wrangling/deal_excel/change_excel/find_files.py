import os

"""
    
    os.walk(top, topdown=True, onerror=None, followlinks=False)
    我们一般只使用第一个参数。（topdown指明遍历的顺序）
    该方法对于每个目录返回一个三元组，(dirpath, dirnames, filenames)。
    第一个是路径，第二个是路径下面的目录，
    第三个是路径下面的非目录（对于windows来说也就是文件）
"""


def pick_file(key_word=''):
    """
    find files in current path(includes subfolders) by name
    支持模糊查询 fuzzy query

    :param key_word: default is '', all files
    :return:
    """
    walk_files = os.walk('.')
    files_list = []
    # add all files name in files_list
    for root, path, files in walk_files:
        for filename in files:
            if key_word in filename:
                files_list.append(root+'/'+filename)
                # files_list.append(filename)
    print(files_list)
    for i, filename in enumerate(files_list):
        print('%d: %s' % (i, filename))
    num = input('请输入要操作的文件序号：')
    num = int(num)
    print('您输入的是：', num)
    print('文件名:', files_list[num])
    return files_list[num]


if __name__ == '__main__':
    pick_file()
