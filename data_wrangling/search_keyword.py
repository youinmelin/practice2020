#coding=utf-8

# 寻找对应的表头
def search_keyword(origin_list, keywords_list):
    header_list = [header for header in origin_list[0]]
    for header_k in header_list:
        for k in keywords_list:
            if header_k == k:
                return k

if __name__ == '__main__':
    origin_list = [{'id': 3, '纳税人识别号': '9111011404V10X', '企业名称': '企业3', '主管税务局': '国家税务总局北京市海淀区区税务局', '主管税务所': '海淀税务所'}, {'id': 2, '纳税人识别号': '9111011404VX', '企业名称': '企业2', '主管税务局': '国家税务总局北京市昌平区税务局', '主管税务所': '沙河所'}, {'id': 1, '纳税人识别号': '91110114005X', '企业名称': '企业1', '主管税务局': '国家税务总局北京市昌平税务局', '主管税务所': '第一税务所'}, {'id': 5, '纳税人识别号': '911101140055', '企业名称': '企业4', '主管税务局': '国家税务总局北京市昌平区税务局', '主管税务所': '沙河税务所'}, {'id': 4, '纳税人识别号': '911101140056', '企业名称': '企业4', '主管税务局': '国家税务总局北京市昌平区税务局', '主管税务所': '沙河税务所'}, {'id': 6, '纳税人识别号': '91110114009X', '企业名称': '企业5', '主管税务局': '国家税务总局北京市顺义区税务局', '主管税务所': '南法信税务所'}]
    list_taxpayer_number_keywords = ['纳税人识别号', '纳税识别号', '纳税人识别码', '纳税人识别码', '信用代码', '纳税人信用代码']
    list_master_keywords = ['主管税务局', '主管税务所', '主管干部', '主管科室']
    print(search_keyword(origin_list, list_master_keywords))
    print(search_keyword(origin_list, list_taxpayer_number_keywords))

