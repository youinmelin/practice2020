from fuzzywuzzy import fuzz
from fuzzywuzzy import process

str_a1 = 'hello the world'
str_a2 = 'heel0 the world'
str_a3 = 'the world hello'
str_b1 = '北京市昌平区税务局'
str_b2 = '北京市昌平税务局'
str_c1 = '纳税人识别号'
str_c2 = '纳税识别号'

print('# fuzz.ratio: compare to different str how likely')
print(str_a1, 'vs', str_a2, ':', fuzz.ratio(str_a1, str_a2))
print(str_a1, 'vs', str_a3, ':', fuzz.ratio(str_a1, str_a3))
print(str_b1, 'vs', str_b2, ':', fuzz.ratio(str_b1, str_b2))
print(str_c1, 'vs', str_c2, ':', fuzz.ratio(str_c1, str_c2))

print('# fuzz.partial_ratio: compare to different str how likely')
print(str_a1, 'vs', str_a2, ':', fuzz.partial_ratio(str_a1, str_a2))
print(str_a1, 'vs', str_a3, ':', fuzz.partial_ratio(str_a1, str_a3))
print(str_b1, 'vs', str_b2, ':', fuzz.partial_ratio(str_b1, str_b2))
print(str_c1, 'vs', str_c2, ':', fuzz.partial_ratio(str_c1, str_c2))

print('# fuzz.token_sort_ratio: compare to different str do not consider sort')
print(str_a1, 'vs', str_a2, ':', fuzz.token_sort_ratio(str_a1, str_a2))
print(str_a1, 'vs', str_a3, ':', fuzz.token_sort_ratio(str_a1, str_a3))

print('# fuzz.token_set_ratio: compare to different str compare set')
print(str_a1, 'vs', str_a2, ':', fuzz.token_set_ratio(str_a1, str_a2))
print(str_a1, 'vs', str_a3, ':', fuzz.token_set_ratio(str_a1, str_a3))
print(str_b1, 'vs', str_b2, ':', fuzz.token_set_ratio(str_b1, str_b2))
print(str_c1, 'vs', str_c2, ':', fuzz.token_set_ratio(str_c1, str_c2))

choices = ['Yes', 'No', 'Maybe', 'N/A']
key_words = ['主管税务局','主管税务所','主管干部','主管科室']
print(process.extract('ya', choices, limit=4))
print(process.extractOne('ya',choices))
print(process.extract('nope', choices, limit=4))
print(process.extractOne('nope',choices))
print(process.extract('管理税务所', key_words))
print(process.extract('管理所', key_words))
print(process.extractOne('00', key_words))


