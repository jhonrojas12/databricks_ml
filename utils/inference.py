import requests
import json

def predict(features: list[list], columns: list, model_url: str, token: str):
    payload = {
        "columns": columns,
        "data": features
    }
    response = requests.post(
        model_url,
        headers={"Authorization": f"Bearer {token}"},
        data=json.dumps(payload)
    )
    return response.json()
