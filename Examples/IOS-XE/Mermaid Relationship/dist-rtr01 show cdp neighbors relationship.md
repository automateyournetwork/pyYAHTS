


```mermaid
erDiagram
    dist-rtr01 |o--|{ dist_sw02_9LQR5W39XQ2 : GigabitEthernet1
    dist_sw02_9LQR5W39XQ2 {
        Platform N9K-9000v
        PortID mgmt0
        Capability RSC
        HoldTime Seconds_178
    }
```

```mermaid
erDiagram
    dist-rtr01 |o--|{ dist_sw02_9LQR5W39XQ2 : GigabitEthernet5
    dist_sw02_9LQR5W39XQ2 {
        Platform N9K-9000v
        PortID Ethernet1/3
        Capability RSC
        HoldTime Seconds_173
    }
```

```mermaid
erDiagram
    dist-rtr01 |o--|{ dist_sw01_9SURZFD8MR6 : GigabitEthernet1
    dist_sw01_9SURZFD8MR6 {
        Platform N9K-9000v
        PortID mgmt0
        Capability RSC
        HoldTime Seconds_171
    }
```

```mermaid
erDiagram
    dist-rtr01 |o--|{ dist_sw01_9SURZFD8MR6 : GigabitEthernet4
    dist_sw01_9SURZFD8MR6 {
        Platform N9K-9000v
        PortID Ethernet1/3
        Capability RSC
        HoldTime Seconds_166
    }
```

```mermaid
erDiagram
    dist-rtr01 |o--|{ dist_rtr02_virl_info : GigabitEthernet6
    dist_rtr02_virl_info {
        Platform CSR1000V
        PortID GigabitEthernet6
        Capability RI
        HoldTime Seconds_137
    }
```

```mermaid
erDiagram
    dist-rtr01 |o--|{ dist_rtr02_virl_info : GigabitEthernet1
    dist_rtr02_virl_info {
        Platform CSR1000V
        PortID GigabitEthernet1
        Capability RI
        HoldTime Seconds_149
    }
```
