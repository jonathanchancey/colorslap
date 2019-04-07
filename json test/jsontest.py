import json
from jsoncomment import JsonComment
import pystache
from os.path import expanduser


# builds the path to the colors.json file we'll be reading from
# TODO add user config option
home = expanduser("~")
colorfile = "/.cache/wal/colors.json"
colorfile = home + colorfile

templateFile = "default.mustache"

# uses JsonComment as a our parser 
parser = JsonComment(json)
renderer = pystache.Renderer()






# try to load the colors into a dictionary
# if fails, exit with error
with open(colorfile, 'r') as fc:
    color_dict = parser.load(fc)

print(color_dict)

# create backup of original settings.json
# try to load settings.json
# if fails, exit with error
# TODO change to non dummy dir
# Should that be a user option?
with open('settings.json', 'r') as fs:
    settings_dict = parser.load(fs)

renderer.render_path(templateFile,)
print(renderer.render_path(templateFile, ))

print(settings_dict)
settings_dict["workbench.colorCustomizations"]["sideBar.background"] = color_dict["special"]["background"]
settings_dict["workbench.colorCustomizations"]["sideBar.foreground"] = color_dict["special"]["foreground"]
print(settings_dict)

# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)


# print(settings_dict['workbench.colorCustomizations']['sideBar.background'])

# try to find all entries
# if fails, appends the entries we need appropriate json section

# take the colors and set the forground background, 
# those of the sidebar, maybe the cursor.





