GitHub Repository Manager

A Python script to automate the process of making public GitHub repositories private using the GitHub API.

Features
- Automatically checks all repositories of a user on GitHub.
- Makes public repositories private.
- Works with GitHub's REST API and requires a GitHub Personal Access Token (PAT).

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine.
- The requests library installed. If you don't have it, you can install it using:
  ```bash
  pip install requests

A GitHub Personal Access Token (PAT) with repo scope. You can generate a token from GitHub's token generation page. => https://github.com/settings/tokens

1) Installation
Clone this repository:
git clone https://github.com/jukeshov-erlan/github-repo-manager.git

2) Navigate into the project directory:
cd github-repo-manager

3) Install the required dependencies:
pip install -r requirements.txt

4) Create a .env file in the project root directory and add your GitHub token:
GITHUB_TOKEN=your_personal_access_token

5) Usage
Run the script to make public repositories private:
python make_repos_private.py

The script will check all of your repositories and automatically make the public ones private.
Example output:
Repository my-repository is now private
Repository another-repository is already private

6) Contact
For any questions or issues, feel free to open an issue on GitHub or reach out to me directly at 
jukeshov-erlan@gmail.com





