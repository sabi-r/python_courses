#
#
# import requests
#
# def test_status_code():
#     url = "https://postman-rest-api-learner.glitch.me//info"
#     payload = {"name": "Add your name in the body"}
#     response = requests.request("POST", url, json=payload)
#     assert response.status_code == 200
#
# def test_status_code():
#     url = "https://uat.4ratech.com/api/v1/client/create-transaction"
#     payload = {
#         "customer_id": "c922d3dd-d039-4cbe-b788-ec388e278546",
#         "amount": 4284,
#         "currency": "INR",
#         "type": "imps",
#         "webhook_url": "https://uat.4ratech.com/api/test"
#     }
#     response = requests.request("POST", url, json=payload)
#     assert response.status_code == 200

import requests

def test_authentication():
    auth_url = "https://uat.4ratech.com/api/v1/app/auth/login"
    auth_data = {
        "username": "rahimova_sabi",
        "password": "R0McaWZ3Ybfb1xiy",
        "device_name": "postman"
    }
    headers = {
        "Accept": "application/json"
    }

    response = requests.post(auth_url, json=auth_data, headers=headers)

    assert response.status_code == 200, f"Authentication failed. Status code: {response.status_code}"

if __name__ == "__main__":
    test_authentication()
