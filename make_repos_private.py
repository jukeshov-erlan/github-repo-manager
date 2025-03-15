import os
from dotenv import load_dotenv
import requests

load_dotenv()

token = os.getenv('GITHUB_TOKEN')

if not token:
    print("Token not found!")
    exit(1)

headers = {'Authorization': f'token {token}'}

repos_url = 'https://api.github.com/user/repos'
response = requests.get(repos_url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    # Write here your github username
    your_username = 'your username'
    for repo in repos:
        repo_name = repo['name']
        if repo['private']:
            print(f'Repository {repo_name} is already private')
            continue

        change_url = f'https://api.github.com/repos/{your_username}/{repo_name}'
        payload = {'private': True}
        change_response = requests.patch(change_url, json=payload, headers=headers)

        if change_response.status_code == 200:
            print(f'Repository {repo_name} is now private')
        else:
            print(f'I can\'t change repository {repo_name}')
else:
    print('I can\'t get list of repositories')
