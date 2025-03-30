"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
right_motor = robot.getDevice('right_motor')
right_motor.setPosition(float('inf'))
right_motor.setVelocity(1.0)
left_motor = robot.getDevice('left_motor')
left_motor.setPosition(float('inf'))
left_motor.setVelocity(1.0)
back_motor = robot.getDevice('back_motor')
back_motor.setTorque(0.0)      # 关闭电机扭矩输出
back_motor.setAvailableTorque(0.0)  # 可选：限制最大扭矩为 0

led = robot.getDevice('led')
led.set(1)

ds_front = robot.getDevice('dis_sen_front')
ds_front.enable(timestep)
ds_left = robot.getDevice('dis_sen_left')
ds_left.enable(timestep)
ds_right = robot.getDevice('dis_sen_right')
ds_right.enable(timestep)

left_camera = robot.getDevice("left_camera")
left_camera.enable(timestep)
right_camera = robot.getDevice("right_camera")
right_camera.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    dis_front = ds_front.getValue()
    dis_left = ds_left.getValue()
    dis_right = ds_right.getValue()
    if dis_front < 3:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        back_motor.setVelocity(0.0)
        back_motor.setAvailableTorque(10.0)
    else:
        if dis_left - dis_right > 5:
            left_motor.setVelocity(0.0)
            right_motor.setVelocity(1.5)
            back_motor.setVelocity(0.0)
            back_motor.setAvailableTorque(10.0)
        elif dis_left - dis_right < -5:
            right_motor.setVelocity(0.0)
            left_motor.setVelocity(1)
            back_motor.setVelocity(0.0)
            back_motor.setAvailableTorque(10.0)
        else:
            right_motor.setVelocity(1.0)
            left_motor.setVelocity(1.0)
            back_motor.setTorque(0.0)      # 关闭电机扭矩输出
            back_motor.setAvailableTorque(0.0)  # 可选：限制最大扭矩为 0
        
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    print(f'ds_front:{ds_front.getValue()},ds_left:{ds_left.getValue()},ds_right:{ds_right.getValue()}')
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
