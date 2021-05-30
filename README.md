# waiter_bringup
final project


dezip action_ws.tar et glisser dans la branche principal du workspace
Run command : 
```bash
cd action_ws && colcon build
. install/setup.bash
```
Pour check si ca marche :
```bash
ros2 interface show action_tutorials_interfaces/action/Waiter
```

Pour le prog principal :
```bash
cd ~ros2_ws/src
git clone https://github.com/maximilianmorlion/waiter_bringup.git
```

