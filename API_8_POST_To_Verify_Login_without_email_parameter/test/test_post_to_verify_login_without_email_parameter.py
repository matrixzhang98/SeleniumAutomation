import requests


def test_post_to_verify_login_without_email_parameter(api_base_url):
    url = f"{api_base_url}/verifyLogin"
    payload = {"password": "abc1234"}
    response = requests.post(url, payload)

    data = response.json()

    assert data["responseCode"] == 400, "Status code is not 400"
    assert data["message"] == "Bad request, email or password parameter is missing in POST request.", "Unexpected error message"