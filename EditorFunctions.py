import unreal
import random


def executeConsoleCommand():
    console_cmd = ['r.ScreenPercentage 0.1',
                   'r.Color.Max 6',
                   'stat fps',
                   'stat unit']
    for x in console_cmd:
        unreal.CppLib.execute_console_command(x)
