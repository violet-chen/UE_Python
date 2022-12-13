import unreal
import random
# from imp import reload
# import showSlowTasksProgression_12 as test
# reload(test)
# test.executeSlowTask()

def executeSlowTask():
    quantity_steps_in_slow_task = 1000
    with unreal.ScopedSlowTask(quantity_steps_in_slow_task, 'My Slow Task Text ...') as slow_task:
        slow_task.make_dialog(True)
        for x in range(quantity_steps_in_slow_task):
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(1, 'My Slow Task Text ...' + str(x) + '/' + str(quantity_steps_in_slow_task))
            # Execute slow logic
            deferredSpawnActor()

def deferredSpawnActor():
    world = unreal.EditorLevelLibrary.get_editor_world()
    actor_class = unreal.EditorAssetLibrary.load_blueprint_class('/Game/MyBluePrint/BPActor')
    actor_location = unreal.Vector(random.uniform(0.0, 2000.0), random.uniform(0.0, 2000.0), 0.0)
    actor_rotation = unreal.Rotator(random.uniform(0.0, 360.0), random.uniform(0.0, 360.0), random.uniform(0.0, 360.0))
    actor_scale = unreal.Vector(random.uniform(0.1, 2.0), random.uniform(0.1, 2.0), random.uniform(0.1, 2.0))
    actor_transform = unreal.Transform(actor_location, actor_rotation, actor_scale)
    # actor = unreal.GameplayStatics.begin_deferred_actor_spawn_from_class(world, actor_class, actor_transform)
    # unreal.GameplayStatics.finish_spawning_actor(actor, actor_transform)
    actor = unreal.CppLib.get_actor(world, actor_class, actor_transform)
    unreal.CppLib.set_actor(actor,actor_transform)
