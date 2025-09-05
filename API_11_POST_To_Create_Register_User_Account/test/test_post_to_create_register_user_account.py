import requests


def test_post_to_create_register_user_account(api_base_url):
    url = f"{api_base_url}/createAccount"
    payload = {
        "name": "rahul",
        "email": "rahulshettyacademyAPI11@gmail.com",
        "password": "abc123",
        "title": "Mr.",
        "day": "15",
        "month": "July",
        "year": "1995",
        "firstname": "Tom",
        "lastname": "Smith",
        "company": "Microsoft",
        "address1": "Microsoft Headquarters, One Microsoft Way, Redmond, WA 98052 United States",
        "address2": "Building 92, Floor 3",
        "country": "Canada",
        "state": "Ontario",
        "city": "Toronto",
        "zipcode": "M4B1B3",
        "mobile_number": "1234567890"
    }
    # 不加 data=，有時Python 會把 payload 當成 json 或 params，導致後端接收不到正確的 form-data，所以回傳 400
    response = requests.post(url, data=payload)
    assert response.request.method == "POST", "Method is not POST"

    data = response.json()

    assert data["responseCode"] == 201, "Status code is not 201"
    assert data["message"] == "User created!", "Unexpected error message"
