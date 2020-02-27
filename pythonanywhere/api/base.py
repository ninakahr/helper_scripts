import os

import requests

PYTHON_VERSIONS = {
    "2.7": "python27", "3.4": "python34", "3.5": "python35", "3.6": "python36", "3.7": "python37", "3.8": "python38",
}


class AuthenticationError(Exception):
    pass


class NoTokenError(Exception):
    pass


def get_api_endpoint():
    hostname = os.environ.get(
        "PYTHONANYWHERE_SITE",
        "www." + os.environ.get(
            "PYTHONANYWHERE_DOMAIN",
            "pythonanywhere.com"
        )
    )
    return "https://{hostname}/api/v0/user/{{username}}/{{flavor}}/".format(hostname=hostname)


def call_api(url, method, **kwargs):
    token = os.environ.get("API_TOKEN")
    if token is None:
        raise NoTokenError(
            "Oops, you don't seem to have an API token.  "
            "Please go to the 'Account' page on PythonAnywhere, then to the 'API Token' "
            "tab.  Click the 'Create a new API token' button to create the token, then "
            "start a new console and try running this script again."
        )
    insecure = os.environ.get("PYTHONANYWHERE_INSECURE_API") == "true"
    response = requests.request(
        method=method,
        url=url,
        headers={"Authorization": "Token {token}".format(token=token)},
        verify=not insecure,
        **kwargs
    )
    if response.status_code == 401:
        print(response, response.text)
        raise AuthenticationError(
            "Authentication error {status_code} calling API: {response_text}".format(
                status_code=response.status_code, response_text=response.text
            )
        )
    return response


