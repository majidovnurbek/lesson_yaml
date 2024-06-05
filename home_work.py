# import yaml
# data = {
#     "ism": "nurbek",
#     "age": 16,
#     "location": {
#         "shahar": "tashkent",
#         "tuman": "sergeli",
#     },
#     "telephon": {
#         "turi": 'mobil',
#         "number": 555555555,
#         "turi": "is",
#         "number2": 555555555,
#     },
#
#     "kundalik_chiqishlari": {
#         "day": "dushanba",
#         "time": "8:00"
#     }
#
# }
# with open("private.yaml","w") as file_yaml:
#     yaml.dump(data,file_yaml)
# "ism": "nurbek",
# "age": 16,
# 'Location': {"shahar": "tashkent", \
#              "tuman": "sergeli"},
#
# 'telephone': {'turi': 'mobil', \
#               'nunber': 55555555, 'turi': "is", 'number2': 555555555},
# "kundalik_chiqishlari": {"day": "dushanba", \
#                          "time": "8:00"}
# import yaml
# data = {
#
#     "ism": "nurbek",
#     "age": 16,
#     'Location': {"city": "tashkent",\
#                  "region": "sergeli"},
#     'telephone': {'turi': 'mobile', \
#                    'number': 555555, 'number2': 444444},
#     'kundalik_chiqishlari': {'day': 'dushanba',\
#                                     "time": "8:00"}
# }
# with open("private.yaml","w") as file_yaml:
#     yaml.dump(data,file_yaml)
import yaml
# datas = {
#
#     "ism": "nurbek",
#     "age": 16,
#     'Location': {"city": "tashkent",\
#                  "region": "sergeli"},
#     'telephone': {'turi': 'mobile', \
#                    'number': 555555, 'number2': 444444},
#     'kundalik_chiqishlari': {'day': 'dushanba',\
#                                     "time": "8:00"}
# }
# import yaml
# def home_work(data_yaml):
#     with open("data_yaml", "r") as file_yaml:
#         data = yaml.safe_load(file_yaml)
#         return data
#
# datass = home_work('private.yaml')
# print(datass)

import yaml


class HomeWork:
    def __init__(self, home_work):
        self.home_work = home_work

    def read_home(self):
        with open(self, home_work, "r") as file:
            data = yaml.safe_load(file)
            return data


read = HomeWork(home_work)
print(read.read_home())
