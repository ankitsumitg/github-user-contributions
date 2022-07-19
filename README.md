# [GitHub User Contributions 👨🏻‍💻 ](https://github.com/ankitsumitg/github-user-contributions)
<a href="https://github.com/ankitsumitg"><img src="https://img.shields.io/github/workflow/status/ankitsumitg/github-user-contributions/python_build?logo=github&style=for-the-badge" alt="GitHub Contrib"></a>

* Simple api to get GitHub `user contributions` ( No GitHub api key is needed ).
* Simply use the raw json once your username is updated. ( Typically within a minute or so )

## Usage
* Comment your username in the [discussion thread](https://github.com/ankitsumitg/github-user-contributions/discussions/1)
  * Format: `@username`
  * This is one time process only
* Wait for the `python_build` workflow to complete
  * Workflow will take about 1 minute to complete
  * Your contributions will be updated once workflow `completes`
* Check the `end-points` with your username mentioned below
* Since the response is in json, you can use it how-ever you like it!
* Also, your contributions will be `updated at 00:00 UTC every day` 😀


## Endpoints
* These are the endpoints that you can use with your username:
* Right now response has 
  * `username: str`
  * `fullname: str`
  * `contributions: int`

| No. | Endpoint                                                                                                       | Parameters                  | Description                         | Example                                                                                                    |
|-----|----------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| 1   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/YYYY/MM/DD ``` | `username` `YYYY` `MM` `DD` | Contribution for a particular Day   | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/2022/07/17 |
| 2   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/YYYY/MM ```    | `username` `YYYY` `MM`      | Contribution for a particular Month | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/2022/07    |
| 3   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/YYYY ```       | `username` `YYYY`           | Contribution for a particular Year  | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/2022       |
| 4   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/LASTYEAR ```   | `username`                  | Contribution since Last Year        | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/LASTYEAR   |
| 5   | ```https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/username/LIFETIME ```   | `username`                  | Contribution all Lifetime 😎        | https://raw.githubusercontent.com/ankitsumitg/github-user-contributions/main/api/v1/ankitsumitg/LIFETIME   |

## Sample response for 1st example endpoint
```json
{
  "username": "ankitsumitg", 
  "fullname": "Ankit Gupta", 
  "contribution": 9
}
```

## Internal Working
* Internally, the `github-user-contributions` is running a `python` script that crawls and scrapes the `skyline-contributions` from GitHub users page
* Everything is happening is asynchronously
* And `python_build` workflow runs the script and updates the `user contributions`

## License
![GitHub](https://img.shields.io/github/license/ankitsumitg/github-user-contributions?style=for-the-badge)

## Contributors
<a href="https://github.com/ankitsumitg/github-user-contributions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ankitsumitg/github-user-contributions" />
</a>