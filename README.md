# waiter_bringup
final project



Run command : 
```bash
source ros2_ws/install/setup.bash
sudo apt update
sudo apt install ros-foxy-dynamixel-sdk
sudo apt install ros-foxy-turtlebot3-msgs
sudo apt install ros-foxy-turtlebot3
echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
export ROS_DOMAIN_ID=30 #TURTLEBOT3

mkdir –p ~/turtlebot3_ws/src/
cd ~/turtlebot3_ws/src/
git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/turtlebot3_ws && colcon build --symlink-install
. install/setup.bash 

sudo apt install ros-foxy-navigation2
sudo apt install ros-foxy-nav2-bringup
sudo apt install ros-foxy-turtlebot3-gazebo

export TURTLEBOT3_MODEL=waffle
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/foxy/share/turtlebot3_gazebo/models
ros2 launch nav2_bringup tb3_simulation_launch.py

```

When reopen the project :

```bash
echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
export ROS_DOMAIN_ID=30 #TURTLEBOT3
cd ~/turtlebot3_ws
. install/setup.bash
export TURTLEBOT3_MODEL=waffle
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/foxy/share/turtlebot3_gazebo/models
```


Pour le prog principal :
```bash
cd ~ros2_ws/src
git clone https://github.com/maximilianmorlion/waiter_bringup.git
```

Glisser le action_tutorials_interfaces dossier dans le ros2_ws/src

puis 

```bash
cd ros2_ws/src && colcon build

```

Pour check si ca marche :
```bash
. install/setup.bash
ros2 interface show waiter_bringup/action/Waiter
```
