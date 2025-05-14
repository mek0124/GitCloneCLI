"""Main CLI application module."""
import click
from app.commands.test import test
from app.commands.clone import clone

@click.group()
@click.version_option(package_name='git-clone')
def app():
    """GitClone - A CLI tool for managing multiple Git repositories.
    
    Provides commands for cloning repositories and viewing package information.
    """
    pass

# Register commands
app.add_command(test)
app.add_command(clone)

if __name__ == '__main__':
    app()
