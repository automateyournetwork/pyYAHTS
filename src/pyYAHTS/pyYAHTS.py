import sys
import os
import json
import logging
import smtplib
import ssl
import webbrowser
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from gtts import gTTS
import rich_click as click
import yaml
import networkx as nx
import pandas as pd
from pyats.topology import Testbed, Device
from genie import testbed
from rich import print_json
from rich.console import Console
from rich.progress import track
from json2table import convert
from jinja2 import Environment, FileSystemLoader
from fpdf import FPDF
from pyvis.network import Network

class GetJson():
    def __init__(self,
                hostname,
                os,
                username,
                password,
                command,
                filetype,
                from_email,
                email_password,
                to_email,
                verbose):
        self.hostname = hostname
        self.os = os
        self.username = username
        self.password = password
        self.command = command
        self.filetype = filetype
        self.from_email = from_email
        self.email_password = email_password
        self.to_email = to_email
        self.verbose = verbose
        if self.os == "nxos":
            self.supported_templates = ['acl',
                            'arp',
                            'bgp',
                            'hsrp',
                            'interface',
                            'lldp',
                            'ntp',
                            'ospf',
                            'platform',
                            'routing',
                            'vlan',
                            'vrf',
                            'show access-lists',
                            'show bgp process vrf all',
                            'show bgp sessions',
                            'show cdp neighbors',
                            'show cdp neighbors detail',
                            'show environment',
                            'show interface',
                            'show interface status',
                            'show interface transceiver',
                            'show inventory',
                            'show ip arp vrf all',
                            'show ip interface brief',
                            'show ip ospf',
                            'show ip ospf interface',
                            'show ip ospf interface vrf all',
                            'show ip ospf neighbors detail',
                            'show ip ospf neighbors detail vrf all',
                            'show ip route',
                            'show ip route vrf all',
                            'show mac address-table',
                            'show port-channel summary',
                            'show version',
                            'show vlan']
        else:
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
                            'show inventory',
                            'show ip arp',
                            'show ip interface brief',
                            'show ip ospf',
                            'show ip ospf database',
                            'show ip ospf interface',
                            'show ip ospf neighbor',
                            'show ip ospf neighbor detail',
                            'show ip route',
                            'show license summary',
                            'show mac address-table',
                            'show ntp associations',
                            'show version',
                            'show vlan',
                            'show vrf']

    def print_json(self):
        if self.command == "all":
            for single_command in self.supported_templates:
                self.command = single_command
                parsed_json = json.dumps(self.capture_state(), indent=4, sort_keys=True)
                print_json(parsed_json)
                if "Cannot" in parsed_json:
                    click.secho("No Data To Create File", fg='red')
                else:
                    if self.filetype:
                        self.pick_filetype(parsed_json)
                    if (self.from_email != 'none'
                        and self.email_password != 'none'
                        and self.to_email != 'none'):
                        self.send_email(parsed_json)
        else:
            parsed_json = json.dumps(self.capture_state(), indent=4, sort_keys=True)
            print_json(parsed_json)
            if "Cannot" in parsed_json:
                click.secho("No Data To Create File", fg='red')
            else:
                if self.filetype:
                    self.pick_filetype(parsed_json)
                if (self.from_email != 'none'
                    and self.email_password != 'none'
                    and self.to_email != 'none'):
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
        elif self.filetype == 'pdf':
            self.pdf_file(parsed_json)
        elif self.filetype == 'markdown':
            self.markdown_file(parsed_json)
        elif self.filetype == 'csv':
            self.csv_file(parsed_json)
        elif self.filetype == 'svg':
            self.svg_file(parsed_json)
        elif self.filetype == 'graph':
            self.graph_file(parsed_json)
        elif self.filetype == 'mindmap':
            self.mindmap_file(parsed_json)
        elif self.filetype == 'flowchart':
            self.flowchart_file(parsed_json)
        elif self.filetype == 'class':
            self.class_file(parsed_json)
        elif self.filetype == 'state':
            self.state_file(parsed_json)
        elif self.filetype == 'relationship':
            self.relationship_file(parsed_json)
        elif self.filetype == 'piechart':
            self.piechart_file(parsed_json)
        elif self.filetype == 'mp3':
            self.mp3_file(parsed_json)            
        elif self.filetype == 'all':
            self.all_files(parsed_json)

    def json_file(self, parsed_json):
        with open(f'{self.hostname} {self.command}.json', 'w') as f:
            f.write(parsed_json)
        click.secho(f"JSON file created at { sys.path[0] }/{self.hostname} {self.command}.json",
        fg='green')

    def yaml_file(self, parsed_json):
        clean_yaml = yaml.dump(json.loads(parsed_json), default_flow_style=False)
        with open(f'{self.hostname} {self.command}.yaml', 'w') as f:
            f.write(clean_yaml)
        click.secho(f"YAML file created at { sys.path[0] }/{self.hostname} {self.command}.yaml",
        fg='green')

    def html_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                html_template = env.get_template(f'{self.os} html.j2')
                html_output = html_template.render(command = self.command,
                    data_to_template=json.loads(parsed_json))
                with open(f'{self.hostname} {self.command}.html', 'w') as f:
                    f.write(html_output)
                break
            else:
                good_json = json.loads(parsed_json)
                build_direction = "TOP_TO_BOTTOM"
                table_attributes = {"style" : "width:100%"}
                html_version = convert(good_json,
                    build_direction=build_direction,
                    table_attributes=table_attributes)
                with open(f'{self.hostname} {self.command}.html', 'w') as f:
                    f.write(html_version)
        click.secho(f"HTML file created at { sys.path[0] }/{self.hostname} {self.command}.html",
            fg='green')

    def pdf_file(self, parsed_json):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size = 6)
        pdf.cell(200, 10, txt = f"{self.hostname} {self.command}", ln = 1, align = 'C')
        pdf.multi_cell(200, 10, txt = parsed_json)
        pdf.output(f'{self.hostname} {self.command}.pdf')
        click.secho(f"PDF file created at { sys.path[0] }/{self.hostname} {self.command}.pdf",
            fg='green')

    def markdown_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                markdown_template = env.get_template(f'{self.os} md.j2')
                markdown_output = markdown_template.render(command = self.command,
                    data_to_template=json.loads(parsed_json))
                with open(f'{self.hostname} {self.command}.md', 'w') as f:
                    f.write(markdown_output)
                break
            else:
                df = pd.json_normalize(json.loads(parsed_json),max_level=2)
                markdown_table = df.to_markdown(index='false')
                with open(f'{self.hostname} {self.command}.md', 'w') as f:
                    f.write(markdown_table)
        click.secho(f"Markdown file created at { sys.path[0] }/{self.hostname} {self.command}.md",
            fg='green')

    def csv_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                csv_template = env.get_template(f'{self.os} csv.j2')
                csv_output = csv_template.render(command = self.command,
                    data_to_template=json.loads(parsed_json),
                    hostname=self.hostname)
                with open(f'{self.hostname} {self.command}.csv', 'w') as f:
                    f.write(csv_output)
                break
            else:
                df = pd.json_normalize(json.loads(parsed_json))
                df.to_csv(f'{self.hostname} {self.command}.csv', index=False)
        click.secho(f"CSV file created at { sys.path[0] }/{self.hostname} {self.command}.csv",
            fg='green')

    def svg_file(self, parsed_json):
        console = Console(record=True)
        console.print(parsed_json)
        console.save_svg(f"{self.hostname} {self.command}.svg",
            title=f"{self.hostname} {self.command}")
        click.secho(f"SVG file created at { sys.path[0] }/{self.hostname} {self.command}.svg",
            fg='green')

    def graph_csv_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                graph_csv_template = env.get_template(f'{self.os} graph_csv.j2')
                graph_csv_output = graph_csv_template.render(command = self.command,
                    data_to_template=json.loads(parsed_json),
                    hostname=self.hostname)
                with open(f'{self.hostname} {self.command}_graph.csv', 'w') as f:
                    f.write(graph_csv_output)
                break

    def graph_file(self, parsed_json):
        self.graph_csv_file(parsed_json)
        df = pd.read_csv(f'{self.hostname} {self.command}_graph.csv')
        G = nx.from_pandas_edgelist(df,source='Source',target="Target",edge_attr=True)
        net = Network(notebook=True, width=1500, height=1000)
        net.show_buttons(True)
        net.from_nx(G)
        net.show(f'{self.hostname} {self.command} graph.html')
        os.remove(f'{self.hostname} {self.command}_graph.csv')
        click.secho(
            f"Network Graph file created at { sys.path[0] }/{self.hostname} {self.command}.md",
            fg='green')

    def mindmap_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                mindmap_template = env.get_template(f'{self.os} mindmap.j2')
                mindmap_output = mindmap_template.render(command = self.command,
                    data_to_template=json.loads(parsed_json),
                    hostname=self.hostname)
                with open(f'{self.hostname} {self.command} mindmap.md', 'w') as f:
                    f.write(mindmap_output)
                click.secho(
                    f"Mindmap file created at { sys.path[0] }/{self.hostname} {self.command}.md",
                    fg='green')
                break

    def flowchart_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                flowchart_template = env.get_template(f'{self.os} flowchart.j2')
                flowchart_output = flowchart_template.render(hostname = self.hostname,
                    command = self.command,
                    data_to_template=json.loads(parsed_json))
                with open(f'{self.hostname} {self.command} flowchart.md', 'w') as f:
                    f.write(flowchart_output)
                click.secho(
                    f"Mermaid Flowchart file created at { sys.path[0] }/{self.hostname} {self.command}.md",
                    fg='green')
                break

    def class_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                class_template = env.get_template(f'{self.os} class.j2')
                class_output = class_template.render(hostname = self.hostname,
                    command = self.command,
                    data_to_template=json.loads(parsed_json))
                with open(f'{self.hostname} {self.command} class.md', 'w') as f:
                    f.write(class_output)
                click.secho(
                    f"Mermaid Class file created at { sys.path[0] }/{self.hostname} {self.command}.md",
                    fg='green')
                break

    def state_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                state_template = env.get_template(f'{self.os} state.j2')
                state_output = state_template.render(hostname = self.hostname,
                    command = self.command,
                    data_to_template=json.loads(parsed_json))
                with open(f'{self.hostname} {self.command} state.md', 'w') as f:
                    f.write(state_output)
                click.secho(
                    f"Mermaid State file created at { sys.path[0] }/{self.hostname} {self.command}.md",
                    fg='green')
                break

    def relationship_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                relationship_template = env.get_template(f'{self.os} relationship.j2')
                relationship_output = relationship_template.render(hostname = self.hostname,
                    command = self.command,
                    data_to_template=json.loads(parsed_json))
                with open(f'{self.hostname} {self.command} relationship.md', 'w') as f:
                    f.write(relationship_output)
                click.secho(
                    f"Mermaid Relationship file created at { sys.path[0] }/{self.hostname} {self.command}.md",
                    fg='green')
                break

    def piechart_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                pie_template = env.get_template(f'{self.os} pie.j2')
                pie_output = pie_template.render(hostname = self.hostname,
                    command = self.command,
                    data_to_template=json.loads(parsed_json))
                with open(f'{self.hostname} {self.command} piechart.md', 'w') as f:
                    f.write(pie_output)
                click.secho(
                    f"Mermaid Piechart file created at { sys.path[0] }/{self.hostname} {self.command}.md",
                    fg='green')
                break

    def mp3_file(self, parsed_json):
        for template in self.supported_templates:
            if self.command == template:
                template_dir = Path(__file__).resolve().parent
                env = Environment(loader=FileSystemLoader(str(template_dir)))
                mp3_template = env.get_template(f'{self.os} mp3.j2')
                mp3_output = mp3_template.render(hostname = self.hostname,
                    command = self.command,
                    data_to_template=json.loads(parsed_json))
                language = 'en-US'
                mp3 = gTTS(text = mp3_output, lang=language)
                # Save MP3
                mp3.save(f'{self.hostname} {self.command}.mp3')
                click.secho(
                    f"MP3 file created at { sys.path[0] }/{self.hostname} {self.command}.md",
                    fg='green')
                webbrowser.open(f"{self.hostname} {self.command}.mp3")
                break

    def all_files(self, parsed_json):
        self.json_file(parsed_json)
        self.yaml_file(parsed_json)
        self.html_file(parsed_json)
        self.pdf_file(parsed_json)
        self.markdown_file(parsed_json)
        self.csv_file(parsed_json)
        self.graph_file(parsed_json)
        self.mindmap_file(parsed_json)
        self.flowchart_file(parsed_json)
        self.class_file(parsed_json)
        self.state_file(parsed_json)
        self.relationship_file(parsed_json)
        self.piechart_file(parsed_json)
        self.mp3_file(parsed_json)
        self.svg_file(parsed_json)

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
        return new_testbed

    def capture_state(self):
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        n=10
        for device in self.connect_device():
            if self.verbose:
                device.connect(learn_hostname=True,log_stdout=True)
            else:
                for n in track(range(n), description='Connecting to devices'):
                    device.connect(learn_hostname=True,log_stdout=False)
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
            device.disconnect()
            return command_output

@click.command()
@click.option('--hostname',
    prompt='Hostname',
    help='Hostname of device - must match the device',
    required=True, envvar="HOSTNAME")
@click.option('--os',
    prompt='OS',
    type=click.Choice(['ios', 'iosxe', 'iosxr', 'nxos'],
        case_sensitive=True),
    help='OS of device - must match the device',
    required=True,
    envvar="OS")
@click.option('--username',
    prompt='Username',
    help='Username',
    required=True,
    envvar="USERNAME")
@click.option('--password',
    prompt=True,
    hide_input=True,
    help="User Password",
    required=True,
    envvar="PASSWORD")
@click.option('--command',
    prompt='Command',
    help=('''A valid pyATS Learn Function (i.e. ospf)
             or valid CLI Show Command (i.e. "show ip interface brief")'''),
    required=True)
@click.option('--filetype',
    prompt='Filetype',
    type=click.Choice(['none',
                        'json',
                        'yaml',
                        'html',
                        'csv',
                        'markdown',
                        'pdf',
                        'svg',
                        'graph',
                        'mindmap',
                        'flowchart',
                        'class',
                        'state',
                        'relationship',
                        'piechart',
                        'mp3',
                        'all'],
        case_sensitive=True),
    help='Filetype to output captured network state to',
    required=False,
    default='none')
@click.option('--from_email',
    help='Email address to send output from',
    required=False,
    default='none')
@click.option('--email_password',
    hide_input=True,
    help='Email account password',
    required=False,
    default='none')
@click.option('--to_email',
    help='Email address to send output to',
    required=False,
    default='none')
@click.option('-v','--verbose',
    help='Display pyATS Logging',
    required=False,
    is_flag=True)
def cli(hostname,
        os,
        username,
        password,
        command,
        filetype,
        from_email,
        email_password,
        to_email,
        verbose):
    invoke_class = GetJson(hostname,
                            os,
                            username,
                            password,
                            command,
                            filetype,
                            from_email,
                            email_password,
                            to_email,
                            verbose)
    invoke_class.print_json()

if __name__ == "__main__":
    cli()
