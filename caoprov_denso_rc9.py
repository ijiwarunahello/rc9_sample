import win32com.client


class RC9:
    DISPATCH = "CAO.CaoEngine"
    PROV = "CaoProv.DENSO.RC9"
    def __init__(self, option, name="RC9") -> None:
        self.option = option
        self.name = name
        self.is_take_arm = False

        self.initialize()

    def initialize(self):
        self.eng = win32com.client.Dispatch(self.DISPATCH)
        self.ctrl = self.eng.Workspaces(0).AddController(
            self.name, self.PROV, "", self.option
        )
        self.arm = self.ctrl.AddRobot("arm", "")

    def take_arm(self):
        if not self.is_take_arm:
            self.arm.Execute("TakeArm", 0)
            print("TakeArm")
            self.is_take_arm = True
        else:
            print("TakeArm already done.")

    def give_arm(self):
        if self.is_take_arm:
            self.arm.Execute("GiveArm", "")
            print("GiveArm")
            self.is_take_arm = False
        else:
            print("Doesn't have TakeArm")

    def _motor(self, cond, wait=True):
        option = [cond, 0 if wait else 1]
        self.arm.Execute("Motor", option)

    def motor_on(self):
        self._motor(1)

    def motor_off(self):
        self._motor(0)

    def move(self, posedata, comp=1, option=""):
        self.arm.Move(comp, posedata, option)

    def curpos(self):
        return self.arm.Execute("CurPos", "")

    def get_value(self, io):
        var = self.ctrl.AddVariable(io, "")
        return var
