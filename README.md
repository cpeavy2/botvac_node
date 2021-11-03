## (Neato) Botvac launch files
 
This repository contains ROS2 Foxy launch files for the Neato Botvac robots.
 
## Assumes Ubuntu 20.04 and ROS2 Foxy have been successfully installed
 
## Install on Ubuntu PC workstation and Raspberry Pi4
 
Prerequisites:
```
sudo apt install build-essential
sudo apt install ros-foxy-xacro
sudo apt install python3-rosdep2
```
Be sure and create a workspace for your ROS2 source builds.
Check these repos out into your workspace as follows:
```
cd <ws>/src
git clone https://github.com/cpeavy2/botvac_node.git
git clone https://github.com/cpeavy2/neato_robot.git
git clone https://github.com/kobuki-base/cmd_vel_mux.git
git clone https://github.com/kobuki-base/velocity_smoother.git
git clone -b foxy-devel https://github.com/ros-planning/navigation2.git
 
cd ..
rosdep update
rosdep install --from-paths src --ignore-src -r -y
 
echo 'source ~/<ws>/install/setup.bash' >> ~/.bashrc   # sources setup.bash for future sessions. Use your own ROS workspace.
source ~/<ws>/install/setup.bash                       # sources setup.bash for current session
 
colcon build                                           # This will take a long time so use an AC adapter not battery power.
``` 
## Power Pi with battery bank and put into dirt bin on Botvac. Connect Pi to micro USB socket in the dirt bin and make sure the robot is on.
## ssh to Pi4 and launch
``` 
ros2 launch botvac_node botvac_base.launch.py          # This launches the Neato Node which calls the Neato Driver.
``` 
## Launch Slam Toolbox on PC
```
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=False autostart:=True map:=/home/user/ws/src/navigation2/nav2_bringup/bringup/maps/map.yaml slam:=True
```  
   Note: Load from directory on your workstation. Remove "slam:=True" to load saved map.
 
## Run RViz2 on PC
```
ros2 launch nav2_bringup rviz_launch.py 
```
## Run Teleop on PC
``` 
ros2 run teleop_twist_keyboard teleop_twist_keyboard
``` 
## To create map drive robot around using the teleop keyboard node
 
## After finishing the map use this command to save map on PC

```
ros2 run nav2_map_server map_saver_cli -f ~/<ws>/src/navigation2/nav2_bringup/bringup/maps/map --free 0.196 --ros-args -p save_map_timeout:=5000
```
Note: Save to directory on your workstation. That is use your own ROS2 workspace.
 

## After creating the map and saving it kill the slam toolbox and rviz2 terminal. Launch the below launch file to load in the map you saved.

``` 
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=False autostart:=True map:=/home/user/ws/src/navigation2/nav2_bringup/bringup/maps/map.yaml
```
Again, load from user and workspace directory on your workstation.

## Relaunch rviz2

```
ros2 launch nav2_bringup rviz_launch.py
```

## On rviz2 Set the robot's pose (2D Pose Estimate). Select a target goal (Navigation2 Goal) on the map and the robot will autonomously navigate there.
