import docker
from argparse import ArgumentParser


class ComposeIt(object):
    def __init__(self, container_list, socket):
        from ComposeIt import Parser

        try:
            client = docker.APIClient(base_url=socket, timeout=10)
            inspect_results = []
            for container in container_list:
                inspect = client.inspect_container(container)
                inspect_results.append(inspect)
            self.parser = Parser.InspectParser(inspect_results)
            self.parser.perform_parse()
        except docker.errors.NotFound:
            print("Container not found")


def main():
    argparser = ArgumentParser(description='Compose-It')
    argparser.add_argument('-s', '--socket', action='store_true', help='Docker socket',
                           default='unix://var/run/docker.sock')
    argparser.add_argument('container_list', nargs='+', help="Existing container Id or Name to generate from")

    args = argparser.parse_args()

    ComposeIt(args.container_list, args.socket)


if __name__ == '__main__':
    main()
