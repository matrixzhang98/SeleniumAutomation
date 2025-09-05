import requests
import json


def test_post_to_search_product(api_base_url):
    url = f"{api_base_url}/searchProduct"
    payload = {"search_product": "top"}
    response = requests.post(url, payload)

    assert response.status_code == 200, "Status code is not 200"
    assert response.request.method == "POST", "Request method is not POST"

    data = response.json()

    assert "products" in data, "'product' key not found in response"
    assert isinstance(data["products"], list), "'product' is not a list"
    assert len(data["products"]) > 0, "'product' list is empty"

    has_keywords = any(
        "top" in product["name"].lower() or
        "top" in product["category"].lower()
        for product in data["products"]
    )

    assert has_keywords, "keywords are not found in product name or category"

    print("Response JSON:", json.dumps(data, indent=2))