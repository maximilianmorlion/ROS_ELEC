# waiter_bringup
final project



Run command : 



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
