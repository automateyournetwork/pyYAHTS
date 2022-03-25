import sys
import logging
import json
from pyats.topology import Testbed, Device
from genie import testbed

class get_json():
    def __init__(self, hostname, os, username, password, command):
        self.hostname = hostname
        self.os = os
        self.username = username
        self.password = password
        self.command = command
        self.print_json()

    # Create Testbed
    def connect_device(self):
        try:
            first_testbed = Testbed('dynamicallyCreatedTestbed')
            testbed_device = Device(self.hostname,
                        alias = self.hostname,
                        type = 'switch',
                        os = self.os,
                        credentials = {
                            'default': {
                                'username': self.username,
                                'password': self.password,
                            }
                        },
                        connections = {
                            'cli': {
                                'protocol': 'ssh',
                                'ip': self.hostname,
                                'port': 22,
                                'arguements': {
                                    'connection_timeout': 360
                                }
                            }
                        })
            testbed_device.testbed = first_testbed
            new_testbed = testbed.load(first_testbed)
        except Exception as e:
            logging.exception(e)
        return(new_testbed)

    def capture_state(self):
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        for device in self.connect_device():
            device.connect(log_stdout=False)
        # Parse or Learn based on command
            if 'show' in self.command:
                try:
                    command_output = device.parse(self.command)
                except:
                    command_output = f"Cannot Parse { self.command }"
            elif self.command == "config":
                try:
                    command_output = device.learn(self.command)
                except:
                    command_output = "Cannot Learn Config"
            elif self.command == "platform":
                try:
                    command_output = device.learn(self.command).to_dict()
                except:
                    command_output = "Cannot Learn Platform"
            else:
                try:
                    command_output = device.learn(self.command).info
                except:
                    command_output = f"Cannot Learn { self.command }"
            return(command_output)

    def print_json(self):
        print(json.dumps(self.capture_state(), indent=4, sort_keys=True))
        return

if __name__ == "__main__":
    get_json(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])        