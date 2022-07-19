import asyncio
import json
import os
import platform
import re
from collections import defaultdict

import aiofiles
import aiohttp
from bs4 import BeautifulSoup

GITHUB_URL = 'https://github.com/'


async def api_v1_dump(file_path, data):
    async with aiofiles.open(file_path, 'w') as f:
        await f.write(json.dumps(data))


async def api_v1_write(user_details, result):
    tasks = list()
    user_name = user_details['username']
    for key, val in result.items():
        if key == 'LIFETIME' or key == 'LASTYEAR' or len(key) == 4:
            tasks.append(api_v1_dump(f'./api/v1/{user_name}/{key}', {**user_details, **{'contribution': val}}))
        elif len(key) == 6:
            tasks.append(api_v1_dump(f'./api/v1/{user_name}/{key[:4]}/{key[4:]}',
                                     {**user_details, **{'contribution': val}}))
        else:
            tasks.append(api_v1_dump(f'./api/v1/{user_name}/{key[:4]}/{key[4:6]}/{key[6:]}',
                                     {**user_details, **{'contribution': val}}))
        if len(tasks) == 50:
            await asyncio.gather(*tasks)
            tasks.clear()
    await asyncio.gather(*tasks)


async def api_v1_update(year, url, session):
    return_dict = defaultdict(int)
    async with session.get(url) as resp:
        if resp.status == 200:
            user_page = await resp.text()
            soup = BeautifulSoup(user_page, 'html.parser')
            contributions = soup.findAll('rect', {'class': 'ContributionCalendar-day'})
            for contrib in contributions:
                if len(contrib.attrs) == 10:
                    return_dict[year] += int(contrib.attrs['data-count'])
                    if year != 'LASTYEAR':
                        date = contrib.attrs['data-date'].replace('-', '')
                        return_dict[date[:6]] += int(contrib.attrs['data-count'])
                        return_dict[date] = int(contrib.attrs['data-count'])
                    # print(contrib.attrs['data-date'], contrib.attrs['data-count'], flush=True)
            # print(f'{year} : {total}', flush=True)
    return return_dict, return_dict[year] if year != 'LASTYEAR' else 0


async def api_v1(user_name, session):
    # Get user's GitHub raw page
    async with session.get(GITHUB_URL + user_name) as resp:
        if resp.status == 200:
            user_page = await resp.text()
            # Parse the html
            soup = BeautifulSoup(user_page, 'html.parser')
            # Get the user's all years of api
            years = soup.find('ul', {'class': 'filter-list small'}).findAll('li')
            # Full username
            full_name = soup.find('span', {'class': 'p-name vcard-fullname d-block overflow-hidden'}).text.strip()
            if not full_name:
                full_name = user_name
            # Add the years into a list
            years_lst = [year.text.strip() for year in years]
            # Form urls for each year including in the last year
            urls = [(year, GITHUB_URL + user_name + '?tab=overview&from=' + year + '-12-01&to=' + year + '-12-31')
                    for year in years_lst]
            urls.append(('LASTYEAR', GITHUB_URL + user_name))
            # Get the user's all contribution for each year
            results = await asyncio.gather(*[asyncio.ensure_future(api_v1_update(year, url, session))
                                             for year, url in urls])
            results.append(({'LIFETIME': sum([result[1] for result in results])}, 0))
            # Dump json inside api/v1 directory
            user_details = {'username': user_name, 'fullname': full_name}
            # Create a directory for the user
            for year in years_lst:
                for month in range(1, 13):
                    os.makedirs(f'./api/v1/{user_name}/{year}/{month:02}', exist_ok=True)
            os.makedirs(f'./api/v1/{user_name}', exist_ok=True)
            await asyncio.gather(*[api_v1_write(user_details, result[0]) for result in results])
            # print(f'{full_name} : {results}', flush=True)
        else:
            print(f'Some Issue occurred', flush=True)


async def main():
    with open('contributors.md', 'r') as f:
        users = re.findall(r'@(\w+)', f.read(), re.MULTILINE)
        if users:
            print(f'Updating api for {len(users)} users', flush=True)
            async with aiohttp.ClientSession() as session:
                await asyncio.gather(*[api_v1(user, session) for user in users])
    print('Completed updating', flush=True)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
