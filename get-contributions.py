import sys

import requests
from bs4 import BeautifulSoup

GITHUB_URL = 'https://github.com/'


def main():
    # Get user_name from command line argument
    user_name = sys.argv[1]
    # Get user's GitHub raw page
    user_page = requests.get(GITHUB_URL + user_name)
    # Parse the html
    soup = BeautifulSoup(user_page.text, 'html.parser')
    # Get the user's all years of contributions
    years = soup.find('ul', {'class': 'filter-list small'}).findAll('li')
    # Add the years into a list
    years_lst = [year.text.strip() for year in years]
    # Get the user's all contributions for each year
    for year in years_lst:
        total = 0
        new_url = GITHUB_URL + user_name + '?tab=overview&from=' + year + '-12-01&to=' + year + '-12-31'
        user_page = requests.get(new_url)
        soup = BeautifulSoup(user_page.text, 'html.parser')
        contribs = soup.findAll('rect', {'class': 'ContributionCalendar-day'})
        for contrib in contribs:
            if len(contrib.attrs) == 10:
                total += int(contrib.attrs['data-count'])
                # print(contrib.attrs['data-date'], contrib.attrs['data-count'], flush=True)
        print(f'{year} : {total}', flush=True)


if __name__ == '__main__':
    main()
