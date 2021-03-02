import click
from pj_1.client_my import current_start_client





# ==========click====client========
@click.command()
@click.argument('addr')
@click.argument('port')
def main(addr, port):
    current_start_client(addr, port)


if __name__ == '__main__':
    main()