import machine
import utime


class run():
    def __init__(self):
        self.speed = 100
        self.runspeed = int(self.speed / 100 * 65535)
        self.l_pin = [16, 17, 22]  # f:16 b:17 run:22
        self.r_pin = [15, 14, 10]  # f:15 b:14 run:10
        self.l_go = 0  # f:0 b:1
        self.r_go = 0  # f:0 b:1
        self.l_run = machine.Pin(self.l_pin[self.l_go], machine.Pin.OUT)
        self.l_gospeed = machine.PWM(machine.Pin(self.l_pin[2]))
        self.r_run = machine.Pin(self.r_pin[self.r_go], machine.Pin.OUT)
        self.r_gospeed = machine.PWM(machine.Pin(self.r_pin[2]))
        # 必须同时使用两次value

    def l_speedout(self):
        self.l_gospeed.freq(50)
        self.l_gospeed.duty_u16(self.runspeed)

    def r_speedout(self):
        self.r_gospeed.freq(50)
        self.r_gospeed.duty_u16(self.runspeed)

    def stop(self):
        self.l_speedout()
        self.l_speedout()
        for l_stop in range(2):
            self.l_go = l_stop
            self.l_run.value(0)
        for r_stop in range(2):
            self.r_go = r_stop
            self.r_run.value(0)

    def left_f(self):  # turn right f
        self.stop()
        self.l_speedout()
        self.l_go = 0
        self.l_run.value(0)
        self.l_go = 1
        self.l_run.value(1)

    def left_b(self):  # turn right b
        self.stop()
        self.l_speedout()
        self.l_go = 1
        self.l_run.value(0)
        self.l_go = 0
        self.l_run.value(1)

    def right_f(self):  # turn left f
        self.stop()
        self.r_speedout()
        self.r_go = 0
        self.r_run.value(0)
        self.r_go = 1
        self.r_run.value(1)

    def right_b(self):  # turn left b
        self.stop()
        self.r_speedout()
        self.r_go = 1
        self.r_run.value(0)
        self.r_go = 0
        self.r_run.value(1)

    def all_forward(self):
        self.stop()
        self.left_f()
        self.right_f()

    def all_back(self):
        self.stop()
        self.left_b()
        self.right_b()

    def roundturnleft(self):
        self.stop()
        self.left_b()
        self.right_f()

    def roundturnright(self):
        self.stop()
        self.left_f()
        self.right_b()


go = run()
for i in range(2):
    go.all_forward()
    utime.sleep(3)
    go.stop()
    go.all_back()
    utime.sleep(3)
    go.stop()
    go.left_f()
    utime.sleep(3)
    go.stop()
    go.left_b()
    utime.sleep(3)
    go.stop()
    go.right_f()
    utime.sleep(3)
    go.stop()
    go.right_f()
    utime.sleep(3)
    go.stop()
    go.roundturnleft()
    utime.sleep(3)
    go.stop()
    go.roundturnright()
    utime.sleep(3)
    go.stop()
