import requests

def send_to_langflow(question: str, session_id: str, flow_id: str):
    url = f"http://192.168.15.101:7860/api/v1/run/{flow_id}"
    
    payload = {
        "input_value": question,
        "output_type": "chat",
        "input_type": "chat",
        "stream": False,
        "session_id": session_id
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    return response
