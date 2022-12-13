import unreal

def getAllProperties(object_class):
    return unreal.CppLib.get_all_properties(object_class)  # 通过自定义C++的类中的函数，得到所有属性的字符串列表

def printAllProperties():
    obj = unreal.Actor()  # 将打印actor类型的所有属性
    object_class = obj.get_class()
    for x in getAllProperties(object_class):
        y = x
        # while循环的作用是为了对齐字符串
        while len(y) < 42:
            y = ' ' + y
        print(y + ':' + str(obj.get_editor_property(x)))
