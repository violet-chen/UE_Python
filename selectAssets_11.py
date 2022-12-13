import unreal
# from imp import reload
# import selectAssets_11 as sa
# reload(sa)
# sa.showAssetsInContentBrowser()
def showAssetsInContentBrowser():
    paths = ['/Game/MyAsset/Sounds/SoundTest',
             '/Game/MyAsset/Textures/light_setAOVs']
    unreal.EditorAssetLibrary.sync_browser_to_objects(paths)

def getSelectedAssets():
    return unreal.CppLib.get_selected_assets()

def setSelectedAssets():
    paths = ['/Game/StarterContent/Maps/Advanced_Lighting',
             '/Game/MyAsset/Sounds/soundTest']
    return unreal.CppLib.set_selected_assets(paths)

def getSelectedFolders():
    return unreal.CppLib.get_selected_folders()

def setSelectedFolders():
    paths = ['/Game/MyAsset/Sounds',
             '/Game/MyAsset/Textures']
    return unreal.CppLib.set_selected_folders(paths)
