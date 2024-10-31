# FlashCard Quiz Application
#### Video Demo:  <https://youtu.be/L-jRTzDvn2g>

## Overview

The Flashcard Quiz Application is a command-line tool created to assist users in creating, managing, and testing themselves using flashcards. It supports adding, viewing, and deleting flashcards, as well as quizzing oneself. The application aims to facilitate active learning and memory retention through interactive flashcard sessions.

## Project Structure

The project comprises two primary files:

1. `project.py`: Houses the core functionalities of the application, including loading and saving flashcards, managing flashcard data, and providing an interactive command-line interface for user interaction.
2. `test_project.py`: Contains test cases written using the `pytest` framework to ensure the proper functioning of the FlashCard Quiz Application.

## Design of `project.py`

`project.py` houses the core functionalities of the application. It is responsible for loading and saving flashcards, managing flashcard data, and providing an interactive command-line interface for user interaction. The design choice to implement these functionalities within a single file aims to maintain simplicity and ease of understanding.

#### Key Design Aspects:

1. **Modular Design**: The code is organized into functions, each handling specific tasks such as loading flashcards or adding new ones. This modular design enhances code readability and maintainability.

2. **Interactive CLI**: The command-line interface (CLI) allows users to interact with the application seamlessly. Commands like `add`, `view`, `delete`, `quiz`, and `exit` provide intuitive ways to manage and quiz flashcards.

3. **File I/O with JSON**: Flashcards are stored in a JSON format for easy storage and retrieval. This design choice facilitates data persistence and simplifies the implementation of file I/O operations.

## Design of `test_project.py`

`test_project.py` contains test cases written using the `pytest` framework to ensure the proper functioning of the FlashCard Quiz Application. Testing this codebase poses certain challenges due to its design, particularly regarding file I/O operations and interactive CLI functionalities.

#### Difficulty in Testing:

1. **Dependency on External Resources**: Testing functions that involve file I/O operations requires creating and manipulating temporary files. While `pytest` provides fixtures like `tmp_path` for this purpose, setting up and tearing down these resources in tests can be complex.

2. **Handling User Input**: Testing functions that interact with the CLI involves simulating user input and capturing program output. This necessitates using tools like `pytest`'s `capsys` fixture to capture stdout and stdin streams, adding complexity to test setup and assertions.

3. **Integration Testing Challenges**: Verifying the integration of different components, such as CLI interaction with flashcard management functions, requires comprehensive testing scenarios. This involves designing test cases that cover various user inputs and edge cases, potentially leading to lengthy and intricate tests.

## Conclusion

The FlashCard Quiz Application's design prioritizes simplicity, modularity, and user-friendliness in its main implementation (`project.py`). However, testing this codebase poses challenges due to its reliance on external resources and interactive functionalities. Overcoming these challenges requires careful test design, leveraging `pytest`'s features for managing test fixtures and capturing program output. Despite the difficulties, thorough testing is crucial to ensuring the application's reliability and functionality across different usage scenarios.