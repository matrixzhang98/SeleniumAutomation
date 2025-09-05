import requests

def test_get_user_account_detail_by_email(api_base_url):
    url = f"{api_base_url}/getUserDetailByEmail"
    payload = {"email": "rahulshettyacademyAPI11@gmail.com"}
    response = requests.get(url, params=payload)
    assert response.request.method == "GET", "Method is not GET"

    data = response.json()
    assert data["responseCode"] == 200, "Status code is not 200"
    assert data["user"]["email"] == "rahulshettyacademyAPI11@gmail.com", \
        "Email does not match"
