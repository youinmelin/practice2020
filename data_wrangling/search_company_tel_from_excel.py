import pandas as pd
import pprint


def search_company_tel_from_execl():
    path = 'data_source/'
    filename = '7月未申报0716.xlsx'
    df = pd.read_excel(path + filename)
    # data_list = df.to_dict(orient='records')
    data_list = df.to_dict()
    pprint.pprint(data_list)


if __name__ == '__main__':
    search_company_tel_from_execl()