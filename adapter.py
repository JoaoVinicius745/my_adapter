from input.langflow import send_to_langflow

def adapter(question: str, session_id: str, flow_id: str):
    response = send_to_langflow(question, session_id, flow_id)

    if response.ok:
        return response.json()
    else:
        return {
            "error": "Erro na chamada à nova API",
            "details": response.text
        }
