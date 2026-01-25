import requests
import pytest
import json

@pytest.mark.mock_service
def test_mock():
    response = requests.get("http://mock-service:5000/health")
    assert response.status_code == 200
    message = json.dumps(response.text,indent=2)
    assert message is not None
    print("Response got from mock server is : "+str(message))