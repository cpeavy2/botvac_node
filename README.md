## (Neato) Botvac launch files
 
This repository contains ROS2 humble launch files for the Neato Botvac robot and remote Workstation. Not compatible with D8, D9 and D10.
 
## Assumes Ubuntu 22.04 and ROS2 Humble have been successfully installed on both Workstation and Pi
 
## Install on Raspberry Pi4
 
Prerequisites:
```
sudo apt install build-essential
sudo apt install ros-humble-xacro
sudo apt install python3-rosdep2
```
Be sure and create a workspace <ws> and source <src> directory for your ROS2 source builds.
...
Check these repos into that workspace <ws> / source <src> directory as follows:
```
cd <ws>/src
git clone https://github.com/cpeavy2/botvac_node.git
git clone https://github.com/cpeavy2/neato_robot.git
git clone https://github.com/kobuki-base/cmd_vel_mux.git
git clone https://github.com/kobuki-base/velocity_smoother.git
``` 
## Install on Ubuntu PC workstation in /src (not necessary to have Nav2 on Pi)
```
cd <ws>/src
git clone -b humble https://github.com/ros-planning/navigation2.git

```
## On both Workstation and Pi
```
cd ..
rosdep update
rosdep install --from-paths src --ignore-src -r -y
``` 
Install colcon: ROS 2 repository!
https://colcon.readthedocs.io/en/released/user/installation.html
 
## On both Workstation and Pi
``` 
cd ~/<ws>
colcon build
 
cd ..    # Home directory
echo 'source ~/<ws>/install/setup.bash' >> ~/.bashrc   # sources setup.bash for future sessions. Use your own ROS workspace.
source ~/<ws>/install/setup.bash                       # sources setup.bash for current session
 
``` 
## Power Pi with Battery Bank and put into dirt bin on Botvac. Connect Pi to micro USB socket in the dirt bin and make sure the robot is on.
## ssh to Pi4 and launch
``` 
ros2 launch botvac_node botvac_base.launch.py          # This launches the Neato Node which calls the Neato Driver.
``` 
## Launch Slam Toolbox on PC Workstation
```
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=False autostart:=True map:=/home/user/ws/src/navigation2/nav2_bringup/bringup/maps/map.yaml slam:=True
```  
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
 

## After creating the map and saving it... kill the slam toolbox and rviz2 terminal. Launch the below launch file to load in the map you saved.

``` 
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=False autostart:=True map:=/home/user/ws/src/navigation2/nav2_bringup/bringup/maps/map.yaml
```
Again, load from user and workspace directory on your workstation.

## Relaunch rviz2

```
ros2 launch nav2_bringup rviz_launch.py
```

## On rviz2 set the robot's pose (2D Pose Estimate). Select a target goal (Navigation2 Goal) on the map and the robot will autonomously navigate there.
