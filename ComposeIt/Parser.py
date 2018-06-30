import sys
import yaml
from collections import OrderedDict
from ComposeIt.Option import options

COMPOSE_VERSION = '3'


class InspectParser(object):

    def __init__(self, inspect_results):
        self.inspect_results = inspect_results

        yaml.add_representer(OrderedDict, self.represent_ordereddict)

    @staticmethod
    def represent_ordereddict(dumper, data):
        value = []

        for item_key, item_value in data.items():
            node_key = dumper.represent_data(item_key)
            node_value = dumper.represent_data(item_value)

            value.append((node_key, node_value))

        return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)

    def perform_parse(self):

        service_name = OrderedDict()
        yml = OrderedDict()

        for container in self.inspect_results:
            config = container['Config']
            host_config = container['HostConfig']

            service = OrderedDict()

            for key, value in config.items():
                current_option = 'Config' + '.' + key
                if current_option in options:
                    options[current_option].process_option(value=value, yml=service)

            for key, value in host_config.items():
                current_option = 'HostConfig' + '.' + key
                if current_option in options:
                    options[current_option].process_option(value=value, yml=service)

            service_name[container['Name'][1:]] = service

        yml['version'] = COMPOSE_VERSION
        yml['services'] = service_name

        yaml.dump(yml, sys.stdout, default_flow_style=False)
