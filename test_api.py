import os
os.environ["MOCK_AI"]="true"
from fastapi.testclient import TestClient
from backend.main import app
client=TestClient(app)
def test_root(): assert client.get("/").status_code==200
def test_health(): assert client.get("/health").json()["status"]=="ok"
def test_generate():
    r=client.post("/generate",json={"document_type":"NDA","parties":"ABC Pvt Ltd and John Doe","terms":"Confidential information must not be disclosed.","effective_date":"1 October 2026"})
    assert r.status_code==200 and "ABC Pvt Ltd" in r.json()["content"]
def test_validation(): assert client.post("/generate",json={"document_type":"","parties":"A","terms":"B","effective_date":"C"}).status_code==422
