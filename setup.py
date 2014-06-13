from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['pr2_gripper_traj_action'],
    package_dir={'': 'nodes'},
    requires=['actionlib', 'actionlib_msgs', 'std_msgs' , 'roslib'  , 'pr2_controllers_msgs', 'rospy' ],
    scripts=['nodes/pr2GripperTrajActionServer.py' ]
)

setup(**d)
