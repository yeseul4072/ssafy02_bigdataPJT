# import crawling
# import json
# import itertools
# error_list = []
# with open('./error.txt', "r") as error_file:    
#     error_list = [code.strip() for code in error_file.readlines()]
# print(error_list)

# result = []
# for code in error_list:
#     flag = True
#     while flag:
#         try:        
#             print(code)        
#             result.append(crawling.get_child_care_detail(code))
#             flag = False
#         except Exception as e:
#             print(e)
#             flag = True
# print(result)

# with open('./error.txt', "w") as error_file:
#     print('write')

# data = []
# with open('./data.json', "r") as json_file:
#     data = json.load(json_file)
#     for res in result:
#         data.append(res)

# with open('./data.json', 'w') as json_file:
#     json.dump(data, json_file)