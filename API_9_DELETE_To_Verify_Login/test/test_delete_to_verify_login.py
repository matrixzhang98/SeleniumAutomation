import requests
import json


def test_delete_to_verify_login(api_base_url):
    url = f"{api_base_url}/verifyLogin"
    response = requests.delete(url)
    assert response.request.method == "DELETE", "Method is not DELETE"

    data = response.json()

    assert data["responseCode"] == 405, "Status code is not 405"
    assert data["message"] == "This request method is not supported.", "Unexpected error message"

    print("Response JSON:", json.dumps(data, indent=2))