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
from rich.progress import track
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
        self.supported_templates = ['acl',
                            'arp',
                            'bgp',
                            'dot1x',
                            'hsrp',
                            'interface',
                            'lldp',
                            'ntp',
                            'ospf',
                            'platform',
                            'routing',
                            'stp',
                            'vlan',
                            'vrf',
                            'show access-lists',
                            'show bgp process vrf all',
                            'show bgp sessions',
                            'show cdp neighbors',
                            'show cdp neighbors detail',
                            'show environment',
                            'show etherchannel summary',
                            'show interfaces',
                            'show interfaces status',
                            'show interfaces trunk',
                            'show interface',
                            'show interface status',
                            'show interface transceiver',
                            'show inventory',
                            'show ip arp',
                            'show ip arp vrf all',
                            'show ip interface brief',
                            'show ip ospf',
                            'show ip ospf database',
                            'show ip ospf interface',
                            'show ip ospf interface vrf all',
                            'show ip ospf neighbor',
                            'show ip ospf neighbor detail',
                            'show ip ospf neighbors detail',
                            'show ip ospf neighbors detail vrf all',
                            'show ip route',
                            'show ip route vrf all',
                            'show license summary',
                            'show mac address-table',
                            'show ntp associations',
                            'show port-channel summary',
                            'show version',
                            'show vlan',
                            'show vrf']

    def print_json(self):
        parsed_json = json.dumps(self.capture_state(), indent=4, sort_keys=True)
        print_json(parsed_json)
        if "Cannot" in parsed_json:
            click.secho("No Data To Create File", fg='red')
        else:
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
        elif self.filetype == 'svg':
            self.svg_file(parsed_json)
    
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
        with open(f'{self.hostname} {self.command}.html', 'w') as f:
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
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(template_dir))
                markdown_template = env.get_template(f'{self.os} md.j2')              
                markdown_output = markdown_template.render(command = self.command, data_to_template=json.loads(parsed_json))
                with open(f'{self.hostname} {self.command}.md', 'w') as f:
                    f.write(markdown_output)
                break          
            else:
                df = pd.json_normalize(json.loads(parsed_json),max_level=2)
                markdown_table = df.to_markdown(index='false')
                with open(f'{self.hostname} {self.command}.md', 'w') as f:
                    f.write(markdown_table)
        click.secho(f"Markdown file created at { sys.path[0] }/{self.hostname} {self.command}.md", fg='green')

    def csv_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(template_dir))
                csv_template = env.get_template(f'{self.os} csv.j2')              
                csv_output = csv_template.render(command = self.command, data_to_template=json.loads(parsed_json))
                with open(f'{self.hostname} {self.command}.csv', 'w') as f:
                    f.write(csv_output)
                break          
            else:
                df = pd.json_normalize(json.loads(parsed_json))
                df.to_csv(f'{self.hostname} {self.command}.csv', index=False)
        click.secho(f"CSV file created at { sys.path[0] }/{self.hostname} {self.command}.csv", fg='green')

    def svg_file(self, parsed_json):
        console = Console(record=True)
        console.print(parsed_json)
        console.save_svg(f"{self.hostname} {self.command}.svg", title=f"{self.hostname} {self.command}")
        import webbrowser
        webbrowser.open(f"{self.hostname} {self.command}.svg")

    def send_email(self, parsed_json):
        subject = f"An Email from pyYAHTS Device {self.hostname} and Command {self.command}"
        body = parsed_json
        sender_email = self.from_email
        receiver_email = self.to_email
        password = self.email_password

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        if self.filetype:
            print(self.filetype)
            filename = f'{self.hostname} {self.command}.{self.filetype}'
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            message.attach(part)
            text = message.as_string()
        else:
            print("if filetype is none")
            text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
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
        n=10
        for device in self.connect_device():
            for n in track(range(n), description='Connecting to devices'):
                device.connect(log_stdout=False)
        # Parse or Learn based on command
            if 'show' in self.command:
                try:
                    for n in track(range(n), description='Parsing Show Command'):
                        command_output = device.parse(self.command)
                except:
                    command_output = f"Cannot Parse { self.command }"
            elif self.command == "config":
                try:
                    for n in track(range(n), description='Parsing Show Config'):
                        command_output = device.learn(self.command)
                except:
                    command_output = f"Cannot Parse { self.command }"
            elif self.command == "platform":
                try:
                    for n in track(range(n), description='Parsing Show Platform'):
                        command_output = device.learn(self.command).to_dict()
                except:
                    command_output = f"Cannot Parse { self.command }"
            else:
                try:
                    for n in track(range(n), description='Parsing Learn Command'):
                        command_output = device.learn(self.command).info
                except:
                    command_output = f"Cannot Parse { self.command }"
            return(command_output)

@click.command()
@click.option('--hostname', prompt='Hostname', help='Hostname of device - must match the device', required=True)
@click.option('--os', prompt='OS', type=click.Choice(['ios', 'iosxe', 'iosxr', 'nxos'], case_sensitive=True), help='OS of device - must match the device', required=True)
@click.option('--username', prompt='Username', help='Username', required=True)
@click.option('--password', prompt=True, hide_input=True, help="User Password", required=True)
@click.option('--command', prompt='Command', help='A valid pyATS Learn Function (i.e. ospf) or valid CLI Show Command (i.e. "show ip interface brief")', required=True)
@click.option('--filetype', prompt='Filetype', type=click.Choice(['none','json','yaml','html','csv','markdown','pdf','svg'], case_sensitive=True), help='Filetype to output captured network state to', required=False, default='none')
@click.option('--from_email', prompt='From Email', help='Email address to send output from', required=False, default='none')
@click.option('--email_password', prompt='Email Password', hide_input=True, help='Email account password', required=False, default='none')
@click.option('--to_email', prompt='To Email', help='Email address to send output to', required=False, default='none')
def cli(hostname, os, username, password, command, filetype, from_email, email_password, to_email):
    invoke_class = GetJson(hostname, os, username, password, command, filetype, from_email, email_password, to_email)
    invoke_class.print_json()

if __name__ == "__main__":
    cli()