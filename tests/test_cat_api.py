import os
import requests
import pytest

# base URL for The Cat API
BASE_URL = "https://api.thecatapi.com/v1"

# load API key from environment variable or config.json
API_KEY = os.getenv("CAT_API_KEY")

if not API_KEY:
    import json

    with open("config.json") as f:
        API_KEY = json.load(f).get("api_key")


# helper function to get headers
def get_headers():
    return {"x-api-key": API_KEY}


# test scenarios
@pytest.mark.parametrize("limit", [1, 5, 10])
def test_get_cat_images(limit):
    """Test retrieving a list of cat images."""
    response = requests.get(f"{BASE_URL}/images/search", headers=get_headers(), params={"limit": limit})
    assert response.status_code == 200, "Expected status code 200"
    assert isinstance(response.json(), list), "Response should be a list"
    assert len(response.json()) == limit, f"Expected {limit} images"


@pytest.mark.parametrize("breed_id, expected_breed", [
    ("beng", "Bengal"),
    ("siam", "Siamese"),
    ("abys", "Abyssinian")
])
def test_get_images_by_breed(breed_id, expected_breed):
    """Test retrieving cat images filtered by breed."""
    response = requests.get(
        f"{BASE_URL}/images/search",
        headers=get_headers(),
        params={"breed_ids": breed_id, "limit": 1}
    )
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert isinstance(data, list) and len(data) == 1, "Expected a list with one item"
    # Validate breed in response
    image = data[0]
    assert "breeds" in image, "Each image should contain breed information"
    assert len(image["breeds"]) > 0, "Expected at least one breed in the response"
    assert image["breeds"][0]["name"] == expected_breed, f"Expected breed name to be {expected_breed}"


def test_response_format():
    """Test that response contains expected fields."""
    response = requests.get(f"{BASE_URL}/images/search", headers=get_headers(), params={"limit": 1})
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert isinstance(data, list) and len(data) == 1, "Response should be a list with one item"
    image = data[0]
    assert "id" in image and "url" in image, "Each image should contain 'id' and 'url'"
    assert image["url"].startswith("http"), "Image URL should be valid"