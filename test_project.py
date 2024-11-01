import pytest
import json
from project import load_flashcards, save_flashcards, add_flashcard, delete_flashcard

@pytest.fixture
def sample_flashcards():
    return [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2+2?", "answer": "4"}
    ]

def test_load_flashcards(tmp_path):
    file_path = tmp_path / "flashcards.json"
    data = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2+2?", "answer": "4"}
    ]
    file_path.write_text(json.dumps(data))
    flashcards = load_flashcards(file_path)
    assert flashcards == data

def test_save_flashcards(tmp_path):
    file_path = tmp_path / "flashcards.json"
    data = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2+2?", "answer": "4"}
    ]
    save_flashcards(file_path, data)
    assert json.loads(file_path.read_text()) == data

def test_add_flashcard(sample_flashcards):
    flashcards = sample_flashcards.copy()
    add_flashcard(flashcards, "What is the capital of Spain?", "Madrid")
    assert flashcards[-1] == {"question": "What is the capital of Spain?", "answer": "Madrid"}

def test_delete_flashcard(sample_flashcards):
    flashcards = sample_flashcards.copy()
    delete_flashcard(flashcards, 0)
    assert len(flashcards) == 1
    assert flashcards[0] == {"question": "What is 2+2?", "answer": "4"}
