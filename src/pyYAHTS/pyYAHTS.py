import sys
import rich_click as click
import json
import logging
from pyats.topology import Testbed, Device
from genie import testbed
from rich import print_json

class GetJson():
    def __init__(self, hostname, os, username, password, command):
        self.hostname = hostname
        self.os = os
        self.username = username
        self.password = password
        self.command = command

    def print_json(self):
        print_json(json.dumps(self.capture_state(), indent=4, sort_keys=True))

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

@click.command()
@click.option('--hostname', prompt='Hostname', help='Hostname of device - must match the device', required=True)
@click.option('--os', prompt='OS', type=click.Choice(['ios', 'iosxe', 'iosxr', 'nxos'], case_sensitive=True), help='OS of device - must match the device', required=True)
@click.option('--username', prompt='Username', help='Username', required=True)
@click.option('--password', prompt=True, hide_input=True, help="User Password", required=True)
@click.option('--command', prompt='Command', help='A valid pyATS Learn Function (i.e. ospf) or valid CLI Show Command (i.e. "show ip interface brief")', required=True)
def cli(hostname, os, username, password, command):
    invoke_class = GetJson(hostname, os, username, password, command)
    invoke_class.print_json()

if __name__ == "__main__":
    cli()