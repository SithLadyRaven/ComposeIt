import docker
from argparse import ArgumentParser

class ComposeIt(object):
    def __init__(self, container_id, socket):
        from ComposeIt import Parser
        
        try:
            client = docker.APIClient(base_url=socket,timeout=10)
            inspect = client.inspect_container(container_id)
            self.parser = Parser.InspectParser(inspect)
            self.parser.performParse()
        except:
            print ("Container not found")
        
def main():
    argParser = ArgumentParser(description='Compose-It')
    argParser.add_argument('-s', '--socket', action='store_true', help='Docker socket', default='unix://var/run/docker.sock')
    argParser.add_argument('container_id', help="Existing container Id or Name to generate from")
    
    args = argParser.parse_args()
    
    ComposeIt(args.container_id, args.socket)
