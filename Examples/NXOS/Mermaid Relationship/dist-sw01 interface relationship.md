
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/1 : VPC_Peer_Link
Ethernet1/1{
Enabled True
Operational_Status up
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode trunk
Type 100/1000/10000 Ethernet
Bandwidth x_1000000
Port_Speed x_1000
Duplex_Mode full
MTU x_9216
MAC_Address x_5254_000d_e744
Physical_Address x_5254_000d_e744
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False

Port_Channel_Interface Port-channel1


Port_Channel_Member True
Last_Change x_02_34_32
}
Ethernet1/1 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/10 : to
Ethernet1/10{
Enabled False
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e74d
Physical_Address x_5254_000d_e74d
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_02_34_49
}
Ethernet1/10 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/100 : N/A
Ethernet1/100{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a7
Physical_Address x_5254_000d_e7a7
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/100 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/101 : N/A
Ethernet1/101{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a8
Physical_Address x_5254_000d_e7a8
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/101 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/102 : N/A
Ethernet1/102{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a9
Physical_Address x_5254_000d_e7a9
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/102 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/103 : N/A
Ethernet1/103{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7aa
Physical_Address x_5254_000d_e7aa
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/103 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/104 : N/A
Ethernet1/104{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7ab
Physical_Address x_5254_000d_e7ab
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/104 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/105 : N/A
Ethernet1/105{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7ac
Physical_Address x_5254_000d_e7ac
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/105 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/106 : N/A
Ethernet1/106{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7ad
Physical_Address x_5254_000d_e7ad
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/106 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/107 : N/A
Ethernet1/107{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7ae
Physical_Address x_5254_000d_e7ae
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/107 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/108 : N/A
Ethernet1/108{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7af
Physical_Address x_5254_000d_e7af
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/108 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/109 : N/A
Ethernet1/109{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b0
Physical_Address x_5254_000d_e7b0
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/109 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/11 : Link_to_inside_host01
Ethernet1/11{
Enabled True
Operational_Status up
Access_VLAN VLAN_101
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_1000000
Port_Speed x_1000
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_000d_e74e
Physical_Address x_5254_000d_e74e
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_02_34_49
}
Ethernet1/11 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/110 : N/A
Ethernet1/110{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b1
Physical_Address x_5254_000d_e7b1
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/110 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/111 : N/A
Ethernet1/111{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b2
Physical_Address x_5254_000d_e7b2
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/111 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/112 : N/A
Ethernet1/112{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b3
Physical_Address x_5254_000d_e7b3
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/112 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/113 : N/A
Ethernet1/113{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b4
Physical_Address x_5254_000d_e7b4
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/113 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/114 : N/A
Ethernet1/114{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b5
Physical_Address x_5254_000d_e7b5
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/114 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/115 : N/A
Ethernet1/115{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b6
Physical_Address x_5254_000d_e7b6
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/115 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/116 : N/A
Ethernet1/116{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b7
Physical_Address x_5254_000d_e7b7
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/116 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/117 : N/A
Ethernet1/117{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b8
Physical_Address x_5254_000d_e7b8
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/117 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/118 : N/A
Ethernet1/118{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7b9
Physical_Address x_5254_000d_e7b9
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/118 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/119 : N/A
Ethernet1/119{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7ba
Physical_Address x_5254_000d_e7ba
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/119 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/12 : N/A
Ethernet1/12{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e74f
Physical_Address x_5254_000d_e74f
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/12 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/120 : N/A
Ethernet1/120{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7bb
Physical_Address x_5254_000d_e7bb
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/120 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/121 : N/A
Ethernet1/121{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7bc
Physical_Address x_5254_000d_e7bc
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/121 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/122 : N/A
Ethernet1/122{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7bd
Physical_Address x_5254_000d_e7bd
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/122 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/123 : N/A
Ethernet1/123{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7be
Physical_Address x_5254_000d_e7be
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/123 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/124 : N/A
Ethernet1/124{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7bf
Physical_Address x_5254_000d_e7bf
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/124 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/125 : N/A
Ethernet1/125{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7c0
Physical_Address x_5254_000d_e7c0
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/125 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/126 : N/A
Ethernet1/126{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7c1
Physical_Address x_5254_000d_e7c1
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/126 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/127 : N/A
Ethernet1/127{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7c2
Physical_Address x_5254_000d_e7c2
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/127 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/128 : N/A
Ethernet1/128{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7c3
Physical_Address x_5254_000d_e7c3
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/128 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/13 : N/A
Ethernet1/13{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e750
Physical_Address x_5254_000d_e750
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/13 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/14 : N/A
Ethernet1/14{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e751
Physical_Address x_5254_000d_e751
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/14 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/15 : N/A
Ethernet1/15{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e752
Physical_Address x_5254_000d_e752
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/15 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/16 : N/A
Ethernet1/16{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e753
Physical_Address x_5254_000d_e753
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/16 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/17 : N/A
Ethernet1/17{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e754
Physical_Address x_5254_000d_e754
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/17 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/18 : N/A
Ethernet1/18{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e755
Physical_Address x_5254_000d_e755
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/18 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/19 : N/A
Ethernet1/19{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e756
Physical_Address x_5254_000d_e756
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/19 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/2 : VPC_Peer_Link
Ethernet1/2{
Enabled True
Operational_Status up
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode trunk
Type 100/1000/10000 Ethernet
Bandwidth x_1000000
Port_Speed x_1000
Duplex_Mode full
MTU x_9216
MAC_Address x_5254_000d_e745
Physical_Address x_5254_000d_e745
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False

Port_Channel_Interface Port-channel1


Port_Channel_Member True
Last_Change x_02_34_33
}
Ethernet1/2 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/20 : N/A
Ethernet1/20{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e757
Physical_Address x_5254_000d_e757
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/20 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/21 : N/A
Ethernet1/21{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e758
Physical_Address x_5254_000d_e758
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/21 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/22 : N/A
Ethernet1/22{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e759
Physical_Address x_5254_000d_e759
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/22 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/23 : N/A
Ethernet1/23{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e75a
Physical_Address x_5254_000d_e75a
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/23 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/24 : N/A
Ethernet1/24{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e75b
Physical_Address x_5254_000d_e75b
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/24 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/25 : N/A
Ethernet1/25{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e75c
Physical_Address x_5254_000d_e75c
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/25 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/26 : N/A
Ethernet1/26{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e75d
Physical_Address x_5254_000d_e75d
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/26 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/27 : N/A
Ethernet1/27{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e75e
Physical_Address x_5254_000d_e75e
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/27 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/28 : N/A
Ethernet1/28{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e75f
Physical_Address x_5254_000d_e75f
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/28 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/29 : N/A
Ethernet1/29{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e760
Physical_Address x_5254_000d_e760
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/29 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/3 : L3_link_to_dist_rtr01
Ethernet1/3{
Enabled True
Operational_Status up
Type 100/1000/10000 Ethernet
Bandwidth x_1000000
Port_Speed x_1000
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_000d_e743
Physical_Address x_5254_000d_e746
IP_Address x_172_16_252_1_30
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_02_34_51
}
Ethernet1/3 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/30 : N/A
Ethernet1/30{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e761
Physical_Address x_5254_000d_e761
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/30 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/31 : N/A
Ethernet1/31{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e762
Physical_Address x_5254_000d_e762
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/31 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/32 : N/A
Ethernet1/32{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e763
Physical_Address x_5254_000d_e763
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/32 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/33 : N/A
Ethernet1/33{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e764
Physical_Address x_5254_000d_e764
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/33 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/34 : N/A
Ethernet1/34{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e765
Physical_Address x_5254_000d_e765
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/34 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/35 : N/A
Ethernet1/35{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e766
Physical_Address x_5254_000d_e766
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/35 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/36 : N/A
Ethernet1/36{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e767
Physical_Address x_5254_000d_e767
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/36 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/37 : N/A
Ethernet1/37{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e768
Physical_Address x_5254_000d_e768
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/37 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/38 : N/A
Ethernet1/38{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e769
Physical_Address x_5254_000d_e769
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/38 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/39 : N/A
Ethernet1/39{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e76a
Physical_Address x_5254_000d_e76a
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/39 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/4 : L3_link_to_dist_rtr02
Ethernet1/4{
Enabled True
Operational_Status up
Type 100/1000/10000 Ethernet
Bandwidth x_1000000
Port_Speed x_1000
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_000d_e743
Physical_Address x_5254_000d_e747
IP_Address x_172_16_252_5_30
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_02_34_51
}
Ethernet1/4 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/40 : N/A
Ethernet1/40{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e76b
Physical_Address x_5254_000d_e76b
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/40 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/41 : N/A
Ethernet1/41{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e76c
Physical_Address x_5254_000d_e76c
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/41 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/42 : N/A
Ethernet1/42{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e76d
Physical_Address x_5254_000d_e76d
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/42 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/43 : N/A
Ethernet1/43{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e76e
Physical_Address x_5254_000d_e76e
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/43 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/44 : N/A
Ethernet1/44{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e76f
Physical_Address x_5254_000d_e76f
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/44 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/45 : N/A
Ethernet1/45{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e770
Physical_Address x_5254_000d_e770
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/45 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/46 : N/A
Ethernet1/46{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e771
Physical_Address x_5254_000d_e771
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/46 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/47 : N/A
Ethernet1/47{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e772
Physical_Address x_5254_000d_e772
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/47 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/48 : N/A
Ethernet1/48{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e773
Physical_Address x_5254_000d_e773
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/48 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/49 : N/A
Ethernet1/49{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e774
Physical_Address x_5254_000d_e774
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/49 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/5 : to
Ethernet1/5{
Enabled False
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e748
Physical_Address x_5254_000d_e748
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_02_34_51
}
Ethernet1/5 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/50 : N/A
Ethernet1/50{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e775
Physical_Address x_5254_000d_e775
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/50 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/51 : N/A
Ethernet1/51{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e776
Physical_Address x_5254_000d_e776
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/51 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/52 : N/A
Ethernet1/52{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e777
Physical_Address x_5254_000d_e777
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/52 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/53 : N/A
Ethernet1/53{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e778
Physical_Address x_5254_000d_e778
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/53 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/54 : N/A
Ethernet1/54{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e779
Physical_Address x_5254_000d_e779
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/54 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/55 : N/A
Ethernet1/55{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e77a
Physical_Address x_5254_000d_e77a
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/55 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/56 : N/A
Ethernet1/56{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e77b
Physical_Address x_5254_000d_e77b
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/56 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/57 : N/A
Ethernet1/57{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e77c
Physical_Address x_5254_000d_e77c
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/57 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/58 : N/A
Ethernet1/58{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e77d
Physical_Address x_5254_000d_e77d
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/58 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/59 : N/A
Ethernet1/59{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e77e
Physical_Address x_5254_000d_e77e
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/59 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/6 : to
Ethernet1/6{
Enabled False
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e749
Physical_Address x_5254_000d_e749
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_02_34_51
}
Ethernet1/6 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/60 : N/A
Ethernet1/60{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e77f
Physical_Address x_5254_000d_e77f
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/60 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/61 : N/A
Ethernet1/61{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e780
Physical_Address x_5254_000d_e780
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/61 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/62 : N/A
Ethernet1/62{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e781
Physical_Address x_5254_000d_e781
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/62 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/63 : N/A
Ethernet1/63{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e782
Physical_Address x_5254_000d_e782
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/63 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/64 : N/A
Ethernet1/64{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e783
Physical_Address x_5254_000d_e783
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/64 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/65 : N/A
Ethernet1/65{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e784
Physical_Address x_5254_000d_e784
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/65 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/66 : N/A
Ethernet1/66{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e785
Physical_Address x_5254_000d_e785
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/66 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/67 : N/A
Ethernet1/67{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e786
Physical_Address x_5254_000d_e786
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/67 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/68 : N/A
Ethernet1/68{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e787
Physical_Address x_5254_000d_e787
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/68 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/69 : N/A
Ethernet1/69{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e788
Physical_Address x_5254_000d_e788
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/69 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/7 : to
Ethernet1/7{
Enabled False
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e74a
Physical_Address x_5254_000d_e74a
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_02_34_50
}
Ethernet1/7 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/70 : N/A
Ethernet1/70{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e789
Physical_Address x_5254_000d_e789
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/70 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/71 : N/A
Ethernet1/71{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e78a
Physical_Address x_5254_000d_e78a
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/71 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/72 : N/A
Ethernet1/72{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e78b
Physical_Address x_5254_000d_e78b
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/72 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/73 : N/A
Ethernet1/73{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e78c
Physical_Address x_5254_000d_e78c
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/73 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/74 : N/A
Ethernet1/74{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e78d
Physical_Address x_5254_000d_e78d
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/74 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/75 : N/A
Ethernet1/75{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e78e
Physical_Address x_5254_000d_e78e
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/75 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/76 : N/A
Ethernet1/76{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e78f
Physical_Address x_5254_000d_e78f
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/76 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/77 : N/A
Ethernet1/77{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e790
Physical_Address x_5254_000d_e790
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/77 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/78 : N/A
Ethernet1/78{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e791
Physical_Address x_5254_000d_e791
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/78 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/79 : N/A
Ethernet1/79{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e792
Physical_Address x_5254_000d_e792
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/79 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/8 : to
Ethernet1/8{
Enabled False
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e74b
Physical_Address x_5254_000d_e74b
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_02_34_50
}
Ethernet1/8 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/80 : N/A
Ethernet1/80{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e793
Physical_Address x_5254_000d_e793
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/80 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/81 : N/A
Ethernet1/81{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e794
Physical_Address x_5254_000d_e794
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/81 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/82 : N/A
Ethernet1/82{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e795
Physical_Address x_5254_000d_e795
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/82 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/83 : N/A
Ethernet1/83{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e796
Physical_Address x_5254_000d_e796
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/83 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/84 : N/A
Ethernet1/84{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e797
Physical_Address x_5254_000d_e797
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/84 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/85 : N/A
Ethernet1/85{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e798
Physical_Address x_5254_000d_e798
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/85 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/86 : N/A
Ethernet1/86{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e799
Physical_Address x_5254_000d_e799
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/86 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/87 : N/A
Ethernet1/87{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e79a
Physical_Address x_5254_000d_e79a
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/87 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/88 : N/A
Ethernet1/88{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e79b
Physical_Address x_5254_000d_e79b
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/88 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/89 : N/A
Ethernet1/89{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e79c
Physical_Address x_5254_000d_e79c
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/89 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/9 : to
Ethernet1/9{
Enabled False
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e74c
Physical_Address x_5254_000d_e74c
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_02_34_50
}
Ethernet1/9 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/90 : N/A
Ethernet1/90{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e79d
Physical_Address x_5254_000d_e79d
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/90 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/91 : N/A
Ethernet1/91{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e79e
Physical_Address x_5254_000d_e79e
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/91 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/92 : N/A
Ethernet1/92{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e79f
Physical_Address x_5254_000d_e79f
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/92 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/93 : N/A
Ethernet1/93{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a0
Physical_Address x_5254_000d_e7a0
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/93 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/94 : N/A
Ethernet1/94{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a1
Physical_Address x_5254_000d_e7a1
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/94 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/95 : N/A
Ethernet1/95{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a2
Physical_Address x_5254_000d_e7a2
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/95 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/96 : N/A
Ethernet1/96{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a3
Physical_Address x_5254_000d_e7a3
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/96 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/97 : N/A
Ethernet1/97{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a4
Physical_Address x_5254_000d_e7a4
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/97 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/98 : N/A
Ethernet1/98{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a5
Physical_Address x_5254_000d_e7a5
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/98 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Ethernet1/99 : N/A
Ethernet1/99{
Enabled True
Operational_Status down
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode access
Type 100/1000/10000 Ethernet
Bandwidth x_10000000
MTU x_1500
MAC_Address x_5254_000d_e7a6
Physical_Address x_5254_000d_e7a6
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
Last_Change x_never
}
Ethernet1/99 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Loopback0 : to
Loopback0{
Enabled False
Operational_Status down
Bandwidth x_8000000
MTU x_1500
Medium broadcast
Delay x_5000
Encapsulation loopback


Port_Channel_Member False
}
Loopback0 |o--|{ Counters : counters
Counters {
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Mgmt0 : to_port8_sandbox_backend
Mgmt0{
Enabled True
Operational_Status up
Type Ethernet
Bandwidth x_1000000
Auto_Negotiate True
Port_Speed x_1000
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_000d_e73c
Physical_Address x_5254_000d_e73c
IP_Address x_10_10_20_177_24
Medium broadcast
Delay x_10
Encapsulation arpa


Port_Channel_Member False
}
Mgmt0 |o--|{ Counters : counters
Counters {
Input_Broadcast x_9
Input_Multicast x_315
Input_Octects x_4920729
Input_Unicast x_13523
Input_Packets x_14302
Input_Rate x_17592
Load_Interval x_1
Output_Rate x_189896
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Null0 : N/A
Null0{
Enabled N/A
Operational_Status N/A
}
Null0 |o--|{ Counters : counters
Counters {
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Port-channel1 : N/A
Port-channel1{
Enabled True
Operational_Status up
Access_VLAN VLAN_1
Native_VLAN VLAN_1
Switchport_Enable True
Switchport_Mode trunk
Bandwidth x_2000000
Port_Speed x_1000
Duplex_Mode full
MTU x_9216
Medium broadcast
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Member Ethernet1/1
Member Ethernet1/2

}
Port-channel1 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Unicast x_0
Input_Unknown x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Discards x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Unicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Vlan1 : N/A
Vlan1{
Enabled False
Operational_Status down
Type EtherSVI
Bandwidth x_1000000
MTU x_1500
MAC_Address x_5254_000d_e743
Delay x_10
Encapsulation arpa


Port_Channel_Member False
}
Vlan1 |o--|{ Counters : counters
Counters {
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Vlan101 : prod_svi_
Vlan101{
Enabled True
Operational_Status up
Type EtherSVI
Bandwidth x_1000000
MTU x_1500
MAC_Address x_5254_000d_e743
IP_Address x_172_16_101_2_24
Delay x_10
Encapsulation arpa


Port_Channel_Member False
}
Vlan101 |o--|{ Counters : counters
Counters {
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Vlan102 : dev_svi_
Vlan102{
Enabled True
Operational_Status up
Type EtherSVI
Bandwidth x_1000000
MTU x_1500
MAC_Address x_5254_000d_e743
IP_Address x_172_16_102_2_24
Delay x_10
Encapsulation arpa


Port_Channel_Member False
}
Vlan102 |o--|{ Counters : counters
Counters {
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Vlan103 : test_svi_
Vlan103{
Enabled True
Operational_Status up
Type EtherSVI
Bandwidth x_1000000
MTU x_1500
MAC_Address x_5254_000d_e743
IP_Address x_172_16_103_2_24
Delay x_10
Encapsulation arpa


Port_Channel_Member False
}
Vlan103 |o--|{ Counters : counters
Counters {
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Vlan104 : security_svi_
Vlan104{
Enabled True
Operational_Status up
Type EtherSVI
Bandwidth x_1000000
MTU x_1500
MAC_Address x_5254_000d_e743
IP_Address x_172_16_104_2_24
Delay x_10
Encapsulation arpa


Port_Channel_Member False
}
Vlan104 |o--|{ Counters : counters
Counters {
}
```
```mermaid
erDiagram
dist-sw01 |o--|{ Vlan105 : iot_svi_
Vlan105{
Enabled True
Operational_Status up
Type EtherSVI
Bandwidth x_1000000
MTU x_1500
MAC_Address x_5254_000d_e743
IP_Address x_172_16_105_2_24
Delay x_10
Encapsulation arpa


Port_Channel_Member False
}
Vlan105 |o--|{ Counters : counters
Counters {
}
```