import requests


def test_post_to_verify_login_with_valid_details(api_base_url):
    url = f"{api_base_url}/verifyLogin"
    payload = {"email": "rahulshettyacademyTestCase20@gmail.com", "password": "abc123"}
    response = requests.post(url, payload)

    assert response.status_code == 200, "Status code is not 200"
    assert response.request.method == "POST", "Request method is not POST"

    data = response.json()

    assert data["responseCode"] == 200, "Status code is not 200"
    assert data["message"] == "User exists!", "Unexpected error message"