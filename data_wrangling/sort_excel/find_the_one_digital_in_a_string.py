def find_the_one_digital_in_str(origin_str, number=-1):
    """
     find_the_digital_from_str
    :param origin_str:
    :param number: which number of the digital do you want, the first is zero, the last is -1
    :return: one digital in the str you want
    """
    list_digitals = [i for i in origin_str if i.isdigit()]
    the_digital = list_digitals[number]
    return the_digital


if __name__ == '__main__':
    origin_str = '123456e'
    print(find_the_one_digital_in_str(origin_str))
