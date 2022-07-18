import requests
import re

with open('last_comment.txt', 'r') as f:
    user_names_from_comments = set(re.findall(r'@(\w+)', f.read(), re.MULTILINE))

with open('contributors.md', 'r') as f:
    user_names_from_contributions = set(re.findall(r'@(\w+)', f.read(), re.MULTILINE))

# remove the usernames from comments that are already present in the contributions
user_names_from_comments = user_names_from_comments - user_names_from_contributions

if user_names_from_comments:
    is_updated = False
    for user_name in user_names_from_comments:
        print(f'Checking user: {user_name}')
        r = requests.get(f'https://api.github.com/users/{user_name}')
        if r.status_code == 200:
            print(f'User: {user_name} exists')
            with open('contributors.md', 'a') as f:
                f.write(f'- @{user_name}\n')
            is_updated = True
        else:
            print(f'User: {user_name} does not exist')
    if not is_updated:
        print('Users dosen\'t exist.')
        exit(1)
else:
    print('No users found or all users are already present in the contributions.md')
    exit(1)
