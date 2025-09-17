import time
import random

# Some sample text passages
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and versatile programming language.",
    "Typing speed tests are a fun way to improve accuracy and speed.",
    "Artificial intelligence is shaping the future of technology"
    
    "Practice makes perfect when it comes to typing fast and correctly."
]

def typing_test():
    # Select random text
    text = random.choice(texts)
    print("\n📜 Your text to type:\n")
    print(text)
    print("\nStart typing when you are ready...\n")

    # Wait for user to start typing
    input("Press Enter to start...")

    # Start timer
    start_time = time.time()
    typed_text = input("\nType here: \n")
    end_time = time.time()

    # Calculate time taken
    time_taken = end_time - start_time
    time_taken = round(time_taken, 2)

    # Calculate speed
    words = len(typed_text.split())
    speed = round((words / time_taken) * 60, 2)  # words per minute

    # Calculate accuracy
    correct_chars = 0
    for i, char in enumerate(typed_text):
        if i < len(text) and typed_text[i] == text[i]:
            correct_chars += 1
    accuracy = round((correct_chars / len(text)) * 100, 2)

    # Show results
    print("\n⏱ Time Taken:", time_taken, "seconds")
    print("⚡ Typing Speed:", speed, "WPM")
    print("🎯 Accuracy:", accuracy, "%")

# Run the test
typing_test()