<label id="top"></label>

## GitClone - CLI App (located in /cli)

Table of Contents

- [Introduction](#introduction)
- [How To Use](#how-to-use---cli-app-️)
- [Issues](#issues)

### How To Use - CLI App [⬆️](#top)

> Note: This is the CLI portion of GitClone, located in the `/cli` directory of the main project.

> Note: You will need Python 3.7+ installed. Bash is not required for the CLI version.

- Clone the main repo `git clone https://github.com/mek0124/GitClone.git`
- Navigate to the CLI directory:
  - `cd GitClone/cli`
- Install the CLI application:
  - `pip install -e .`
- Run the app:
  - Basic usage: `git-clone clone ~/path/to/target/output --urls "url1, url2, url3, ..."`
  - Or from file: `git-clone clone ~/path/to/target/output --file_path urls.txt`

Example Usage:

- Using the URLs flag
  - `git-clone clone ./repos --urls "https://github.com/user/repo1.git,https://github.com/user/repo2.git"`

- Using the file_path flag
  - `git-clone clone ./repos --file_path src/data/urls.txt`
