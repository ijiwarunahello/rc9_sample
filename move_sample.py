from controller import RC9
from move_option import MoveOption
from common import (
    RC9_PROJ_PATH,
    POSITION,
    FIG,
    convert_posedata,
)
import time

rc9 = RC9(RC9_PROJ_PATH)
move_option = MoveOption()

rc9.take_arm()

curpos = rc9.curpos()
print(f"Current pose: {curpos}")

print("Motor ON")
rc9.motor_on()

print("Move P0 (Initial pose)")
ret = move_option.generate()
rc9.move("@P P0", 1, ret)
time.sleep(1.0)

print("Move P1")
move_option.set_speed(10.0)
ret = move_option.generate()
print(ret)
rc9.move("@P P1", 1, ret)
time.sleep(2.0)

print(f"Move {POSITION}")
move_option.set_speed(100.0)
ret = move_option.generate()
posedata = convert_posedata(POSITION)
rc9.move(f"@P {posedata}", 1, ret)
time.sleep(1.0)

print("Move P0 (Initial pose)")
ret = move_option.generate()
rc9.move("@P P0", 1, ret)

rc9.give_arm()
