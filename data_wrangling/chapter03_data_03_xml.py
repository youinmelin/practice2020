from xml.etree import ElementTree as ET

path = "book/data/chp3/"
filename = "data-text.xml"

tree = ET.parse(path + filename)
root = tree.getroot()
data = root.find('Data')

all_data_list = []
for observation in data:
    # print(type(observation))
    for item in observation:
        record_dict = {}
        # dim_list = item.findall('Dim')
        key = list(item.attrib.keys())
        # print (key[0])
        value = list(item.attrib.values())
        record_dict[key[0]] = value[0]
        all_data_list.append (record_dict)
    # break
print (all_data_list)

