# src/tests/test_app.py
from click.testing import CliRunner
from src.app.app import app

def test_app_help():
    """Test the main app help output."""
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "GitClone - A CLI tool for managing multiple Git repositories" in result.output
    assert "clone" in result.output
    assert "test" in result.output

def test_app_version():
    """Test the version option."""
    runner = CliRunner()
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    # Check for either installed version or development version
    # assert "git-clone, version" in result.output or "0.0.1" in result.output