import requests


def test_post_to_all_products_list(api_base_url):
    url = f"{api_base_url}/productsList"
    response = requests.post(url)

    data = response.json()

    assert data["responseCode"] == 405, "Status code is not 405"

    assert data["message"] == "This request method is not supported.", "Unexpected error message"