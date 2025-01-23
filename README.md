I. Project name: Intelligent driving car
Ii. Project Introduction:
This car based on the Raspberry PI microcontroller, its principle is mainly the use of PWM control power control chip, power control chip and then driven by the control DC motor, so that the vehicle has the ability to move. At the same time, this car has strong expansion ability, and modules can be added to expand the function in the later stage.
Materials: Raspberry Pi pico to weld pins,L239D power chip, car body kit (purchased from the Internet to assemble parts), 18650 double series battery box, power supply voltage regulator module, auxiliary materials and wire several.
Iii. Project Implementation:
1. Implementation principle
1.1 PWM
Pulse width modulation (PWM) is an analog control mode, according to the change of the corresponding load to modulate the bias of the transistor base or MOSFet gate, to achieve the change of transistor or MOSFet on-time, so as to achieve the change of the output of the switching regulator power supply. This method can keep the output voltage of the power supply constant when the working conditions change, and is a very effective technology to control the analog line by using the digital signal of the microprocessor. It is widely used in many fields from measurement and communication to power control and conversion.
1.2 Raspberry Pi pico
This is the Raspberry PI microcontroller, based on the RP2040 chip developed by Raspberry PI, which is sufficient for this project. And brush firmware is convenient, suitable for this project. Support MicroPython, c/ C ++. The programming language of this project is MicroPython.
1.3 MicroPython
MicroPython, a complete software implementation of the Python3 programming language, is written in C and optimized to run on a microcontroller. MicroPython is a complete Python compiler and runtime system that runs on microcontroller hardware. Provide the user with an interactive prompt (REPL) to execute the supported commands immediately. In addition to including selected core Python libraries, MicroPython also includes modules that give programmers access to low-level hardware.
1.4 Power Chip
The power chip uses L239D, which has two power supply interfaces, and the tank steering is adopted this time, which needs to control the stop and turn of the wheel, and 8 pins are left and right. Vcc1 supplies 5V power to the chip, and Vcc2 is the power supply port of the motor. In order to maintain a strong power, Vcc2 is supplied with a nominal 7.2V power supply composed of two 18650 in series. Vcc2 of L239D can withstand up to 36V, and if the selected motor can withstand higher voltage, the nominal value is not more than 36V. L239D is also theoretically possible.
1.5 Others:
The power supply of the Raspberry PI uses a double-section 18650 and 7.2V to 5V step-down voltage regulator module, and the connection between the lines uses breadboard and dupont line. The vehicle adopts tank steering, that is, does not use the steering gear and other steering modules, and realizes steering by controlling tire movement, similar to the steering of tank crawler vehicles.
2 Raspberry PI Environment Deployment:
First of all, you need a computer preferably win10 system, there is a MicroUSB to connect the Raspberry PI and the computer, and then download the firmware about the Raspberry PI, the extension is uf2, can be downloaded from the Raspberry PI PICO Chinese website, after the download is successful, the Raspberry PI to the computer, the computer will pop up a RPI - RP2 U disk, Place the prepared uf2 file into this USB flash drive. The USB flash drive will disappear.
After that, please right-click this computer, click Manage, then click Manage Computer, System Tools, Device Manager, click the top icon, port, there will be USB serial device, in the meantime, please unplug the USB flash drive. Remember this serial number. The programming environment is configured. Install programming software to use.
3. Programming software
thonny and pycharm are recommended here. Download thonny and pycharm from the Internet. Thonny was used to test and write files to the Raspberry PI, and pycharm was used to write programs first because of its auxiliary writing, but the machine we used was no longer packaged and could not be installed. To install Python at the same time, I chose 3.9.0.
Two software brainless next step is best. On the start page, Thonny is going to change the Language to simplified Chinese, change the Standard in intial settings to Raspberry Pi, and then click Let's go
I used 4.0.0, which has the installation interpreter at the bottom, just click on the MicroPython (Raspberry Pi pico) COMXX, XX is equal to the serial port number of the previous step

4. Line connection:

L239D: 1: Vcc1 knot Raspberry PI VBUS
2: input4 Connects to the Raspberry PI GP15
3: output4 Connect the motor
6: output3 Connect the motor
7: input3 Connects to Raspberry PI GP14
8: indicates enable3, and 4 indicates Raspberry PI GP10

16: Vcc2 junction external power supply positive electrode
15: input2 connects to Raspberry PI GP17
14: output2 connects to the motor
12: GND Connects to the Raspberry PI GND external power negative terminal
11: output1 connects to the motor
10: input1 connects to Raspberry PI GP16
9: indicates enable1. Indicates enable2: indicates Raspberry PI GP21
I made a four-wheel drive version, and the two motors in the base are facing each other, so I must test the battery before wiring. For the breadboard I used, connect the positive and negative terminals to the opposite and corresponding ports, determine a positive direction, and power on. If there is a reversed motor, just switch the government and the interface. Then the output interface jumper to the narrow plate.
Note: During the wiring, be sure not to randomly connect, according to the illustration and text description, in the test motor steering is, be sure to look at whether the short and positive and negative terminals are connected, in the wiring, should comply with the first wiring, after the power. After power on, should mode battery positive and negative lines, if there is heat, power off immediately.
5. Use of pycharm
After the success in the above steps, you can start programming. I recommend pycharm, which has auxiliary writing and debug, but unfortunately, the package of machine cannot be found, so we need to learn functions separately.
After pycharm is installed, open it, click NewProject, location to change the location of your folder, and after setting it up, click create. Right click on your own folder, New, PythonFile, then name write the name, click the first one. Press enter, and you can start programming.
Then use the auxiliary writing, write a letter, there will be a lot of prompts, use up and down left and right to select the statement, select the press enter, the statement will be presented, after writing a variable can press Ctrl and left key to find the variable.
6. Use of machine and utime: (Note: After pycharm is written, it should be opened with thonny, and when running, connect to the computer and click Run)
Machine is a package that controls the Raspberry PI:
machine.Pin(16, machine.pin-out) is the output of a Pin, this line of code represents the GP16 definition, and we can simply put it into a variable like this:
a = machine.Pin(16,machine.Pin.OUT)
Use another value function, like this:
a.	value(1)
It's simple, but this determines the steering of the motor, which you have to try yourself, whether it's clockwise or counterclockwise
Write the GP17 associated with it, and then use value control, 0 is off, 1 is on. These two should be used together, otherwise the program will not run.
There are also two functions and an initialization, 16,17,21, 16,17 is to control the forward and reverse rotation,21 is to control the speed, which uses PWM, PWM pin has an alternative method:
machine.PWM(machine.Pin(21))
The 21 pins that control the speed are initialized. Then we'll learn two functions, freq() and duty_u16.
freq () is to control the frequency, but we use a DC motor, without frequency control speed, so this is only a necessary parameter, it is recommended to set 50.
duty_u16 () is to control the duty cycle, which can be understood as controlling the speed, but there is a fixed formula: speed/100*65535 (0<=speed<=100) speed is how much speed is represented, and this is actually the case:
c = machine.PWM(machine.Pin(21))
c.freq(50)
c.duty_u16(100/100*65535)
Put together the previous program, one wheel can turn, 16,17,21 this group I set is the right wheel, now the right wheel can turn.
Then write the above code as a function, in the call, add the following instructions:
utime.sleep (3)
Your wheels will spin for three seconds. In the same way, write the other side, debug, and correct the inversion. I'll have a qualified car. Note that when switching instructions, use value (0) for all pins that control positive and negative rotation to start normally.
7. Save to Raspberry PI:
It's -- it's running, you put it in the raspberry PI, it runs automatically when it's powered on. It's easy to put in there, just create a new file, copy the code in there, go to Save, go to Raspberry, and just change the name to main.
But when you use a computer to change it, you can stop the wheel by stopping all the pins.
This completes the project.
4. Application scenarios:
In theory, if the equipment is added with lead plate, waterproof, it can operate in water and a certain ionizing radiation, with thermal imager, life search and rescue equipment, to determine the location of survivors, reduce the possibility of injury to rescuers, plus radar and steering gear, reduce the difficulty of search and rescue.


For Chinese you can wirte it in next.


一、项目名称：智能行驶小车
二、项目简介：
这一款基于树莓派的微控制器制作的小车，其原理主要是运用PWM控制电源控制芯片，电源控制芯片再由控制直流电机驱动，使车辆具有运动能力。同时，此车扩展能力强，后期可添加模块来扩展功能。
材料：Raspberry Pi pico 以焊针脚 ,L239D电源芯片，小车主体套件（从网上购买散件组装），18650双节串联电池盒，电源降压稳压模块，辅助材料及线材若干。
三、项目实施：
	1.实现原理
1.1PWM
脉冲宽度调制（PWM）是一种模拟控制方式，根据相应载荷的变化来调制晶体管基极或MOS管栅极的偏置，来实现晶体管或MOS管导通时间的改变，从而实现开关稳压电源输出的改变。这种方式能使电源的输出电压在工作条件变化时保持恒定，是利用微处理器的数字信号对模拟线路进行控制的一种非常有效的技术。广泛应用在从测量、通信到功率控制与变换的许多领域中。
		1.2 Raspberry Pi pico
这是树莓派的微控制器，基于树莓派自研的RP2040芯片制作，足够本次项目使用。且刷固件方便，适合本次项目。支持MicroPython，c/c++。本次项目编程语言采用MicroPython。
		1.3MicroPython
MicroPython，是Python3编程语言的一个完整软件实现，用C语言编写，被优化于运行在微控制器之上。MicroPython是运行在微控制器硬件之上的完全的Python编译器和运行时系统。提供给用户一个交互式提示符（REPL）来立即执行所支持的命令。除了包括选定的核心Python库，MicroPython还包括了给予编程者访问低层硬件的模块。
		1.4电源芯片
电源芯片采用的L239D，它有两个供电接口，并且本次采用了坦克转向，需要控制轮子的停与转，左右各8个引脚。Vcc1为为芯片供电5V，Vcc2则为电机的供电口，为了保持强大的动力，Vcc2通入了由两节18650串联组成的标称7.2V的电源供电，L239D的Vcc2标称可承受最高36V，若选的电机可承受较高电压，标称不大于36V，理论上也可以使用L239D。
		1.5其他：
树莓派的供电采用的是双节18650加7.2V转5V降压稳压模块，线路之间的连接采用面包板加杜邦线，本车采用了坦克转向即为，不使用舵机与其他转向模块，通过控制轮胎运动来实现转向，类似坦克履带车转向。
2树莓派环境部署：
首先你需要一台电脑最好是win10系统，还有一根有MicroUSB来连接树莓派与电脑，再下载关于树莓派的固件，后缀名为uf2，可从树莓派PICO中文网下载，下载成功后，将树莓派接入电脑，电脑会弹出一个RPI—RP2的U盘，将准备好的uf2文件放入此U盘。U盘将消失。
之后请右键此电脑，点击管理，之后点管理计算机，系统工具，设备管理器，点开最上面的图标，端口，会有USB串行设备，在此期间，请拔掉U盘。记住此串口号。编程环境配置完成。安装编程软件即可使用。
	3.编程软件：
这里推荐使用thonny与pycharm，从网上下载thonny与pycharm。Thonny用来测试与往树莓派写入文件，pycharm则是可以先写程序，因为其有辅助书写，但是，我们用的machine已经没有好包了，无法安装。同时要安装Python，我选择的是3.9.0。
两款软件无脑下一步最好。Thonny在开始页面是要把Language改成简体中文将intial settings中的Standard改成Raspberry Pi，之后点Let’s go
	我用的4.0.0，在底下有安装解释器，直接点开换成MicroPython（Raspberry Pi pico）COMXX， XX等于上一步的串口号
		
4.线路连接：
                                                                                                                                                                                            
L239D ：1：Vcc1 结 树莓派VBUS
2：input4 接 树莓派GP15
3：output4 接电机
6：output3 接电机
7：input3 接 树莓派GP14  
8：enable3,4 接 树莓派GP10

16：Vcc2 结 外部电源正极
15：input2 接 树莓派GP17
14：output2 接电机
12：GND 接树莓派GND 外部电源负极
11：output1 接电机
10：input1 接 树莓派GP16  
9：enable1,2 接 树莓派GP21
我做的是四驱版，底座的两个电机是对着的，在接线前，一定要用电池测试，我用的面包板，将正负极接到对一、应口上，认定一个正方向，上电，如果有反转的电机，将政府及接口对调即可，建议购买专业的面包板，将电机线接到窄板上，在树莓派与L239D接好后，再将输出接口跳线到窄板上。
注意：在接线途中，一定不要乱接，要按图示及文字说明，在测试电机转向是，一定要看好是否短接及正负极相接，在接线时，应遵守先接线，后通电。通电后，应模电池正负线，若有发热，立即断电。
	5.pycharm的使用
在上面步骤中成功后，就可以编程了，我推荐使用pycharm，这款软件有辅助书写，并且有debug，但是可惜的是machine的包，现在找不到合适的包了，需要单独学习函数。
在安装完pycharm后，打开，点击NewProject，location可以改变你的文件夹的位置，设置完后，点击create。在自己的文件夹上右键，New，PythonFile，之后name写名字，点第一个。回车，就可以开始编程了。
再用辅助书写时，写一个字母，会有很多提示，用上下左右来选择语句，选中后按回车，语句就呈现出来了，在写下一个变量后可以按Ctrl加左键就可以找到变量。
6.machine与utime的使用：（注：在pycharm写完后要用thonny打开，运行时需连接电脑，点击运行）
		Machine是控制树莓派的一种包:
machine.Pin(16,machine.Pin.OUT)是一个针脚的输出，这行代码代表着GP16的定义，而我们也很简单，把它放入变量，像这样：
		a = machine.Pin(16,machine.Pin.OUT)
再用一个value函数，像这样：
a.	value(1)
这很简单，但这决定了电机的转向，这需要自己试，是顺时针还是逆时针转
把与其相连的GP17也写进来，再用value控制，0是关，1是开。这两个要一起用才可以，不然此程序将无法运行。
	还有两个函数及一个初始化，16,17,21中，16,17是控制正反转，21则是控制速度，这就用到了PWM，PWM针脚有着另类的方法：
			machine.PWM(machine.Pin(21))
	这样控制速度的21针脚就初始化好了。再就是学习两个函数freq()与duty_u16。
	freq（）是控制频率的，但我们采用的是直流电机，不用频率控制速度，所以这只是一个必要的参数，这里建议设50即可。
	duty_u16（）是控制占空比的，可以理解为控制速度，但有一套固定的公式：speed/100*65535（0<=speed<=100）speed是代表多少速度，实际就是这样：
			c = machine.PWM(machine.Pin(21))
			c.freq(50)
					c.duty_u16(100/100*65535)
再把之前的程序拼起来，一边轮子就可以转了，16,17,21这组我设的是右边的轮，现在右边的轮可以转了。
再将上述代码写成一个函数，在调用，添加如下指令：
		utime.sleep（3）
你的轮子就可以转3秒了。再用相同的方法，写出另一侧，调试，改正反转。就有一辆合格的车了。注意，在指令切换时，将所有控制正反转的针脚，使用value（0）才可以正常启动。
	7.保存到树莓派：
这是，程序运行好，要放到树莓派里，通电后会自动运行。要放入其中也简单，再新建一个文件，把代码复制进去，点保存，选下面Raspberry的那个，把名字改成main即可。
但再用电脑改时，把所有引脚停止才可以使轮子停下。
这样整个项目就完成了。
四、运用场景：
这辆车在后续可添加模块扩展，可以实现搜救任务，理论上，若将此设备加铅板，防水，可在水中及一定电离辐射运转，搭配热成像仪，生命搜救设备，确定幸存者位置，减少救援人员受伤的可能性，加上雷达与舵机，减少搜救困难。


		
