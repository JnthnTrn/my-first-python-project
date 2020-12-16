class PythonClass:
    def __init__(self, teacher_name, slack_channel_name):
        self.teacher_name = teacher_name
        self.slack_channel_name = slack_channel_name
    def __repr__(self):
        return self.teacher_name
    start_time = "4:00pm"
    def print_start_time(self):
        print(self.start_time)
#PythonClass(slack_channel_name) sets slack_channel_name to the argument
​
​
alex_python_class = PythonClass("alex", "totally not discord")
hunter_python_class = PythonClass("fire breathing rubber duckies")
​
num = 5
print(alex_python_class.slack_channel_name)
print(hunter_python_class.slack_channel_name)
​
alex_python_class.print_start_time()
​
#__repr__ method
print(alex_python_class)