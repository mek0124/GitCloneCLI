import click

@click.command("test")
def test():
    version = '0.0.1'
    name = 'git-clone'
    author = 'mek0124'
    repo = 'https://github.com/mek0124/GitClone'
    licens = 'MIT'
    description = 'A CLI tool for cloning multiple Git repositories at once'

    click.echo(f"Name: {name}")
    click.echo(f"Version: {version}")
    click.echo(f"Author: {author}")
    click.echo(f"Repo: {repo}")
    click.echo(f"License: {licens}")
    click.echo(f"Description: {description}")