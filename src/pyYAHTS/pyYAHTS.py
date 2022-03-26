import sys
import rich_click as click
import json
import yaml
import logging
from pyats.topology import Testbed, Device
from genie import testbed
from rich import print_json
from json2table import convert
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

class GetJson():
    def __init__(self, hostname, os, username, password, command, filetype):
        self.hostname = hostname
        self.os = os
        self.username = username
        self.password = password
        self.command = command
        self.filetype = filetype

    def print_json(self):
        parsed_json = json.dumps(self.capture_state(), indent=4, sort_keys=True)
        print_json(parsed_json)
        if self.filetype:
            self.pick_filetype(parsed_json)

    def pick_filetype(self, parsed_json):
        if self.filetype == 'json':
            self.json_file(parsed_json)
        elif self.filetype == 'yaml':
            self.yaml_file(parsed_json)
        elif self.filetype == 'html':
            self.html_file(parsed_json)
        elif self.filetype == 'datatable':
            datatable = "True"
            self.html_file(parsed_json, datatable)
    
    def json_file(self, parsed_json):
        with open(f'{self.hostname} {self.command}.json', 'w') as f:
            f.write(parsed_json)
        click.secho(f"JSON file created at { sys.path[0] }/{self.hostname} {self.command}.json", fg='green')

    def yaml_file(self, parsed_json):
        clean_yaml = yaml.dump(json.loads(parsed_json), default_flow_style=False)
        with open(f'{self.hostname} {self.command}.yaml', 'w') as f:
            f.write(clean_yaml)
        click.secho(f"YAML file created at { sys.path[0] }/{self.hostname} {self.command}.yaml", fg='green')

    def html_file(self, parsed_json, datatable):
        good_json = json.loads(parsed_json)
        build_direction = "TOP_TO_BOTTOM"
        table_attributes = {"style" : "width:100%"}
        html_version = convert(good_json, build_direction=build_direction, table_attributes=table_attributes)
        if datatable == "True":
            self.datatable_file(html_version)
        else:                    
            with open(f'{self.hostname} {self.command}.html', 'w') as f:
                f.write(html_version)
            click.secho(f"HTML file created at { sys.path[0] }/{self.hostname} {self.command}.html", fg='green') 

    def datatable_file(self, html_version):
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(template_dir))
        datatable_template = env.get_template('datatable.j2')
        datatable_output = datatable_template.render(table=html_version)
        with open(f'{self.hostname} {self.command}_datatable.html', 'w') as f:
            f.write(datatable_output)
        click.secho(f"Datatable file created at { sys.path[0] }/{self.hostname} {self.command}.html", fg='green')

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
@click.option('--filetype', prompt='Filetype', type=click.Choice(['json','yaml','html','datatable'], case_sensitive=True), help='Filetype to output captured network state to', required=False)
def cli(hostname, os, username, password, command, filetype):
    invoke_class = GetJson(hostname, os, username, password, command, filetype)
    invoke_class.print_json()

if __name__ == "__main__":
    cli()