import win32com.client
import time

eng = win32com.client.Dispatch("CAO.CaoEngine")

ctrl = eng.Workspaces(0).AddController("RC9", "CaoProv.DENSO.RC9", "", "RCPJ=C:\\Users\\ijiwa\\Documents\\WINCAPSIII\\VS050_RC9\\VS050_RC9\\default.rcpj")
# ctrl = eng.Workspaces(0).AddController("RC9", "CaoProv.DENSO.RC9", "", "Server=127.0.0.1")
Arm1 = ctrl.AddRobot("Arm1", "")

Arm1.Execute("TakeArm", 0)

res = Arm1.Execute("CurPos", "")
print(f"Current pose: {res}")

print("Motor ON")
Arm1.Execute("Motor", [1, 0])

print("Move P0 (Initial pose)")
Arm1.Move(1, "@P P0", "")
time.sleep(1.0)

print("Move P1")
Arm1.Move(1, "@P P1", "")
time.sleep(2.0)

print("Move P0 (Initial pose)")
Arm1.Move(1, "@P P0", "")

Arm1.Execute("GiveArm", "")
