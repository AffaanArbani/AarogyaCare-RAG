"""
Test Redis chat memory.
"""

from chatbot.memory import (
    save_message,
    get_chat_history,
    clear_chat_history,
)

SESSION_ID = "test_session"

# Start fresh
clear_chat_history(SESSION_ID)

# Save messages
save_message(
    SESSION_ID,
    "user",
    "I have severe back pain."
)

save_message(
    SESSION_ID,
    "assistant",
    "Try resting and applying a warm compress."
)

save_message(
    SESSION_ID,
    "user",
    "What exercises should I do?"
)

# Retrieve history
history = get_chat_history(SESSION_ID)

print("=" * 60)
print("Conversation History")
print("=" * 60)

for message in history:
    print(f"{message['role']}: {message['message']}")

# Cleanup
clear_chat_history(SESSION_ID)

print("\n✅ Memory module is working correctly.")