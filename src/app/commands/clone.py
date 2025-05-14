import subprocess
import click
import sys
import os


def clone_repos(target_dir: str, links: list) -> None:
    success = 0
    invalid_urls = []
    failed_clones = []

    original_directory = os.getcwd()

    try:
        os.chdir(target_dir)

        click.echo(f"Attempting To Clone {len(links)} {"repos" if len(links) > 1 else "repo"} to {target_dir}")

        for link in links:
            click.echo(f"\nAttempting To Clone: {link}")

            try:
                subprocess.call(["git", "clone", link])
                success += 1
            except Exception as e:
                click.echo(f"Failed To Clone: {link}", err=True)
                failed_clones.append(link)

    except Exception as e:
        click.echo(f"An Unexpected Error Occured: {str(e)}", err=True)

    finally:
        os.chdir(original_directory)


@click.command("clone")
@click.argument(
    "target_dir",
    type = click.Path(
        file_okay = False,
        writable = True
    ),
    required = True
)
@click.option(
    "--file_path",
    help = "Path to file containing GitHub URLs to clone",
    type = click.Path(
        exists = True,
        readable=True
    )
)
@click.option("--urls", help = "Comma-separated list of GitHub URLs to clone")
def clone(target_dir: str, file_path: str = None, urls: str = None):
    if not file_path and not urls:
        click.echo("Error: You must provide either a file path or a csv list of urls", err=True)
        click.echo("See usage with --help")
        sys.exit(1)  # Use sys.exit instead of exit

    if not os.path.exists(target_dir):
        click.echo(f"Error: Target Directory '{target_dir}' does not exist", err=True)
        sys.exit(1)

    if file_path and not os.path.exists(file_path):
        click.echo(f"Error: File Path '{file_path}' does not exist", err=True)
        sys.exit(1)

    if file_path:
        with open(file_path, 'r') as file:
            url_links = [url.strip() for url in file if url.strip()]
    else:
        url_links = [url.strip() for url in urls.split(',') if url.strip()]

    if not url_links:
        click.echo("Error: No valid URLs provided", err=True)
        sys.exit(1)

    clone_repos(target_dir, url_links)