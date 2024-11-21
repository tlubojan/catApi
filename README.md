# The Cat Api - Test Suite

## Setup Instructions

1. **Clone the repository**:
```bash
   git clone https://github.com/tlubojan/catApi.git
   cd catApi
   ```
2. Install dependencies: 
```bash
   pip install -r requirements.txt
```
3. Set the API Key:
Use environment variable:
```bash
   export CAT_API_KEY=<you_api_key>
```
OR add your API key to config.json file

## Running Tests
1. Run Tests:
```bash
   pytest
```
2. To generate html report:
```bash
   pytest --html=report.html
```

## Test Scenarios
1. Retrieve Cat Images - Validate that the API returns the correct number of images
2. Get Images By Breed - This test case verifies that the API returns images of cats belonging to specific breeds
3. Response Format - Validate that the response contains expected fields (id, url)

## Add More tests
To extend the test suite:
1. Add new test functions in tests/test_cat_api.py