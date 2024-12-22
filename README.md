# GitHub User Activity Viewer

A simple Python script to fetch and display recent activity of a GitHub user.

## Features

- Fetches recent public activities of a GitHub user using the GitHub API.
- Supports the following activity types:
  - **PushEvent**: Displays the number of commits pushed to a repository.
  - **CreateEvent**: Indicates when a new repository is created.
  - **WatchEvent**: Shows when a repository is starred.

## Requirements

- Python 3.x
- `requests` library (install with `pip install requests`)

## Usage

1. Clone the repository or save the script to your local machine.
2. Run the script using the command line.

### Command Syntax:

```bash
python <script_name>.py gh-user-activity <GitHub-username>
```
