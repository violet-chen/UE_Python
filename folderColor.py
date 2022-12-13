# coding: utf-8

import unreal


# import folderColor as fc
# from imp import reload
# reload(fc)
# fc.generateColoredDirectories()

def generateColoredDirectories():
    for x in range(100, 400):
        dir_path = '/Game/PythonGenerated/' + str(x)
        linear_color = getGradientColor(x)
        unreal.CppLib.set_folder_color(dir_path, linear_color)
        unreal.EditorAssetLibrary.make_directory(dir_path)


def getGradientColor(x):
    x = x - 100
    if x < 100:
        r = 1.0 - x / 100.0
        g = 0.0 + x / 100.0
        b = 0.0
    elif x < 200:
        r = 0.0
        g = 1.0 - (x - 100) / 100.0
        b = 0.0 + (x - 100) / 100.0
    else:
        r = 0.0 + (x - 200) / 100.0
        g = 0.0
        b = 1.0 - (x - 200) / 100.0
    return unreal.LinearColor(r, g, b, 1)
