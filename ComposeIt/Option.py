class Option(object):

    def __init__(self, option, otype):
        self.name = option
        self.type = otype

    @staticmethod
    def process_ports(data):
        ports = []
        if data:
            for key, value in data.items():
                port = key.split("/")
                port_str = ""
                if value[0]['HostIp'] != "":
                    port_str = value[0]['HostIp'] + ":"
                port_str = port_str + value[0]['HostPort'] + ":" + str(port[0])
                if len(port) == 2:
                    port_str = port_str + "/" + port[1]
                ports.append(port_str)
        return ports

    @staticmethod
    def process_exposed(data):
        exposed = []
        for key, value in data.items():
            port = key.split("/")
            exposed.append(str(port[0]))
        return exposed

    def process_generic(self, yml, option):
        if option:
            yml[self.name] = option

    def process_option(self, value, yml):
        try:
            if self.type == 'generic':
                self.process_generic(yml=yml, option=value)
            elif self.type == 'ports':
                self.process_generic(yml=yml, option=self.process_ports(data=value))
            elif self.type == 'expose':
                self.process_generic(yml=yml, option=self.process_exposed(data=value))
            elif self.type == 'command':
                self.process_generic(yml=yml, option=' '.join(value))
            elif self.type == 'restart':
                self.process_generic(yml=yml, option=value['Name'])
        except TypeError:
            pass


options = {
    'Config.Env': Option('environment', 'generic'),
    'Config.ExposedPorts': Option('expose', 'expose'),
    'Config.Labels': Option('labels', 'generic'),
    'Config.Cmd': Option('command', 'command'),
    'Config.Image': Option('image', 'generic'),
    'HostConfig.Binds': Option('volumes', 'generic'),
    'HostConfig.PortBindings': Option('ports', 'ports'),
    'HostConfig.CapAdd': Option('cap_add', 'generic'),
    'HostConfig.CapDrop': Option('cap_drop', 'generic'),
    'HostConfig.Dns': Option('dns', 'generic'),
    'HostConfig.DnsSearch': Option('dns_search', 'generic'),
    'HostConfig.Links': Option('links', 'generic'),
    'HostConfig.NetworkMode': Option('network_mode', 'generic'),
    'HostConfig.RestartPolicy': Option('restart', 'restart'),
    'HostConfig.PidMode': Option('pid', 'generic'),
    'HostConfig.Privileged': Option('privileged', 'generic'),
}
