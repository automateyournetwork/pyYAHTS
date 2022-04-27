

```mermaid
erDiagram
dist-rtr01 |o--|{ GigabitEthernet1 : to_port6_sandbox_backend
GigabitEthernet1{
Enabled True
Operational_Status up
Switchport_Enable False
Type CSR vNIC
Bandwidth x_1000000
Auto_Negotiate True
Port_Speed x_1000mbps
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_001f_b4db
Physical_Address x_5254_001f_b4db
IP_Address x_10_10_20_175_24
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
}
GigabitEthernet1 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_3317068
Input_Packets x_48460
Output_Broadcast x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Packets x_47090
Last_Clear x_never
Input_Rate x_8000
Load_Interval x_300
Output_Rate x_21000
}
```
```mermaid
erDiagram
dist-rtr01 |o--|{ GigabitEthernet2 : L3_Link_to_core_rtr01
GigabitEthernet2{
Enabled True
Operational_Status up
Switchport_Enable False
Type CSR vNIC
Bandwidth x_1000000
Auto_Negotiate True
Port_Speed x_1000mbps
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_001e_d479
Physical_Address x_5254_001e_d479
IP_Address x_172_16_252_21_30
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
}
GigabitEthernet2 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Packets x_888
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-rtr01 |o--|{ GigabitEthernet3 : L3_Link_to_core_rtr02
GigabitEthernet3{
Enabled True
Operational_Status up
Switchport_Enable False
Type CSR vNIC
Bandwidth x_1000000
Auto_Negotiate True
Port_Speed x_1000mbps
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_0006_f7ce
Physical_Address x_5254_0006_f7ce
IP_Address x_172_16_252_25_30
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
}
GigabitEthernet3 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Packets x_888
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-rtr01 |o--|{ GigabitEthernet4 : L3_Link_to_dist_sw01
GigabitEthernet4{
Enabled True
Operational_Status up
Switchport_Enable False
Type CSR vNIC
Bandwidth x_1000000
Auto_Negotiate True
Port_Speed x_1000mbps
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_000e_7bb9
Physical_Address x_5254_000e_7bb9
IP_Address x_172_16_252_2_30
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
}
GigabitEthernet4 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_123900
Input_Packets x_1126
Output_Broadcast x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Packets x_933
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-rtr01 |o--|{ GigabitEthernet5 : L3_Link_to_dist_sw02
GigabitEthernet5{
Enabled True
Operational_Status up
Switchport_Enable False
Type CSR vNIC
Bandwidth x_1000000
Auto_Negotiate True
Port_Speed x_1000mbps
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_0016_7077
Physical_Address x_5254_0016_7077
IP_Address x_172_16_252_10_30
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
}
GigabitEthernet5 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_109414
Input_Packets x_1069
Output_Broadcast x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Packets x_930
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-rtr01 |o--|{ GigabitEthernet6 : L3_Link_to_dist_rtr02
GigabitEthernet6{
Enabled True
Operational_Status up
Switchport_Enable False
Type CSR vNIC
Bandwidth x_1000000
Auto_Negotiate True
Port_Speed x_1000mbps
Duplex_Mode full
MTU x_1500
MAC_Address x_5254_0015_ac8a
Physical_Address x_5254_0015_ac8a
IP_Address x_172_16_252_17_30
Delay x_10
Encapsulation arpa
Flow_Control_Receive False
Flow_Control_Send False


Port_Channel_Member False
}
GigabitEthernet6 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_MAC_Pause_Frames x_0
Input_Multicast x_0
Input_Octects x_123161
Input_Packets x_914
Output_Broadcast x_0
Output_Errors x_0
Output_MAC_Pause_Frames x_0
Output_Multicast x_0
Output_Packets x_932
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```
```mermaid
erDiagram
dist-rtr01 |o--|{ Loopback0 : to
Loopback0{
Enabled False
Operational_Status down
Switchport_Enable False
Type Loopback
Bandwidth x_8000000
MTU x_1514
Delay x_5000
Encapsulation loopback


Port_Channel_Member False
}
Loopback0 |o--|{ Counters : counters
Counters {
Input_Broadcast x_0
Input_CRC_Errors x_0
Input_Errors x_0
Input_Multicast x_0
Input_Octects x_0
Input_Packets x_0
Output_Broadcast x_0
Output_Errors x_0
Output_Multicast x_0
Output_Packets x_0
Last_Clear x_never
Input_Rate x_0
Load_Interval x_300
Output_Rate x_0
}
```