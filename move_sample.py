from caoprov_denso_rc9 import RC9
import time

RC9_PROJ_PATH = "RCPJ=C:\\Users\\ijiwa\\Documents\\WINCAPSIII\\VS050_RC9\\VS050_RC9\\default.rcpj"

rc9 = RC9(RC9_PROJ_PATH)
rc9.take_arm()

curpos = rc9.curpos()
print(f"Current pose: {curpos}")

print("Motor ON")
rc9.motor_on()

print("Move P0 (Initial pose)")
rc9.move("@P P0", 1, "")
time.sleep(1.0)

print("Move P1")
rc9.move("@P P1", 1, "")
time.sleep(2.0)

print("Move P0 (Initial pose)")
rc9.move("@P P0", 1, "")

rc9.give_arm()
