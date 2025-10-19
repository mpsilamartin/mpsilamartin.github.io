message = ""
R1 = 0
M = 0
L1 = 0
az = 0
ay = 0
ax = 0
distance = 0
radio.on()
radio.set_group(1)
# si maqueen V3
matrixLidarDistance.initialize(matrixLidarDistance.Addr.ADDR4,
    matrixLidarDistance.Matrix.MAT)
radio.set_group(1)

def on_forever():
    global ax, ay, az, distance, L1, M, R1, message
    ax = input.acceleration(Dimension.X)
    ay = input.acceleration(Dimension.Y)
    az = input.acceleration(Dimension.Z)
    # si maqueen Plus V2.1
    # distance = maqueenPlusV2.read_ultrasonic(DigitalPin.P13, DigitalPin.P14)
    # si maqueen Plus V3
    distance = matrixLidarDistance.matrix_point_output(matrixLidarDistance.Addr.ADDR4, 3, 3)
    # si maqueen V3
    L1 = maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1)
    M = maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M)
    R1 = maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1)
    if distance < 10:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            100)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            100)
    else:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            0)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            0)
    print([distance])
    # Construction du message à transmettre
    message = "" + str(ax) + "," + ("" + str(ay)) + "," + ("" + str(az)) + "," + ("" + str(distance)) + "," + ("" + str(L1)) + "," + ("" + str(M)) + "," + ("" + str(R1))
    radio.send_string(message)
    basic.pause(100)
basic.forever(on_forever)
