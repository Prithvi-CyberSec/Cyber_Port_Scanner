from scanner.services import get_service

def test_service_lookup():
    assert get_service(80) == "HTTP"
