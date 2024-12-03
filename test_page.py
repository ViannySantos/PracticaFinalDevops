import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def html_content():
    with open("index.html", "r") as f:
        return f.read()

def test_title(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    assert soup.title.string == "Hola Mundo"

def test_h1_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    h1 = soup.find("h1")
    assert h1.string == "Hola Mundo"
