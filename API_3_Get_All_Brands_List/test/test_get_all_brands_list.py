import requests


def test_get_all_brands_list(api_base_url):
    url = f"{api_base_url}/brandsList"
    response = requests.get(url)

    assert response.status_code == 200, "Status code is not 200"

    assert response.request.method == "GET", "Method is not GET"

    data = response.json()

    assert "brands" in data, "'brands' key not found in response"

    assert isinstance(data["brands"], list), "'brands' is not a list"

    assert len(data["brands"]) > 0, "'brands' list is empty"