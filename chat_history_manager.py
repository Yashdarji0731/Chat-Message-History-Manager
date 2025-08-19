from collections import deque
from datetime import datetime

class ChatMessage:
    """Represents a chat message with content and timestamp."""
    def __init__(self, text):
        self.text = text
        # Record the current timestamp
        self.timestamp = datetime.now()

    def __str__(self):
        # Format message with timestamp for display
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.text}"

class ChatHistoryManager:
    """Manages chat history using a queue and stacks for undo/redo."""
    def __init__(self):
        # Queue for incoming messages (FIFO)
        self.incoming = deque()
        # Stack of sent messages (LIFO)
        self.undo_stack = []
        # Stack of undone messages (for redo)
        self.redo_stack = []

    def send_message(self, text):
        """Sends a new chat message."""
        msg = ChatMessage(text)
        # Simulate incoming queue: append and then immediately dequeue
        self.incoming.append(msg)
        message = self.incoming.popleft()
        # Add to the history stack and clear any redo history
        self.undo_stack.append(message)
        self.redo_stack.clear()
        print(f"Message sent: {message}")

    def view_history(self):
        """Displays all messages in chat history (oldest first)."""
        if not self.undo_stack:
            print("(No messages in chat history.)")
        else:
            print("Chat History:")
            for msg in self.undo_stack:
                print(msg)

    def undo(self):
        """Undo the last sent message (remove it from history)."""
        if not self.undo_stack:
            print("Nothing to undo.")
        else:
            message = self.undo_stack.pop()
            self.redo_stack.append(message)
            print(f"Undid message: {message}")

    def redo(self):
        """Redo the last undone message (restore it to history)."""
        if not self.redo_stack:
            print("Nothing to redo.")
        else:
            message = self.redo_stack.pop()
            self.undo_stack.append(message)
            print(f"Redid message: {message}")

def main():
    manager = ChatHistoryManager()
    while True:
        print("\n=== Chat Menu ===")
        print("1. Send a new message")
        print("2. View chat history")
        print("3. Undo last message")
        print("4. Redo last undone message")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()
        if choice == '1':
            text = input("Enter your message: ")
            manager.send_message(text)
        elif choice == '2':
            manager.view_history()
        elif choice == '3':
            manager.undo()
        elif choice == '4':
            manager.redo()
        elif choice == '5':
            print("Exiting chat.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
