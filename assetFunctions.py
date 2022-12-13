import unreal

soundPath = 'D:/ZhangRuiChen/UETest/TestFile/Sounds/soundTest.mp3'
texPath = 'D:/ZhangRuiChen/UETest/TestFile/Texture/test_ORM3.png'
static_mesh_fbx = 'D:/ZhangRuiChen/UETest/TestFile/StaticMeshes/sphere.fbx'
skeletal_mesh_fbx = 'D:/ZhangRuiChen/UETest/TestFile/Skeletal/man.fbx'


# from imp import reload
# import assetFunctions
# reload(assetFunctions)
# assetFunctions.importMyAssets()


def importMyAssets():  # 创建导入任务并执行导入
    # texture_task = buildImportTask(texPath, '/Game/Textures')  # 通过buildImportTask函数创建一个AssetImportTask对象
    # sound_task = buildImportTask(soundPath, '/Game/Sounds')  # 同理
    # executeImportTasks([texture_task, sound_task])  # 执行导入操作
    static_mesh_task = buildImportTask(static_mesh_fbx, '/Game/MyAsset/StaticMeshes', buildStaticMeshImportOptions())
    skeletal_mesh_task = buildImportTask(skeletal_mesh_fbx, '/Game/MyAsset/SkeletalMeshes',
                                         buildSkeletalMeshImportOptions())
    executeImportTasks([static_mesh_task, skeletal_mesh_task])


def importAnimation():  # 创建导入任务并执行导入
    animation_fbx = 'D:/ZhangRuiChen/UETest/TestFile/Animation/Animation.fbx'
    animation_fbx_task = buildImportTask(animation_fbx, '/Game/MyAsset/Animations',
                                         buildAnimationImportOptions('/Game/MyAsset/SkeletalMeshes/man_Skeleton'))
    executeImportTasks([animation_fbx_task])


# 这里用到的属性可以参考文档：https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/AssetImportTask.html
def buildImportTask(filename, destination_path, options=None):  # 构建导入任务
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)  # 设置为True后就不会弹出对话框，就是将其设置为自动化
    task.set_editor_property('destination_name', '')  # 可选的要导入的自定义名称，当属性为空时就按照文件名称命名
    task.set_editor_property('destination_path', destination_path)  # 导入的资源在引擎中的路径
    task.set_editor_property('filename', filename)  # 要导入的资源在电脑磁盘上的路径
    task.set_editor_property('replace_existing', True)  # 是否要覆盖资产
    task.set_editor_property('save', True)  # 导入后保存
    task.set_editor_property('options', options)  # 当导入fbx这种资产需要额外的导入选项，需要创建FbxImportUI对象来传递
    return task


# 这里用到的属性可以参考文档：https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/AssetTools.html
def executeImportTasks(tasks):  # 执行导入任务
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)  # 通过这行代码将在buildImportTask函数中创建的task对象进行导入
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            print('Imported: %s' % path)


def buildStaticMeshImportOptions():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', False)  # Static Mesh
    # unreal.FbxMeshImportData
    options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
    # unreal.FbxStaticMeshImportData
    options.static_mesh_import_data.set_editor_property('combine_meshes', True)
    options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
    options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)
    return options


def buildSkeletalMeshImportOptions():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', True)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', True)  # Skeletal Mesh
    # unreal.FbxMeshImportData
    options.skeletal_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
    # unreal.FbxSkeletalMeshImportData
    options.skeletal_mesh_import_data.set_editor_property('import_morph_targets', True)
    options.skeletal_mesh_import_data.set_editor_property('update_skeleton_reference_pose', False)
    return options


# 动画的导入设置选项
def buildAnimationImportOptions(skeleton_path):
    options = unreal.FbxImportUI()

    # 是否导入动画
    options.set_editor_property('import_animations', True)
    # 导入骨架的位置
    options.skeleton = unreal.load_asset(skeleton_path)

    # 设置动画序列的内容
    options.anim_sequence_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.anim_sequence_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.anim_sequence_import_data.set_editor_property('import_uniform_scale', 1.0)

    # 动画的长度
    options.anim_sequence_import_data.set_editor_property('animation_length',
                                                          unreal.FBXAnimationLengthImportType.FBXALIT_EXPORTED_TIME)
    # 去掉冗余的关键帧
    options.anim_sequence_import_data.set_editor_property('remove_redundant_keys', False)
    return options


# import AssetFunction_3 as af
# reload(af)
# af.createDirectory()

# 创建文件夹
def createDirectory():
    unreal.EditorAssetLibrary.make_directory('/Game/MyAsset/MyNewDirectory')


# 复制文件夹
def duplicateDirectory():
    return unreal.EditorAssetLibrary.duplicate_directory('/Game/MyAsset/MyNewDirectory',
                                                         '/Game/MyAsset/MyNewDirectory_Duplicated')


# 删除文件夹
def deleteDirectory():
    unreal.EditorAssetLibrary.delete_directory('/Game/MyAsset/MyNewDirectory')


# 重命名文件夹
def renameDirectory():
    return unreal.EditorAssetLibrary.rename_directory('/Game/MyAsset/MyNewDirectory_Duplicated',
                                                      '/Game/MyAsset/MyNewDirectory_Renamed')


# 复制资产
def duplicateAsset():
    return unreal.EditorAssetLibrary.duplicate_asset('/Game/MyAsset/Textures/test_ORM3',
                                                     '/Game/MyAsset/Textures/test_ORM3_duplicate')


# 删除资产
def deleteAsset():
    unreal.EditorAssetLibrary.delete_asset('/Game/MyAsset/Textures/test_ORM3')


# 判断资产是否存在
def assetExist():
    print(unreal.EditorAssetLibrary.does_asset_exist('/Game/MyAsset/Textures/test_ORM3'))  # False
    print(unreal.EditorAssetLibrary.does_asset_exist('/Game/MyAsset/Textures/test_ORM3_duplicate'))  # True


# 重命名资产
def renameAsset():
    unreal.EditorAssetLibrary.rename_asset('/Game/MyAsset/Textures/test_ORM3_duplicate',
                                           '/Game/MyAsset/Textures/test_ORM3_Renamed')


# 显示复制资产提示框
def duplicateAssetDialog(show_dialog=True):
    if show_dialog:
        unreal.AssetToolsHelpers.get_asset_tools().duplicate_asset_with_dialog('test_ORM3_Duplicated',
                                                                               '/Game/MyAsset/Textures',
                                                                               unreal.load_asset(
                                                                                   '/Game/MyAsset/Textures/test_ORM3_Renamed'))
    else:
        unreal.AssetToolsHelpers.get_asset_tools().duplicate_asset('test_ORM3_Duplicated', '/Game/MyAsset/Textures',
                                                                   unreal.load_asset(
                                                                       '/Game/MyAsset/Textures/test_ORM3_Renamed'))


# 显示重命名提示框
def renameAssetDialog(show_dialog=True):
    first_rename_data = unreal.AssetRenameData(unreal.load_asset('/Game/MyAsset/Textures/test_ORM3_Renamed'),
                                               '/Game/MyAsset/Textures', 'test_ORM3_Renamed_2')
    second_rename_data = unreal.AssetRenameData(unreal.load_asset('/Game/MyAsset/Textures/test_ORM3_Duplicated'),
                                                '/Game/MyAsset/Textures', 'test_ORM3_Duplicated_Renamed')
    if show_dialog:
        unreal.AssetToolsHelpers.get_asset_tools().rename_assets_with_dialog([first_rename_data, second_rename_data])
    else:
        unreal.AssetToolsHelpers.get_asset_tools().rename_assets([first_rename_data, second_rename_data])


# UE官方教程中的代码：
# 列举路径下的所有文件路径
def listAssetPaths(path='/Game'):
    assetPaths = unreal.EditorAssetLibrary.list_assets(path)
    for assetPath in assetPaths: print(assetPath)


# 得到选择的资产的路径
def getSelectionContentBrowser():
    selectAssets = unreal.EditorUtilityLibrary.get_selected_assets()
    for selectAsset in selectAssets: print(selectAsset)


# 得到关卡中所有的Actor
def getAllActors():
    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    for actor in actors: print(actor)


# 得到关卡中选择的Actor
def getSelectActors():
    actors = unreal.EditorLevelLibrary.get_selected_level_actors()
    for actor in actors: print(actor)


# 根据类型列举物体
def getAssetClass(classType):
    assetPaths = unreal.EditorAssetLibrary.list_assets('/Game')
    # print(assetPaths)
    assets = []
    for assetPath in assetPaths:
        assetData = unreal.EditorAssetLibrary.find_asset_data(assetPath)
        assetClass = assetData.asset_class
        if assetClass == classType:
            assets.append(assetData.get_asset())
    # for asset in assets: print(asset)
    return assets


# 获取静态网格体的信息
def getStaticMeshData():
    staticMeshs = getAssetClass('StaticMesh')  # 获取所有类型为StaticMesh的对象
    for staticMesh in staticMeshs:
        # assetImportData = staticMesh.get_editor_property('asset_import_data')  # 获取静态网格体对象的编辑器中的导入信息的属性
        # fbxFilePath = assetImportData.extract_filenames()  # 得到导入信息属性中的fbx路径
        # print(fbxFilePath)
        # print(staticMesh.get_editor_property('lod_group'))
        # print(staticMesh.get_num_lods())
        # 如果静态网个体对象的lod组的属性为None并且lod数量只有一个时将lod组的属性改为LargeProp
        if staticMesh.get_editor_property('lod_group') == 'None':
            if staticMesh.get_num_lods() == 1:
                staticMesh.set_editor_property('lod_group', 'LargeProp')


# 获取静态网格体的lod信息
def getStaticMeshLODData():
    staticMeshs = getAssetClass('StaticMesh')
    staticMeshLODData = []
    for staticMesh in staticMeshs:
        staticMeshTriCount = []  # 负责记录模型的三角形数量
        numLODs = staticMesh.get_num_lods()
        for i in range(numLODs):
            LODTriCount = 0  # 记录当前LOD的三角形数量
            numSections = staticMesh.get_num_sections(i)
            for j in range(numSections):  # 遍历LOD对应的分段得到LOD对应的三角形数量
                # 得到静态网格体对应的分段信息
                sectionData = unreal.ProceduralMeshLibrary.get_section_from_static_mesh(staticMesh, i, j)
                sectionTriCount = (len(sectionData[1]) / 3)  # 把数组的长度除以3以后才能够得到我们需要的正确的三角形的数量。
                LODTriCount += sectionTriCount
            staticMeshTriCount.append(LODTriCount)  # 记录LOD对应的三角形数量
        staticMeshReductions = [100]  # 负责记录模型的LOD对应的三角形百分比
        for i in range(1, numLODs):
            staticMeshReductions.append(int(staticMeshTriCount[i] / staticMeshTriCount[0] * 100))
        # print(staticMesh.get_name())
        # print(staticMeshTriCount)
        # print(staticMeshReductions)

        try:
            LODData = (staticMesh.get_name(), staticMeshTriCount[1])  # 之所以try是因为有的模型只有LOD0,把只有LOD0的过滤掉
        except:
            pass
        staticMeshLODData.append(LODData)
    return staticMeshLODData


# 获取关卡中的模型以及出现的次数
def getStaticMeshInstanceCounts():
    levelActors = unreal.EditorLevelLibrary().get_all_level_actors()  # 获取关卡中的所有Actor

    staticMeshActors = []  # 负责记录所有staticMeshActor的名字
    staticMeshActorCounts = []  # 负责记录所有Actor在关卡中出现的数量

    for levelActor in levelActors:
        if (levelActor.get_class().get_name()) == 'StaticMeshActor':
            staticMeshComponent = levelActor.static_mesh_component  # 得到这个Actor的组件
            staticMesh = staticMeshComponent.static_mesh  # 得到这个组件对应的静态网格体
            staticMeshActors.append(staticMesh.get_name())

    processedActors = []  # 用来记录场景中的所有staticMeshActor但是不会出现相同的名字
    for staticMeshActor in staticMeshActors:
        if staticMeshActor not in processedActors:
            actorCounts = (staticMeshActor, staticMeshActors.count(staticMeshActor))  # 元组，负责记录actor以及对应的关卡出现数量
            staticMeshActorCounts.append(actorCounts)
            processedActors.append(staticMeshActor)
    # key=lambda a: a[1]  的意思是按照列表中的元素中的第二项进行排列，在这里是按照actor出现的次数进行排序
    staticMeshActorCounts.sort(key=lambda a: a[1], reverse=True)
    # for item in staticMeshActorCounts: print(item)

    LODData = getStaticMeshLODData()

    # for item in LODData: print(item)

    aggregateTriCounts = []

    for i in range(len(staticMeshActorCounts)):
        for j in range(len(LODData)):
            if staticMeshActorCounts[i][0] == LODData[j][0]:
                aggregateTriCount = (staticMeshActorCounts[i][0], staticMeshActorCounts[i][1] * LODData[j][1])
                aggregateTriCounts.append(aggregateTriCount)

    aggregateTriCounts.sort(key=lambda a: a[1], reverse=True)  # 存取场景中的actor的mesh名字以及对应的场景中的所有mesh的LOD1的三角形数量
    for item in aggregateTriCounts: print(item)


def returnMaterialInformationSMC():
    levelActors = unreal.EditorLevelLibrary().get_all_level_actors()
    testMat = unreal.EditorAssetLibrary.find_asset_data('/Game/python/MI_test').get_asset()

    for levelActor in levelActors:
        if (levelActor.get_class().get_name()) == 'StaticMeshActor':
            staticMeshComponent = levelActor.static_mesh_component

            for i in range(staticMeshComponent.get_num_materials()):
                staticMeshComponent.set_material(i, testMat)


# 创建基础资产
def create_generic_asset(asset_path='', unique_name=True, asset_class=None, asset_factory=None):
    if unique_name:  # 如果命名冲突的话会自动生成一个新的唯一的路径名字(后缀加数字)
        asset_path, asset_name = unreal.AssetToolsHelpers.get_asset_tools().create_unique_asset_name(
            base_package_name=asset_path, suffix='')
    if not unreal.EditorAssetLibrary.does_asset_exist(asset_path=asset_path):
        path = asset_path.rsplit('/', 1)[0]
        name = asset_path.rsplit('/', 1)[1]
        return unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=name,
            package_path=path,
            asset_class=asset_class,
            factory=asset_factory
        )
    return unreal.load_asset(asset_path)


# 调用创建基础资产的举例
def create_generic_asset_EXAMPLE():
    base_path = '/Game/GenericAssets/'
    generic_assets = [
        [
            base_path + 'sequence',
            unreal.LevelSequence,
            unreal.LevelSequenceFactoryNew()
        ],
        [
            base_path + 'material',
            unreal.Material,
            unreal.MaterialFactoryNew()
        ],
        [
            base_path + 'world',
            unreal.World,
            unreal.WorldFactory()
        ],
        [
            base_path + 'particle_system',
            unreal.ParticleSystem,
            unreal.ParticleSystemFactoryNew()
        ],
        [
            base_path + 'paper_flipbook',
            unreal.PaperFlipbook,
            unreal.PaperFlipbookFactory()
        ]
    ]
    for asset in generic_assets:
        print(create_generic_asset(asset[0], True, asset[1], asset[2]))
