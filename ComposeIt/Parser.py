import sys
import yaml
from collections import OrderedDict
from ComposeIt.Option import options

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
    
    def performParse(self):
        config = self.inspect['Config']
        hostconfig = self.inspect['HostConfig']
        
        yml = OrderedDict()
        service = OrderedDict()
        serviceName = OrderedDict()
        
        for key, value in config.items():
            current_option = 'Config' + '.' + key
            if current_option in options:
                options[current_option].process_option(value = value, yml = service)
                
        for key, value in hostconfig.items():
            current_option = 'HostConfig' + '.' + key
            if current_option in options:
                options[current_option].process_option(value = value, yml = service)
        
        yml['version'] = composeVersion
        serviceName[self.inspect['Name'][1:]] = service
        yml['services'] = serviceName
        
        print (yaml.dump(yml, default_flow_style=False))
