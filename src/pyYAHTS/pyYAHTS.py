import sys
import rich_click as click
import json
import yaml
import pandas as pd
import tabulate
import logging
import email
import smtplib
import ssl
from pyats.topology import Testbed, Device
from genie import testbed
from rich import print_json
from rich.console import Console
from json2table import convert
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from fpdf import FPDF
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class GetJson():
    def __init__(self, hostname, os, username, password, command, filetype, from_email, email_password, to_email):
        self.hostname = hostname
        self.os = os
        self.username = username
        self.password = password
        self.command = command
        self.filetype = filetype
        self.from_email = from_email
        self.email_password = email_password
        self.to_email = to_email

    def print_json(self):
        parsed_json = json.dumps(self.capture_state(), indent=4, sort_keys=True)
        print_json(parsed_json)
        if self.filetype:
            self.pick_filetype(parsed_json)
        if self.from_email != 'none' and self.email_password != 'none' and self.to_email != 'none':
            self.send_email(parsed_json)

    def pick_filetype(self, parsed_json):
        if self.filetype == "none":
            pass
        elif self.filetype == 'json':
            self.json_file(parsed_json)
        elif self.filetype == 'yaml':
            self.yaml_file(parsed_json)
        elif self.filetype == 'html':
            self.html_file(parsed_json)
        elif self.filetype == 'datatable':
            datatable = "True"
            self.html_file(parsed_json, datatable)
        elif self.filetype == 'pdf':
            self.pdf_file(parsed_json)
        elif self.filetype == 'markdown':
            self.markdown_file(parsed_json)
        elif self.filetype == 'csv':
            self.csv_file(parsed_json)
    
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

    def pdf_file(self, parsed_json):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size = 6)
        pdf.cell(200, 10, txt = f"{self.hostname} {self.command}", ln = 1, align = 'C')
        pdf.multi_cell(200, 10, txt = parsed_json)
        pdf.output(f'{self.hostname} {self.command}.pdf')
        click.secho(f"PDF file created at { sys.path[0] }/{self.hostname} {self.command}.pdf", fg='green')

    def markdown_file(self, parsed_json):
        df = pd.json_normalize(json.loads(parsed_json),max_level=2)
        markdown_table = df.to_markdown(index='false')
        with open(f'{self.hostname} {self.command}.md', 'w') as f:
            f.write(markdown_table)
        click.secho(f"Markdown file created at { sys.path[0] }/{self.hostname} {self.command}.md", fg='green')

    def csv_file(self, parsed_json, expand_all=False):
        df = pd.json_normalize(json.loads(parsed_json))
        df.to_csv(f'{self.hostname} {self.command}.csv', index=False)
        click.secho(f"CSV file created at { sys.path[0] }/{self.hostname} {self.command}.csv", fg='green')

    def send_email(self, parsed_json):
        subject = f"An Email from pyYAHTS Device {self.hostname} and Command {self.command}"
        body = parsed_json
        sender_email = self.from_email
        receiver_email = self.to_email
        password = self.email_password

        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            click.secho(f"Email sent to {receiver_email}", fg='green')

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
@click.option('--filetype', prompt='Filetype', type=click.Choice(['none','json','yaml','html','datatable','markdown','pdf','csv'], case_sensitive=True), help='Filetype to output captured network state to', required=False, default='none')
@click.option('--from_email', prompt='From Email', help='Email address to send output from', required=False, default='none')
@click.option('--email_password', prompt='Email Password', hide_input=True, help='Email account password', required=False, default='none')
@click.option('--to_email', prompt='To Email', help='Email address to send output to', required=False, default='none')
def cli(hostname, os, username, password, command, filetype, from_email, email_password, to_email):
    invoke_class = GetJson(hostname, os, username, password, command, filetype, from_email, email_password, to_email)
    invoke_class.print_json()

if __name__ == "__main__":
    cli()