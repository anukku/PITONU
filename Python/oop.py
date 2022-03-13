# class Robot:
#     def walk(self):
#         print("The robot is walking")


# robot = Robot()
# print(type(robot))
# print(isinstance(robot, Robot))
# robot_obj = Robot()
# print(isinstance(robot_obj, Robot))

# robot = Robot(2.4, 6.5)
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print("walking")


robot = Robot(1.3, 11.2)
robot.walk()

print(robot.x)
print(robot.y)
