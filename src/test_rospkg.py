#!/usr/bin/env python

import rospkg


def test_rospkg():
    # Initialize the ROS package object
    rospack = rospkg.RosPack()

    # Get a list of all available packages
    packages = rospack.list()

    # Print the list of packages
    print("Available ROS packages:")
    for package in packages:
        print(package)

if __name__ == '__main__':
    test_rospkg()
