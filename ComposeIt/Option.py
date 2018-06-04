class Option(object):
  
    def __init__ (self, option, type):
        self.name = option
        self.type = type
        
    def process_ports(self, data):
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

    def process_exposed(self, data):
        l = []
        for key,value in data.items():
            port = key.split("/")
            l.append(str(port[0]))
        return l
      
    def process_generic(self, yml, option):
        if option:
            yml[self.name] = option
          
    def process_option(self, value, yml):
        try:
            if self.type == 'generic':
                self.process_generic(yml = yml, option = value)
            elif self.type == 'ports':
                self.process_generic(yml = yml, option = self.process_ports(data = value))
            elif self.type == 'expose':
                self.process_generic(yml = yml, option = self.parse_exposed(data = value))
            elif self.type == 'command':
                self.process_generic(yml=yml, option = ' '.join(value))
            elif self.type =='restart':
                self.process_generic(yml=yml, option = value['Name'])
        except:
            pass

options = {
    'Config.Env' : Option('environment', 'generic'),
    'Config.ExposedPorts' : Option('expose', 'expose'),
    'Config.Labels' : Option('labels', 'generic'),
    'Config.Cmd' : Option('command', 'command'),
    'Config.Image' : Option('image', 'generic'),
    'HostConfig.Binds' : Option('volumes', 'generic'),
    'HostConfig.PortBindings' : Option('ports', 'ports'),
    'HostConfig.CapAdd' : Option('cap_add', 'generic'),
    'HostConfig.CapDrop' : Option('cap_drop', 'generic'),
    'HostConfig.Dns' : Option('dns', 'generic'),
    'HostConfig.DnsSearch' : Option('dns_search', 'generic'),
    'HostConfig.Links' : Option('links', 'generic'),
    'HostConfig.NetworkMode' : Option('network_mode', 'generic'),
    'HostConfig.RestartPolicy' : Option('restart', 'restart'),
    'HostConfig.PidMode' : Option('pid', 'generic'),
    'HostConfig.Privileged' : Option('privileged', 'generic'),
}