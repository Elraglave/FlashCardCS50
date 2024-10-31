import json
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

# Function to load flashcards from a JSON file
def load_flashcards(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save flashcards to a JSON file
def save_flashcards(file_path, flashcards):
    with open(file_path, 'w') as file:
        json.dump(flashcards, file)

# Function to add a flashcard
def add_flashcard(flashcards, question, answer):
    flashcards.append({"question": question, "answer": answer})

# Function to delete a flashcard
def delete_flashcard(flashcards, index):
    if 0 <= index < len(flashcards):
        flashcards.pop(index)

# Function to display flashcards using rich with borders
def display_flashcards_rich(flashcards):
    for idx, card in enumerate(flashcards):
        panel_content = f"[bold]Question:[/bold] {card['question']}\n[bold]Answer:[/bold] {card['answer']}"
        panel = Panel(panel_content, title=f"Flashcard {idx}", border_style="bold blue")
        console.print(panel)

# Function to enhance the display of add operation
def add_flashcard_display(flashcards, file_path):
    question = Prompt.ask("Enter question")
    answer = Prompt.ask("Enter answer")
    add_flashcard(flashcards, question, answer)
    save_flashcards(file_path, flashcards)
    console.print(f"[green]Flashcard added![/green] Question: {question} | Answer: {answer}")

# Function to enhance the display of delete operation
def delete_flashcard_display(flashcards, file_path):
    index = int(Prompt.ask("Enter index to delete"))
    if 0 <= index < len(flashcards):
        deleted_card = flashcards[index]
        delete_flashcard(flashcards, index)
        save_flashcards(file_path, flashcards)
        console.print(f"[red]Flashcard deleted![/red] Question: {deleted_card['question']} | Answer: {deleted_card['answer']}")
    else:
        console.print("[bold red]Invalid index![/bold red]")

# Function to enhance the display of quiz operation
def quiz_flashcards_display(flashcards):
    score = 0
    for card in flashcards:
        answer = Prompt.ask(card['question'])
        if answer.lower() == card['answer'].lower():
            score += 1
            console.print("[green]Correct![/green]")
        else:
            console.print(f"[red]Incorrect.[/red] The correct answer was: {card['answer']}")
    console.print(f"[bold]You got {score} out of {len(flashcards)} correct.[/bold]")

# Main function to run the flashcard quiz application
def main():
    file_path = 'flashcards.json'
    flashcards = load_flashcards(file_path)

    while True:
        command = Prompt.ask("Enter command (add/view/delete/quiz/exit)").strip().lower()
        if command == 'add':
            add_flashcard_display(flashcards, file_path)
        elif command == 'view':
            display_flashcards_rich(flashcards)
        elif command == 'delete':
            delete_flashcard_display(flashcards, file_path)
        elif command == 'quiz':
            quiz_flashcards_display(flashcards)
        elif command == 'exit':
            break
        else:
            console.print("[bold red]Unknown command.[/bold red]")

if __name__ == "__main__":
    main()