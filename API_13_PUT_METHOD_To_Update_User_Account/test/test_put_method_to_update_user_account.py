import requests
import json


def test_put_method_to_update_user_account(api_base_url):
    url = f"{api_base_url}/updateAccount"
    payload = {
        "name": "rahul",
        "email": "rahulshettyacademyAPI11@gmail.com",
        "password": "abc123",
        "title": "Mrs.",
        "day": "15",
        "month": "July",
        "year": "1995",
        "firstname": "TomAPI13",
        "lastname": "SmithAPI13",
        "company": "MicrosoftAPI13",
        "address1": "MicrosoftAPI13 Headquarters, One Microsoft Way, Redmond, WA 98052 United States",
        "address2": "BuildingAPI13 92, Floor 3",
        "country": "Canada",
        "state": "OntarioAPI13",
        "city": "TorontoAPI13",
        "zipcode": "M4B1B3API13",
        "mobile_number": "1234567890"
    }
    response = requests.put(url, data=payload)
    assert response.request.method == "PUT", "Method is not PUT"

    data = response.json()
    assert data["responseCode"] == 200, "Status code is not 200"
    assert data["message"] == "User updated!", "Unexpected error message"

    print("Response JSON:", json.dumps(data, indent=2))