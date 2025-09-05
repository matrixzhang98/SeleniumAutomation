import requests


def test_post_to_search_product_without_search_product_parameter(api_base_url):
    url = f"{api_base_url}/searchProduct"
    response = requests.post(url)

    data = response.json()

    assert data["responseCode"] == 400, "Status code is not 400"
    assert data["message"] == "Bad request, search_product parameter is missing in POST request.", "Unexpected error message"