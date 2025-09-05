import requests


def test_delete_method_to_delete_user_account(api_base_url):
    url = f"{api_base_url}/deleteAccount"
    payload = {"email": "rahulshettyacademyAPI11@gmail.com", "password": "abc123"}
    response = requests.delete(url, data=payload)

    assert response.request.method == "DELETE", "Method is not DELETE"
    data = response.json()

    assert data["responseCode"] == 200, "Status code is not 200"
    assert data["message"] == "Account deleted!", "Unexpected error message"
