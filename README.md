TheCableGuy
===========

The CableGuy tool can be used to check the network topology - any missing 'cable-connections'. 
This application does the following: 
(a) takes the expected topology in the .DOT file format as input. 
(2) Obtains the topology information from the ODL using the rest-APIs 
(c) Compares the two topologies and displays and missing/lost ‘cable-connectivity’. 

Currently the application is customized for ODL-controller, and only for physical-network topology. 

In future, we plan to enhance it to cover multiple-controllers, and also the virtual-network topologies.

The REST requests used in this application to obtain information from the ODL can be enlisted as below:
1.	Topology Request: "http://"+odl_ip+":"+odl_port_num+"/controller/nb/v2/topology/default"
2.	Switches connected to ODL:  "http://"+odl_ip+":"+odl_port_num+"/controller/nb/v2/switchmanager/default/nodes"
3.	List of ports: "http://"+odl_ip+":"+odl_port_num+"/controller/nb/v2/switchmanager/default/node/OF/"

