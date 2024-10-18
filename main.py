import customtkinter as ctk
import threading
from chatbot_app import AwesomeChatbotApp

def run_chatbot(app):
    # This function runs your chatbot logic in a separate thread
    app.run_chat_logic()

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = AwesomeChatbotApp(root)

    # Start chatbot logic in a new thread
    chatbot_thread = threading.Thread(target=run_chatbot, args=(app,))
    chatbot_thread.daemon = True  # So it exits when the main thread exits
    chatbot_thread.start()

    root.mainloop()
