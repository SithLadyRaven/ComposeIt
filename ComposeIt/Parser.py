import sys
import yaml
from collections import OrderedDict

composeVersion = '3'
    
class InspectParser(object):
    
    def __init__(self, inspect):
        self.inspect = inspect
        
        yaml.add_representer(OrderedDict, self.represent_ordereddict)
    
    def represent_ordereddict(self, dumper, data):
        value = []
    
        for item_key, item_value in data.items():
            node_key = dumper.represent_data(item_key)
            node_value = dumper.represent_data(item_value)
    
            value.append((node_key, node_value))
    
        return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)

    def parsePorts(self, data):
        l = []
        if data:
            for key,value in data.items():
                port = key.split("/")
                portStr = ""
                if value[0]['HostIp'] != "":
                    portStr = value[0]['HostIp'] + ":"
                portStr = portStr + value[0]['HostPort'] + ":" + str(port[0])
                if len(port) == 2:
                   portStr = portStr + "/" + port[1]
                l.append(portStr)
        return l

    def parseExposed(self, data):
        l = []
        for key,value in data.items():
            port = key.split("/")
            l.append(str(port[0]))
        return l
    
    def addOption(self, name, baseDict, option):
        if option:
            baseDict[name] = option
            
    def performParse(self):

        config = self.inspect['Config']
        hostconfig = self.inspect ['HostConfig']
        
        yml = OrderedDict()
        service = OrderedDict()
        serviceName = OrderedDict()
        
        self.addOption(name="environment", baseDict = service, option = config['Env'])
        self.addOption(name="volumes", baseDict = service, option = hostconfig['Binds'])
        self.addOption(name='ports', baseDict = service, option = self.parsePorts(hostconfig['PortBindings']))
        self.addOption(name='expose', baseDict = service, option = self.parseExposed(config['ExposedPorts']))
        self.addOption(name='labels', baseDict = service, option = config['Labels'])
        try:
           self.addOption(name='command', baseDict = service, option = " ".join(config['Cmd']))
        except:
           pass
        self.addOption(name='cap_add', baseDict = service, option = hostconfig['CapAdd'])
        self.addOption(name='cap_drop', baseDict = service, option = hostconfig['CapDrop'])
        self.addOption(name='cgroup_parent', baseDict = service, option = hostconfig['CgroupParent'])
        self.addOption(name='dns', baseDict = service, option = hostconfig['Dns'])
        self.addOption(name='dns_search', baseDict = service, option = hostconfig['DnsSearch'])
        self.addOption(name='links', baseDict = service, option = hostconfig['Links'])
        self.addOption(name='network_mode', baseDict = service, option = hostconfig['NetworkMode'])
        self.addOption(name='restart', baseDict = service, option = hostconfig['RestartPolicy']['Name'])
        self.addOption(name='pid', baseDict = service, option = hostconfig['PidMode'])
        self.addOption(name='privileged', baseDict = service, option = hostconfig['Privileged'])
        self.addOption(name='image', baseDict = service, option = config['Image'])
        self.addOption(name='version', baseDict = yml, option = composeVersion)
        self.addOption(name=self.inspect['Name'][1:], baseDict = serviceName, option = service)
        self.addOption(name='services', baseDict = yml, option = serviceName)
        
        print (yaml.dump(yml, default_flow_style=False))
