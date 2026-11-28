from ai_summary import build_auth_headers, get_groq_api_key


def test_groq_api_key_loaded():
    key = get_groq_api_key()
    assert key.startswith("gsk_") and len(key) > 20


def test_build_auth_headers():
    key = get_groq_api_key()
    headers = build_auth_headers()
    assert headers["Authorization"] == f"Bearer {key}"
    assert headers["Content-Type"] == "application/json"
