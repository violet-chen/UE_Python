import unreal


def get_selected_actors():
    return unreal.EditorLevelLibrary.get_selected_level_actors()


def get_selected_actors_EXAMPLE():
    for x in get_selected_actors():
        print(x)


def select_actors(actors_to_select=[]):
    unreal.EditorLevelLibrary.set_selected_level_actors(actors_to_select)


def select_actors_EXAMPLE():
    all_actors = unreal.EditorLevelLibrary.get_all_level_actors()
    actors_to_select = []
    for x in range(len(all_actors)):
        actors_to_select.append(all_actors[x])
    select_actors(actors_to_select)


def clear_actor_selection_EXAMPLE():
    select_actors()
