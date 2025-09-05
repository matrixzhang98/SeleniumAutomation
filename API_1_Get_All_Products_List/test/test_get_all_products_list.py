import requests
import json


def test_get_all_products_list(api_base_url):
    url = f"{api_base_url}/productsList"
    response = requests.get(url)

    assert response.status_code == 200, "Status code is not 200"

    assert response.request.method == "GET", "Method is not GET"

    data = response.json()

    assert "products" in data, "'products' key not found in response"

    assert isinstance(data["products"], list), "'products' is not a list"

    assert len(data["products"]) > 0, "'products' list is empty"

    print("Response JSON:", json.dumps(data, indent=2))