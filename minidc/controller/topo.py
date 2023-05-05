#!/usr/bin/env python

class Host(object):
    def __init__(self, name, ip, eth, switch, vlans):
        self.name = name
        self.ip = ip
        self.eth = eth
        self.switch = switch
        self.vlans = vlans

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{0}: ({1}, {2}, {3}, {4})".format(self.name,
                                                  self.ip,
                                                  self.eth,
                                                  self.switch,
                                                  self.vlans)


class CoreSwitch(object):
    def __init__(self, name, dpid, vlans):
        self.name = name
        self.dpid = dpid
        self.vlans = vlans

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{0}: ({1}, {2})".format(self.name,
                                        self.dpid,
                                        self.vlans)


class EdgeSwitch(object):
    def __init__(self, name, dpid, neighbors):
        self.name = name
        self.dpid = dpid
        self.neighbors = neighbors

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{0}: ({1}, {2})".format(self.name,
                                        self.dpid,
                                        self.neighbors)


class Topology(object):
    def __init__(self, config):
        self.hosts = {
            'h3': Host('h3', '10.0.0.3', '4e:00:55:1c:ad:b2', 's101', [1]),
            'h6': Host('h6', '10.0.0.6', '8a:74:a0:1c:38:7e', 's101', [1]),
            'h1': Host('h1', '10.0.0.1', '2e:b4:75:8f:34:78', 's102', [0]),
            'h4': Host('h4', '10.0.0.4', '86:d2:65:55:90:8a', 's102', [1]),
            'h2': Host('h2', '10.0.0.2', '52:1b:41:bd:e1:4e', 's103', [0]),
            'h5': Host('h5', '10.0.0.5', 'fe:f4:f8:9e:cc:75', 's103', [1])
        }
        self.vlans = {1: ['h3', 'h6', 'h4', 'h5'], 0: ['h1', 'h2']}
        self.edgeSwitches = {
            's101': EdgeSwitch('s101', 101, ['h3', 'h6']),
            's102': EdgeSwitch('s102', 102, ['h1', 'h4']),
            's103': EdgeSwitch('s103', 103, ['h2', 'h5'])
        }
        self.coreSwitches = {
            's104': CoreSwitch('s104', 104, [0]),
            's105': CoreSwitch('s105', 105, [1])
        }
        self.ports = {
            's104': {1: 's101', 's101': 1, 2: 's102', 's102': 2, 3: 's103', 's103': 3},
            's105': {1: 's101', 's101': 1, 2: 's102', 's102': 2, 3: 's103', 's103': 3},
            's101': {1: 's104', 's104': 1, 2: 's105', 's105': 2, 3: 'h3', 'h3': 3, 4: 'h6', 'h6': 4},
            's102': {1: 's104', 's104': 1, 2: 's105', 's105': 2, 3: 'h1', 'h1': 3, 4: 'h4', 'h4': 4},
            's103': {1: 's104', 's104': 1, 2: 's105', 's105': 2, 3: 'h2', 'h2': 3, 4: 'h5', 'h5': 4}
        }
        self.switches = ['s101', 's102', 's103', 's104', 's105']

        print("controller topoooooo")

    def getVlanCore(self, vlan):
        for core in self.coreSwitches.values():
            if vlan in core.vlans:
                return core.name
        return None

    def dpidToName(self, dpid):
        for sw in self.edgeSwitches.values() + self.coreSwitches.values():
            if dpid == sw.dpid:
                return sw.name
        return None
