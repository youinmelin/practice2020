import os


def add_filename_on_last(origin_name, add_name):
    """
    add string between filename and suffix name
    :param origin_name:
    :param add_name: the string which do you want to add
    :return: new file name
    """
    prefix_filename = os.path.splitext(origin_name)[0]
    suffix_filename = os.path.splitext(origin_name)[1]
    new_file_name = prefix_filename + add_name + suffix_filename
    return new_file_name


def add_filename_on_first(origin_name, add_name):
    """
    add string before filename
    :param origin_name:
    :param add_name: the string which do you want to add
    :return: new file name
    """
    prefix_filename = os.path.splitext(origin_name)[0]
    suffix_filename = os.path.splitext(origin_name)[1]
    new_file_name = add_name + prefix_filename + suffix_filename
    return new_file_name


def change_suffix(origin_name, new_suffix):
    """
    change the suffix name
    :param origin_name:
    :param new_suffix:
    :return: new file name
    """
    prefix_filename = os.path.splitext(origin_name)[0]
    # suffix_filename = os.path.splitext(origin_name)[1]
    new_file_name = prefix_filename + new_suffix
    return new_file_name
