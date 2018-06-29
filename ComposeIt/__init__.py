import docker
from argparse import ArgumentParser


# noinspection PyBroadException,PyBroadException,PyBroadException
class ComposeIt(object):
    # noinspection PyBroadException
    def __init__(self, container_id, socket):
        from ComposeIt import Parser

        try:
            client = docker.APIClient(base_url=socket, timeout=10)
            inspect = client.inspect_container(container_id)
            self.parser = Parser.InspectParser(inspect)
            self.parser.perform_parse()
        except:
            print("Container not found")


def main():
    argparser = ArgumentParser(description='Compose-It')
    argparser.add_argument('-s', '--socket', action='store_true', help='Docker socket',
                           default='unix://var/run/docker.sock')
    argparser.add_argument('container_id', help="Existing container Id or Name to generate from")

    args = argparser.parse_args()

    ComposeIt(args.container_id, args.socket)


if __name__ == '__main__':
    main()
