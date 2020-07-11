import click
import shaker

@click.command()
@click.option('--pump', multiple=True, type=click.Tuple([int, int]), help='<int> of the pump to activate during <int> seconds')
def get_the_order(pump):
    """Program that interact with the hardware peripheral of the Barbox project"""
    shaker.compute_orders(pump)

if __name__ == '__main__':
    get_the_order()