import serial

com = serial.Serial(port = "/dev/ttyUSB0",
		baudrate = 9600,
		bytesize = serial.EIGHTBITS,
		parity = serial.PARITY_NONE,
		timeout = 1)
s = "test.ino"
com.write(s.encode())

a=1

while a:
    if com.in_waiting != 0:
        content =com.readline()
        print(content[:-2].decode())
    #else:
        #a=0