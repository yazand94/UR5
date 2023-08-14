##### this program is the main program for the whole task (Robot's movements, Camera, and results in GUI)
# from camera.save_and_load_image import take_photos_helper
# from classifier.predict import predict_image_list
# from GUI.start import start_grid_vis
# from utils import write_predict_result, read_predict_result
import time
import socket
import numpy as np
from operator import add
import robot_control as rc

#Should be something like this:
#
# Grab tool
# Move robot to cam
# Grab 1 image and save to output_images
# turn tool                                 ) repeat 7 times
# Grab 1 image and save to output_images    )
# predict image list
# put tool away
# calculate result
# show result in GUI
# Grab next tool
# and so on
# until all tools are processed
#
# And some example code:

# socket realtime connection
rt_socket = None

####### Socket settings:
HOST= "169.254.46.85"
PORT= 30003

# Define your new functions here. These are just placeholders and you'll need to implement them.

def close_gripper():
    f= open("C:/Python/Prüfzelle/python-urx-master/python-urx-master/examples/close.script", "rb")
    l= f.read(1024)

    while (l):
        rt_socket.send(l)
        l= f.read(1024)
    time.sleep(1)

def open_gripper():
    f= open("C:/Python/Prüfzelle/python-urx-master/python-urx-master/examples/open.script", "rb")
    l= f.read(1024)

    while (l):
        rt_socket.send(l)
        l= f.read(1024)
    time.sleep(1)

def go_to_home():
    #HOME1:
    rt_socket.send(("movej([3.10424261, -2.0193459, 2.17555291, 1.4432128, 4.73088947, -1.5905185],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)

def grab_tool(position_pick : list):
    ## The robot move towards the first tool:
    #Wegpunkt_1:
    rt_socket.send(("movej([3.36010788, -1.75876829, 2.00573238, 1.3566444, 4.72006843, -1.84725648],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_2:
    rt_socket.send(("movel([3.30076668, -1.81496789, 1.6048302, 1.81304803, 4.72704975, -1.74829631],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_3:
    rt_socket.send(("movel([3.24613788, -1.729621, 1.2384856, 2.09299884, 4.73001681, -1.6924458],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_4:
    rt_socket.send((f"movel({str(position_pick)},\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)

    #Gripper Close:
    close_gripper()

    #Wegpunkt_5:
    rt_socket.send(("movel([3.25015213, -1.75789562, 2.16351014, 1.1873475, 4.72233736, -1.7011724],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)

def move_robot_to_cam():
    #Wegpunkt_6:
    rt_socket.send(("movej([3.06427457, -2.1940534, 2.44276282, 1.3367477, 4.71605417, -1.2938126],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_7:
    rt_socket.send(("movej([3.0639255, -3.07143042, 2.58395996, 2.0821778, 4.74869183, -1.305506],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_55:
    rt_socket.send(("movej([3.21018409, -3.07806267, 2.62619693, 2.72114284, 4.68498731, -1.6428784],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_8:
    rt_socket.send(("movej([3.06427457, -3.07125588, 2.08078153, 3.89330596, 4.6355945, -1.3060299],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Waypoint_1:
    rt_socket.send(("movej([3.06410003, -2.59059221, 1.97606178, 3.98912454, 4.76387619, -0.25970499],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Waypoint_2:
    rt_socket.send(("movej([3.0639255, -2.29667876, 1.74777271, 4.35878527, 4.79424492, -0.19652407],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Waypoint_3:
    rt_socket.send(("movej([3.0639255, -2.52095357, 1.7437585, 4.66927935, 4.75305515, -0.19704767],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Waypoint_4:
    rt_socket.send(("movej([3.04943927, -1.6308357, 1.1054915, 5.25152119, 4.68952517, -0.05899213],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_9:
    rt_socket.send(("movel([3.17248498, -1.606401, 1.121025, 5.21486927, 4.69161956, 0.06440265],\
             a=0.1, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_22:
    rt_socket.send(("movel([3.17248498, -1.6517796, 1.2849114, 5.09601235, 4.69231769, 0.06475172],\
             a=0.1, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)

def find_tool_sensor(z_step: float):
    while True: 
        if rc.get_digital_input(0):
            return True
        print("True")
        # Move z axis [2] toward sensor
        sensor_position = rc.get_tool_positions()
        sensor_position[2] -= z_step
        rt_socket.send(("movej(get_inverse_kin(p" + str(sensor_position) + "), a=1, v=2)" + "\n").encode('utf8'))
        rc.wait_robot_moving(rt_socket)
        rc.wait_robot_moving_done(rt_socket)


def turn_tool(turn_angle : float):
    turn_position = rc.get_joint_positions()
    turn_position[5] += np.deg2rad(turn_angle) # convert to radians
    rt_socket.send(("movej(" + str(turn_position) + ", a=1, v=1)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)

def put_tool_away(position_pick : list):
    #Waypoint_7:
    rt_socket.send(("movel([3.04943927, -1.616873, 1.0620328, 5.28119178, 4.68952517, -0.05899213],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)    
    #Waypoint_8:
    rt_socket.send(("movel([3.23374604, -2.26893, 1.4091788, 5.56829845, 4.61185802, -1.48161],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Waypoint_9:
    rt_socket.send(("movel([3.15764968, -2.59163941, 2.04343149, 3.70899919, 4.66753402, -1.5404276],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Waypoint_10:
    rt_socket.send(("movel([3.17039059, -2.81678688, 2.5380578, 3.43952036, 4.65322232, -1.5388568],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Waypoint_11:
    rt_socket.send(("movel([3.28523325, -2.7214919, 2.56528493, 3.220307, 4.55478575, -1.5500269],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Waypoint_12:
    rt_socket.send(("movel([3.28523325, -2.72131737, 2.33298161, 3.21960887, 4.55478575, -1.5500269],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Waypoint_13:
    rt_socket.send(("movel([2.93546927, -2.72131737, 2.33298161, 3.21960887, 4.55478575, -1.5500269],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_58:
    rt_socket.send(("movej([3.24386895, -2.48796685, 2.5062928, 1.6851154, 4.75357875, -1.6310102],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_61:
    rt_socket.send(("movej([3.46727109, -2.12528743, 2.3701571, 1.3048081, 4.60365497, -1.8570303],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_63:
    rt_socket.send(("movel([3.17318311, -1.76766947, 2.2963297, 1.0084512, 4.6605527, -1.5604989],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_60:
    rt_socket.send(("movel([3.00702777, -1.67552, 2.36719006, 0.885231, 4.76981031, -1.433788],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_5:
    rt_socket.send(("movel([3.25015213, -1.75789562, 2.16351014, 1.1873475, 4.72233736, -1.7011724],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_59:
    rt_socket.send(("movel([3.25277013, -1.7404423, 1.3255776, 1.9942132, 4.72198829, -1.5746361],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_68:
    rt_socket.send(("movej([3.25765705, -1.7090264, 1.2239994, 2.06088478, 4.7162287, -1.58825],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)
    #Wegpunkt_33:
    rt_socket.send(("movej([3.25748252, -1.7044885, 1.1997393, 2.08497032, 4.7158796, -1.5879006],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)

    # Gripper OPEN
    open_gripper()

    #Wegpunkt_5:
    rt_socket.send(("movel([3.25015213, -1.75789562, 2.16351014, 1.1873475, 4.72233736, -1.7011724],\
             a=2, v=2)" + "\n").encode('utf8'))
    rc.wait_robot_moving(rt_socket)
    rc.wait_robot_moving_done(rt_socket)

# # Take photo from camera
# def take_photo():
#     # output_images = take_photos_helper(8)
#     # #output_images = ["classifier/testdataset/2208241448352.png"]
#     # res = predict_image_list(output_images)
#     # write_predict_result(res)
#     # res_storage = read_predict_result()
#     # start_grid_vis(res_storage)

#     # Predict
#     # store prediction
#     # visualize in GUI
#     pass

# def calculate_result():
#     pass  # Replace with code to calculate the result

# Assume we have a list of tools to process
tools = ['tool1', 'tool2', 'tool3', 'tool4', 'tool5', 'tool6', 'tool7', 'tool8']

def get_tool_position(tool_id):
    match tool_id:
        case 'tool1':
            return [3.24823227, -1.7168804, 1.2067206, 2.1031217, 4.72512988, -1.6943656]
        case 'tool2':
            return [3.24823227, -1.7168804, 1.2067206, 2.1031217, 4.72512988, -1.6943656]
        case 'tool3':
            return [3.24823227, -1.7168804, 1.2067206, 2.1031217, 4.72512988, -1.6943656]
        case 'tool4':
            return [3.24823227, -1.7168804, 1.2067206, 2.1031217, 4.72512988, -1.6943656]
        case 'tool5':
            return [3.24823227, -1.7168804, 1.2067206, 2.1031217, 4.72512988, -1.6943656]
        case 'tool6':
            return [3.24823227, -1.7168804, 1.2067206, 2.1031217, 4.72512988, -1.6943656]
        case 'tool7':
            return [3.24823227, -1.7168804, 1.2067206, 2.1031217, 4.72512988, -1.6943656]
        case 'tool8':
            return [3.24823227, -1.7168804, 1.2067206, 2.1031217, 4.72512988, -1.6943656]
        case _:
            return None

# main
if __name__ == '__main__':
    # Connect to robot
    rt_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rt_socket.connect((HOST, PORT))
    time.sleep(0.1)

    # Go to home position
    go_to_home()

    # For each tool
    for tool in tools:
        # Get tool position
        tool_position = get_tool_position(tool)

        # Grab tool from pick position
        grab_tool(tool_position) #each tool should have coordinates ore previous defined moves assigned

        # Move robot to cam
        move_robot_to_cam()

        # Find tool sensor
        find_tool_sensor(z_step=0.001)

        # Move back from sensor
        current_position = rc.get_tool_positions()
        current_position[1] -= 0.022 # move to y
        current_position[2] += 0.022 # move to z
        rt_socket.send((f"movel(p{str(current_position)}, a=1, v=2)" + "\n").encode('utf8'))
        rc.wait_robot_moving(rt_socket)
        rc.wait_robot_moving_done(rt_socket)
        # rt_socket.send((f"movel(p{str(current_position[1])}, a=0.01, v=0.5)" + "\n").encode('utf8'))
        # rc.wait_robot_moving(rt_socket)
        # rc.wait_robot_moving_done(rt_socket)

        # Grab 1 image and save to output_images
        output_images = []
        turn_angle = 20     # in degrees
        for _ in range(8):
            #take_photo() # take photo
            # output_imagert_socket.append(take_photos_helper(1))  # Grab 1 image       
            turn_tool(turn_angle) # turn tool

    #     # Predict
    #     # res = predict_image_list(output_images)
    #     # write_predict_result(res)

        # retrun tool to pick position
        put_tool_away(tool_position)

    #     # store prediction
    #     # res_storage = read_predict_result()
    #     calculate_result()

    # # After all tools are processed
    # # start_grid_vis(res_storage)