# [GitHub User Contributions 👨🏻‍💻](https://github.com/ankitsumitg/github-user-contributions)
<a href="https://github.com/ankitsumitg"><img src="https://img.shields.io/github/actions/workflow/status/ankitsumitg/github-user-contributions/python_build.yml?logo=github&style=for-the-badge" alt="GitHub Contrib"></a>

* Simple api to get GitHub `user contributions` ( No GitHub api key is needed ).
* Simply use the raw Json once your username is updated. ( Typically, within a minute or so )
* Any help/suggestions are welcome ⚡ 👍🏻
## Usage
* Comment your username in the [discussion thread](https://github.com/ankitsumitg/github-user-contributions/discussions/1)
  * Format: `@username`
  * This is a one time process only
* Wait for the `python_build` workflow to complete
  * Workflow will take about 1 minute to complete
  * Your contributions will be updated once workflow `completes`
* Check the `end-points` with your username mentioned below
* Since the response is in json, you can use it however you like it!
* Also, your contributions will be `updated every day at 00:00 UTC` 😀


## Endpoints
* These are the endpoints that you can use with your username:
* Right now the response has 
  * `username: str`
  * `fullname: str`
  * `contributions: int`

| No. | Endpoint                                                                                                            | Parameters                  | Description                         | Example                                                                                                         |
|-----|---------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| 1   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/YYYY/MM/DD.json ``` | `username` `YYYY` `MM` `DD` | Contribution for a particular Day   | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/2022/07/17.json |
| 2   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/YYYY/MM.json ```    | `username` `YYYY` `MM`      | Contribution for a particular Month | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/2022/07.json    |
| 3   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/YYYY.json ```       | `username` `YYYY`           | Contribution for a particular Year  | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/2022.json       |
| 4   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/LASTYEAR.json ```   | `username`                  | Contribution since Last Year        | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/LASTYEAR.json   |
| 5   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/LIFETIME.json ```   | `username`                  | Contribution all Lifetime 😎        | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/LIFETIME.json   |

## Sample response for 1st example endpoint
```json
  {
    "username": "ankitsumitg", 
    "fullname": "Ankit Gupta", 
    "contribution": 9
  }
```
## Support for [shields.io](https://shields.io) badge
<img
    src="https://img.shields.io/badge/dynamic/json?color=green&label=contribution&style=for-the-badge&logo=github&query=contribution&url=https%3A%2F%2Fraw.githubusercontent.com%2Fankitsumitg%2Fgithub-user-contributions%2Fmain%2Fapi%2Fv1%2Fankitsumitg%2FLIFETIME.json"
    alt="Contribution Badge">
```html
<img src="https://img.shields.io/badge/dynamic/json?color=green&label=contribution&style=for-the-badge&logo=github&query=contribution&url=https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/LIFETIME.json" alt="Contribution Badge">
```
* Change the url parameter accordingly
* Refer [shields.io](https://shields.io) Dynamic badge documentation to make the badge to your liking 😍


## Internal Working
* Internally, the `github-user-contributions` runs a `python` script that crawls and scrapes the `skyline-contributions` from GitHub users page
* Everything happens asynchronously
* `python_build` workflow runs the script and updates the `user contributions`

## Notes
* If a user did not make private contributions visible on GitHub profile, then only `public contributions` will be counted

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## Contributors
<a href="https://github.com/ankitsumitg/github-user-contributions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ankitsumitg/github-user-contributions" />
</a>

# [GitHub User Contributions 👨🏻‍💻](https://github.com/ankitsumitg/github-user-contributions)

* [GitHub Link](https://github.com/ankitsumitg/github-user-contributions)
* Simply use the raw Json once your username is updated. (Typically, within a minute or so. See: [Usage](https://github.com/ankitsumitg/github-user-contributions#usage))
* Any help/suggestions are welcome ⚡ 👍🏻
* Would really appreciate any improvements/contributions 😊
* Types
   * Day Wise
   * Month Wise
   * Year Wise
   * Since Last Year
   * Lifetime
* Do checkout 😊👍🏻
