import json
from jsoncomment import JsonComment


# Serialized JSON data written to a native Python str object.
# json_string = json.dumps(data)

# with open('distros.json', 'r') as f:
#     distros_dict = json.load(f)

# for distro in distros_dict:
#     print(distro['Name'])

with open('settings.json', 'r') as f:
    settings_dict = json.load(f)

print(settings_dict['workbench.colorCustomizations']['sideBar.background'])

