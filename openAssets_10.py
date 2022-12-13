import unreal
# 在ue中执行的调用命令
# from imp import reload
# import openAssets_10 as oa
# reload(oa)
# oa.openAssets()

# 打开资产
def openAssets():
    assets = [unreal.load_asset('/Game/MyAsset/Sounds/soundTest'),
              unreal.load_asset('/Game/MyAsset/Textures/light_setAOVs'),
              unreal.load_asset('/Game/MyAsset/Textures/light_createShot'),
              unreal.load_asset('/Game/MyAsset/Textures/light_importLight')]
    unreal.AssetToolsHelpers.get_asset_tools().open_editor_for_assets(assets)

# 调用自定义的C++类中的函数
def getAllOpenedAssets():
    return unreal.CppLib.get_assets_opened_in_editor()

def closeAssets():
    assets = getAllOpenedAssets()
    unreal.CppLib.close_editor_for_assets(assets)