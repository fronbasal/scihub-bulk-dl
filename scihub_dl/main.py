from pathlib import Path
from typing import List

import click

from scihub_dl.crawler import SciHub


@click.command()
@click.argument('doi', type=str, required=True, nargs=-1)
@click.option('--output', '-o', type=click.Path(exists=False, file_okay=False, dir_okay=True, ), help='Output directory', required=True)
@click.option('--url', '-u', default='https://sci-hub.se/', help='Sci-Hub URL')
@click.option('--timeout', '-t', default=60, help='Request timeout')
def store(doi: str, output: str, url: List[str], timeout: int):
    output = Path(output)
    for d in doi:
        SciHub(d, output, url, timeout).fetch()


if __name__ == '__main__':
    store()
