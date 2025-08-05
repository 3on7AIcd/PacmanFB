import requests

BASE_URL = "http://localhost:8000"

def test_health_check():
    res = requests.get(f"{BASE_URL}/")
    assert res.status_code == 200
    print("✅ Health check passed.")

def test_chat_agent():
    res = requests.post(f"{BASE_URL}/chat-agent", json={"query": "What was my profit on Beef Wellington?"})
    assert res.status_code == 200
    print("✅ Chat agent response received.")

if __name__ == "__main__":
    test_health_check()
    test_chat_agent()