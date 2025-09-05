import requests


def test_post_to_verify_login_with_invalid_details(api_base_url):
    url = f"{api_base_url}/verifyLogin"
    payload = {"email": "rahulshettyacademyXXX@gmail.com", "password": "abc123"}
    response = requests.post(url, payload)

    assert response.request.method == "POST", "Request method is not POST"

    data = response.json()

    assert data["responseCode"] == 404, "Status code is not 404"
    assert data["message"] == "User not found!", "Unexpected error message"
