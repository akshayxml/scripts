# Get number of bytes of code written in each language of all your github repos

# Add PAT here
token = "access_token"

import requests

def get_user_repos(token):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "type": "all",  # This includes public, private, and member repos
        "per_page": 100  # Maximum allowed per page
    }

    all_repos = []

    while url:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            repos = response.json()
            all_repos.extend(repos)

            url = response.links.get('next', {}).get('url')
            params = {}  
        else:
            print(f"Error: {response.status_code}")
            return None
        
    user_repos = [repo for repo in all_repos if repo['owner']['login'] == 'akshayxml']

    return user_repos

repos = get_user_repos(token)
if repos:
    for repo in repos:
        print(f"REPO = {repo['name']}")
        url = f"https://api.github.com/repos/akshayxml/{repo['name']}/languages"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            repos = response.json()
            print(repos)
        else:
            print(f"Error: {response.status_code}")
    print(f"\nTotal personal repositories: {len(repos)}")
