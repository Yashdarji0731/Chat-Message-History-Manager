This Python project implements a simple chat history manager with undo/redo functionality. It uses a queue (FIFO) to hold incoming messages and two stacks (LIFO) to manage undo and redo operations. Each message is stored along with a timestamp of when it was sent. The program provides a text-based menu so the user can send messages, view the chat history, undo the last message, redo an undone message, or exit. The design is modular and well-commented, suitable for a GitHub repository and easy for beginners to follow.

Features & How to Run: This program uses Python’s standard libraries (collections.deque, datetime) and requires no special setup. To run it, save the code to a .py file (for example, chat_manager.py) and execute it with Python 3 (python chat_manager.py). Follow the on-screen menu to send messages, undo/redo, view history, or exit.

overview of the code

🔹 How It Works

ChatMessage Class

Represents a single chat message.

Stores message text and timestamp.

Provides a formatted string for display like:

[2025-08-20 12:30:45] Hello!


ChatHistoryManager Class

Core manager that handles all operations:

incoming → a queue (deque) for incoming messages.

undo_stack → a stack (list) for storing sent messages.

redo_stack → a stack for storing undone messages (for redo).

Functions:

send_message() → Adds a new message.

view_history() → Shows all past messages.

undo() → Removes the last message and moves it to the redo stack.

redo() → Restores the last undone message.

main() function (Menu-driven app)

Provides a simple menu for the user to interact with:

1. Send a new message
2. View chat history
3. Undo last message
4. Redo last undone message
5. Exit


Keeps running until the user chooses to exit.
