import asyncio
import json
import os
import platform

import aiohttp
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


async def get_commits_for_each_repo(username, repo_name, session):
    total_commits = 0
    print(f'Getting total commits for {repo_name}')
    commits_url = f'https://api.github.com/repos/{username}/{repo_name}/commits?per_page=100'
    # Fetch first page of commits
    commits_response = await session.get(commits_url, params=None)
    commits = await commits_response.json()
    # Count commits authored by the user per page
    user_commits = sum(1 for commit in commits if commit['author'] and commit['author']['login'] == username)
    total_commits += user_commits
    # Check if next page exist
    link = commits_response.headers.get('link', '').split(',')
    if link and link[0]:
        total_pages = int(link[-1].split(';')[0].split('page=')[-1][:-1])
        # Iterate through remaining pages
        all_commits_resp = await asyncio.gather(*[session.get(commits_url, params={'page': page})
                                                  for page in range(2, total_pages + 1)])
        all_commits_json = await asyncio.gather(*[commits_resp.json() for commits_resp in all_commits_resp])
        for commits in all_commits_json:
            # Count commits authored by the user per page
            user_commits = sum(
                1 for commit in commits if commit['author'] and commit['author']['login'] == username)
            total_commits += user_commits
    return total_commits


async def get_total_commits(username, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        # Fetch list of repositories
        repositories_url = f'https://api.github.com/search/repositories?q=user:{username}'
        repositories_response = await session.get(repositories_url, params=None)
        repositories_json = await repositories_response.json()
        repositories = repositories_json['items']
        all_commits_sum = sum(await asyncio.gather(*[get_commits_for_each_repo(username, repo['name'], session)
                                                     for repo in repositories]))

    return all_commits_sum


# Replace with your GitHub username and full name
user_name = 'ankitsumitg'
full_name = 'Ankit Gupta'

# Read token from environment variable
env_token = os.getenv('GH_TOKEN_CONTRIB_API')


def main():
    # Run the async function
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    total_commits = asyncio.run(get_total_commits(user_name, env_token))
    print(f"Total lifetime commits by {user_name}: {total_commits}")
    with open(f'./api/v1/{user_name}/LIFETIME.json', 'w') as f:
        f.write(json.dumps({'username': user_name, 'fullname': full_name, 'contribution': total_commits}))


if __name__ == '__main__':
    main()
