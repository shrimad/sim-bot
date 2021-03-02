# Demo of a simple proportional line follower using two sensors
# It's deliberately flawed and will exit with errors in some circumstances;
# try fixing it!

from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, UltrasonicSensor
import time

steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)
gyro = GyroSensor(INPUT_4)
ultrasonic = UltrasonicSensor(INPUT_1)

GAIN = 1

while True:
    prevDistance = ultrasonic.distance_centimeters
    #print( '********' )
    #print('Gyro: ' + str(gyro.angle_and_rate))
    #print('Ultrasonic: ' + str(ultrasonic.distance_centimeters))
    error = colorLeft.reflected_light_intensity - colorRight.reflected_light_intensity
    #print( "Left light intensity: " + str( colorLeft.reflected_light_intensity ))
    #print( "Right light intensity: " + str( colorRight.reflected_light_intensity ))
    correction = error * GAIN
    #ultrasonic test
    if (  ultrasonic.distance_centimeters < 2 ):
        print ("break coz of distance")
        break
    elif( ( correction > 100 ) or ( correction < -100 ) ):
        diff = correction % 100
        count = correction / 100
        steerVal = 0;
        print( "diff: " + str( diff ) )
        print( "count: " + str( count ) )
        print( "correction: " + str( correction ) )
        if( correction > 100 ):
            steering_drive.on ( 100, 20 )
            steering_drive.on ( diff, 20 )
        else:
            steering_drive.on ( -100, 20 )
            steering_drive.on ( 0 - diff, 20 )
            
        
        steering_drive.on( diff, 20)
    else:
        #print( "Correction: " + str( correction ) )
        steering_drive.on(correction, 20)