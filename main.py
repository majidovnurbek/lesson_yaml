# import yaml
# data = {
#     'Name': 'John Doe',
#     'Position': 'DevOps Engineer',
#     'Location': 'England',
#     'Age': '26',
#     'Experience': {'GitHub': 'Software Engineer', \
#                    'Google': 'Technical Engineer', 'Linkedin': 'Data Analyst'},
#     'Languages': {'Markup': ['HTML'], 'Programming' \
#         : ['Python', 'JavaScript', 'Golang']}
# }
# data_yaml = yaml.dump(data)
# print(data_yaml, type(data_yaml))
############################################################################
import yaml
data = {
    'Name': 'John Doe',
    'Position': 'DevOps Engineer',
    'Location': 'England',
    'Age': '26',
    'Experience': {'GitHub': 'Software Engineer', \
                   'Google': 'Technical Engineer', 'Linkedin': 'Data Analyst'},
    'Languages': {'Markup': ['HTML'], 'Programming' \
        : ['Python', 'JavaScript', 'Golang']}
}
with open("data_yaml","w") as file_yaml:
    yaml.dump(data,file_yaml)
def
    with open("data_yaml","r") as file_yaml:
        data = yaml.safe_load(file_yaml)
        print(data)


