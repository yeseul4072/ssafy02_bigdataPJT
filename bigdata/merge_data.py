# import os
# import json
# import itertools

# file_list = set([file_name for file_name in os.listdir('./') if len(file_name.split('.')) > 1 and file_name.split('.')[1] == 'json'])
# data = []
# for file_name in file_list:
#     with open("./{file_name}".format(file_name=file_name), "r") as json_file:
#         data.append(json.load(json_file))
#         print(len(data[-1]))
# data = list(itertools.chain.from_iterable(data))

# with open("./data.json", "w") as json_file:
#     json.dump(data, json_file)