import os
import pytest
from unittest import mock
from click.testing import CliRunner
from src.app.commands.clone import clone, clone_repos

@pytest.fixture
def dummy_urls():
    return ["https://github.com/user/repo1.git", "https://github.com/user/repo2.git"]

def test_clone_repos_success(monkeypatch, dummy_urls):
    monkeypatch.setattr("subprocess.call", lambda cmd: 0)  # Mock subprocess.call as success
    monkeypatch.setattr("os.getcwd", lambda: "/mock/original")
    monkeypatch.setattr("os.chdir", lambda path: None)

    clone_repos("/mock/target", dummy_urls)
    # Since there's no return or log capturing, just ensuring no exceptions raised

def test_clone_repos_failure(monkeypatch):
    urls = ["https://github.com/fail/repo.git"]

    def fake_call(cmd):
        raise Exception("Git clone failed")

    monkeypatch.setattr("subprocess.call", fake_call)
    monkeypatch.setattr("os.getcwd", lambda: "/mock/original")
    monkeypatch.setattr("os.chdir", lambda path: None)

    # Should not raise error even if clone fails
    clone_repos("/mock/target", urls)

def test_clone_cli_no_args(tmp_path):
    runner = CliRunner()
    result = runner.invoke(clone, [str(tmp_path)])
    assert result.exit_code == 1
    assert "must provide either a file path or a csv list" in result.output


def test_clone_cli_invalid_target(tmp_path):
    runner = CliRunner()
    # Not creating target_dir to simulate "does not exist"
    result = runner.invoke(clone, [str(tmp_path / "invalid"), "--urls", "https://github.com/user/repo.git"])
    assert result.exit_code == 1
    assert "does not exist" in result.output

def test_clone_cli_urls(monkeypatch, tmp_path, dummy_urls):
    monkeypatch.setattr("subprocess.call", lambda cmd: 0)
    monkeypatch.setattr("os.getcwd", lambda: "/mock/original")
    monkeypatch.setattr("os.chdir", lambda path: None)

    runner = CliRunner()
    result = runner.invoke(clone, [str(tmp_path), "--urls", ",".join(dummy_urls)])
    assert result.exit_code == 0
    assert "Attempting To Clone" in result.output

def test_clone_cli_from_file(monkeypatch, tmp_path, dummy_urls):
    monkeypatch.setattr("subprocess.call", lambda cmd: 0)
    monkeypatch.setattr("os.getcwd", lambda: "/mock/original")
    monkeypatch.setattr("os.chdir", lambda path: None)

    # Create a temporary file with URLs
    file_path = tmp_path / "repos.txt"
    file_path.write_text("\n".join(dummy_urls))

    runner = CliRunner()
    result = runner.invoke(clone, [str(tmp_path), "--file_path", str(file_path)])
    assert result.exit_code == 0
    assert "Attempting To Clone" in result.output
