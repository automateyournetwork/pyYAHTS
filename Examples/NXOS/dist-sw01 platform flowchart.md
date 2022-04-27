
```mermaid
flowchart LR;
dist-sw01 <--> Nexus9000_9000v <--> Nexus9000_9000v_Chassis <--> SN_9SURZFD8MR6 <--> Image_bootflash:///nxos.9.2.4.bin <--> NX-OS <--> 9.2.4
```
```mermaid
flowchart LR;
dist-sw01  <--> Slot_Nexus_9000v_Ethernet_Module <--> SN_9SURZFD8MR6
```
```mermaid
flowchart LR;
dist-sw01  <--> Slot_N9K-9000v <--> SN_9SURZFD8MR6 <--> bootflash:/nxos.9.2.4.bin 
```