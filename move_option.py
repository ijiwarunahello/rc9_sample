class MoveOption:
    def __init__(self):
        self.speed = 100.0
        self.accel = 100.0
        self.decel = 100.0
        self.time = 0
        self.next = "NEXT"

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_accel(self, accel):
        self.accel = accel

    def get_accel(self):
        return self.accel

    def set_decel(self, decel):
        self.decel = decel

    def get_decel(self):
        return self.decel

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def set_next(self):
        self.next = "NEXT"

    def unset_next(self):
        self.next = ""

    def get_next(self):
        return self.next

    def generate(self):
        base = f"SPEED={self.speed},ACCEL={self.accel},DECEL={self.decel},"
        base += f"TIME={self.time}," if self.time > 0 else ""
        base += self.next
        return base
