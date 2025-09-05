import requests


def test_put_to_all_brands_list(api_base_url):
    url = f"{api_base_url}/brandsList"
    response = requests.put(url)

    data = response.json()

    assert data["responseCode"] == 405, "Status code is not 405"

    assert data["message"] == "This request method is not supported.", "Unexpected error message"