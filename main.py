import keyboard
import pymem
from pymem import process
import time
from offsets import *

_process = pymem.Pymem("csgo.exe")
_client = pymem.process.module_from_name(_process.process_handle, "client.dll").lpBaseOfDll


def BHOP():
    while True:
        try:
            if keyboard.is_pressed("space"):
                player = _process.read_int(_client + dwLocalPlayer)
                jump = _client + dwForceJump
                player_state = _process.read_int(player + m_fFlags)

                if player_state == 257 or player_state == 263:  # 257 - player on ground, 263 - crouch
                    _process.write_int(jump, 5)
                    time.sleep(0.1)  # Чем меньше задержка - тем лучше bhop, но большая нагрузка на процессор
                    _process.write_int(jump, 4)
        except pymem.exception.MemoryReadError:
            pass


BHOP()
