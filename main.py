# vWe108CxftyKecJ5RNEy
# vWe108CxftyKecJ5RNEy

from ovs_vsctl import VSCtl
from ovs_vsctl import list_cmd_parser
from ovs_vsctl import line_parser

from bridge import Bridge
from port import Port
import json


def getPortList(vsctl, bridgeName, allInterfaceList):
    ports = []
    for port in vsctl.run('list-ports ' + bridgeName, parser=line_parser):
        for interface in allInterfaceList:
            if interface.name == port:
                print("####################")
                print(bridgeName)
                print(port)
                if "container_id" in interface.external_ids:
                    pass
                print(interface.external_ids)
                print("####################")
                ports.append(Port(port, "", interface.external_ids))
                break
    return ports




def getBridgeList(vsctl):
    bridges = []
    allInterfaceList = vsctl.run('--columns=name,external-ids list Interface', parser=list_cmd_parser)
    for br in vsctl.run('--columns=name list bridge', parser=list_cmd_parser):
        bridges.append(Bridge(br.name, getPortList(vsctl, br.name, allInterfaceList)))
    return bridges







if __name__ == '__main__':
    vsctl = VSCtl('tcp', '127.0.0.1', 6640)
    print(getBridgeList(vsctl))



# print(vsctl.run('list-ports br0', parser=line_parser))











#
# from ovs_vsctl import VSCtl
# from ovs_vsctl import list_cmd_parser
# from ovs_vsctl import line_parser
#
# vsctl = VSCtl('tcp', '127.0.0.1', 6640)
# # print(vsctl.run('--columns=name list bridge', parser=list_cmd_parser))
# test = vsctl.run('--columns=name list bridge', parser=list_cmd_parser)
# for i in test:
#     print(i.name
#
#           )
#
#
# print(vsctl.run('list-ports br0', parser=line_parser))
#
#
# # print(vsctl.run('--columns=name,external-ids list Interface', parser=list_cmd_parser))
#
# # vsctl.run(command='show')
# # popen = vsctl.run('show')
# # print(popen.stdout.read())