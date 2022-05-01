
| VRF | Address Family | Route | Active | Metric | Next Hop Index | Next Hop | Outgoing Interface | Route Preference | Source Protocol |
| --- | -------------- | ----- | ------ | ------ | -------------- | -------- | -------------------| ---------------- | --------------- |
| default | ipv4 | 172.16.101.0/24 | True | 0 | 1 | 172.16.101.2 | N/A | 0 | direct |
| default | ipv4 | 172.16.101.1/32 | True | 0 | 1 | 172.16.101.1 | N/A | 0 | hsrp |
| default | ipv4 | 172.16.101.2/32 | True | 0 | 1 | 172.16.101.2 | N/A | 0 | local |
| default | ipv4 | 172.16.102.0/24 | True | 0 | 1 | 172.16.102.2 | N/A | 0 | direct |
| default | ipv4 | 172.16.102.1/32 | True | 0 | 1 | 172.16.102.1 | N/A | 0 | hsrp |
| default | ipv4 | 172.16.102.2/32 | True | 0 | 1 | 172.16.102.2 | N/A | 0 | local |
| default | ipv4 | 172.16.103.0/24 | True | 0 | 1 | 172.16.103.2 | N/A | 0 | direct |
| default | ipv4 | 172.16.103.1/32 | True | 0 | 1 | 172.16.103.1 | N/A | 0 | hsrp |
| default | ipv4 | 172.16.103.2/32 | True | 0 | 1 | 172.16.103.2 | N/A | 0 | local |
| default | ipv4 | 172.16.104.0/24 | True | 0 | 1 | 172.16.104.2 | N/A | 0 | direct |
| default | ipv4 | 172.16.104.1/32 | True | 0 | 1 | 172.16.104.1 | N/A | 0 | hsrp |
| default | ipv4 | 172.16.104.2/32 | True | 0 | 1 | 172.16.104.2 | N/A | 0 | local |
| default | ipv4 | 172.16.105.0/24 | True | 0 | 1 | 172.16.105.2 | N/A | 0 | direct |
| default | ipv4 | 172.16.105.1/32 | True | 0 | 1 | 172.16.105.1 | N/A | 0 | hsrp |
| default | ipv4 | 172.16.105.2/32 | True | 0 | 1 | 172.16.105.2 | N/A | 0 | local |
| default | ipv4 | 172.16.252.0/30 | True | 0 | 1 | 172.16.252.1 | N/A | 0 | direct |
| default | ipv4 | 172.16.252.1/32 | True | 0 | 1 | 172.16.252.1 | N/A | 0 | local |
| default | ipv4 | 172.16.252.12/30 | True | 41 | 1 | 172.16.252.6 | N/A | 110 | ospf |
| default | ipv4 | 172.16.252.16/30 | True | 41 | 1 | 172.16.252.2 | N/A | 110 | ospf |
| default | ipv4 | 172.16.252.16/30 | True | 41 | 2 | 172.16.252.6 | N/A | 110 | ospf |
| default | ipv4 | 172.16.252.20/30 | True | 41 | 1 | 172.16.252.2 | N/A | 110 | ospf |
| default | ipv4 | 172.16.252.24/30 | True | 41 | 1 | 172.16.252.2 | N/A | 110 | ospf |
| default | ipv4 | 172.16.252.28/30 | True | 41 | 1 | 172.16.252.6 | N/A | 110 | ospf |
| default | ipv4 | 172.16.252.32/30 | True | 41 | 1 | 172.16.252.6 | N/A | 110 | ospf |
| default | ipv4 | 172.16.252.4/30 | True | 0 | 1 | 172.16.252.5 | N/A | 0 | direct |
| default | ipv4 | 172.16.252.5/32 | True | 0 | 1 | 172.16.252.5 | N/A | 0 | local |
| default | ipv4 | 172.16.252.8/30 | True | 41 | 1 | 172.16.252.2 | N/A | 110 | ospf |
| management | ipv4 | 0.0.0.0/0 | True | 0 | 1 | 10.10.20.254 | N/A | 1 | static |
| management | ipv4 | 10.10.20.0/24 | True | 0 | 1 | 10.10.20.177 | N/A | 0 | direct |
| management | ipv4 | 10.10.20.177/32 | True | 0 | 1 | 10.10.20.177 | N/A | 0 | local |