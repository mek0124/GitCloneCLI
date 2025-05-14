# src/tests/test_test_command.py
from click.testing import CliRunner
from src.app.commands.test import test

def test_test_command_output():
    """Test the test command output."""
    runner = CliRunner()
    result = runner.invoke(test)
    assert result.exit_code == 0
    assert "Name: git-clone" in result.output
    assert "Version: 0.0.1" in result.output
    assert "Author: mek0124" in result.output
    assert "Repo: https://github.com/mek0124/GitClone" in result.output
    assert "License: MIT" in result.output
    assert "Description: A CLI tool for cloning multiple Git repositories at once" in result.output