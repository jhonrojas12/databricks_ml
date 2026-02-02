import requests
import json

url = "https://<workspace>.databricks.com/model/AutomatedMLModel/1/invocations"
token = "<DATABRICKS_PERSONAL_ACCESS_TOKEN>"

# Ejemplo de payload (así espera MLflow)
data = {
    "columns": ["feature1", "feature2", "feature3"],
    "data": [
        [1.2, 3.4, 5.6],
        [7.8, 9.0, 1.2]
    ]
}

response = requests.post(
    url,
    headers={"Authorization": f"Bearer {token}"},
    data=json.dumps(data)
)

print(response.json())
