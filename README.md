# pyYAHTS
An interpretation of pyATS

pyYAHTS is a dyanmic, on-demand, YAML-free / testbed.yaml free, implementation of pyATS. 

It works with any IOS / IOS-XE / IOS-XR / NXOS device!

The results are Rich JSON printed to the screen

## Requirements
pyYAHTS is an extension of pyATS, which is required, and only runs on Linux operating systems
## Installation

1. pip install pyYAHTS

## Getting Started

pyYAHTS works on any Cisco OS IOS / IOS-XE / IOS-XR / NXOS

pyYAHTS requires the follow options be speficied at runtime:

1. Hostname of the device - must exactly match the configured hostname
2. Operating System - Either ios, iosxe, iosxr, or nxos
3. Username
4. Password
5. Either a pyATS Learn Function, such as ospf, or any supported pyATS Parsed CLI Show Command, such as "show ip interface brief"

![Help](images/help01.png)

For a list of supported Learn Functions please visit [Available Learn Functions](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models)

![Available Learn Functions](/images/available_learn_functions.png)

For a list of supported Parsers please visit [Available Show Command Parsers](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers)

![Available Show Parsers](/images/available_show_parsers01.png)

A sample of "Show IP Interface" Parsers for IOS-XE
![IOS-XE Show IP Interface Sample](/images/available_show_parsers02.png)


## Using pyYAHTS

In any virtual environment with pyATS installed pyYAHTS can be executed several ways

1. Prompted Inputs

```python
(virtualenv)$ pyYAHTS
Hostname: dist-sw01
OS (ios, iosxe, iosxr, nxos): nxos
Username: cisco
Password:
Command: ospf
```

2. Directly supplying options

```python
(virtualenv)$ pyYAHTS --hostname dist-sw01 --os nxos --username cisco --password cisco --command ospf
```

3. Mixing supplied options and prompted responses

```python
(virtualenv)$ pyYAHTS --hostname dist-sw01 --os nxos --username cisco --password cisco
Command: ospf
```

## Creating JSON files

Of course you can also redirect the printed output to a JSON file! 

```python
pyYAHTS --hostname dist-sw01 --os nxos --username cisco --password cisco --command ospf > dist_sw01_learned_ospf.json
```
## Help

pyYAHTS includes a handy Rich Click Help! Simple type:

```python
$ pyYAHTS --help
```

![More Help](images/help01.png)

## Contact

Please reach out on Twitter [Twitter](https://twitter.com/john_capobianco) or open an issue if you hit any snags or have any questions!