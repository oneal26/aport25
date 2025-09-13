import re
from collections import Counter

def analyze_text(text):

    # total characters 
    total_characters = len(text)

    # total words
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)

    # average word length 
    if total_words > 0:
        average_word_length = sum(len(word) for word in words) / total_words
    else: 
        average_word_length = 0

    # sentence count 
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    total_sentences = len(sentences)

    # most common words
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(5)

    return {
        "total_characters": total_characters,
        "total_words": total_words,
        "average_word_length": average_word_length,
        "total_sentences": total_sentences,
        "most_common_words": most_common_words
    }

# main function handle usser interaction and display statistics 
def main():
    print("Text Analysis")
    print("------------------------")

    choice = input("Analyze from (F)ile or (U)ser input ").strip().lower()

    if choice == 'f':
        file_path = input("Enter text file path: ").strip()
        try:
            with open(file_path, 'r', encoding='utf-8') as f: 
                text_content = f.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return
        except Exception as e: 
            print(f"An error occured while reading the file: {e}")
            return 
    elif choice == 'u':
        print("Enter your text (press Enter twice to complete):")
        lines = []
        while True: 
            line = input()
            if not line:
                break
            lines.append(line)
        text_content = "\n".join(lines)
    else: 
        print("Invalid choice. Enter 'F' or 'U'.")
        return 

    if not text_content: 
        print("No text provided for analysis.")
        return

    statistics = analyze_text(text_content)

    print("\n--- Text Statistics ---")
    print(f"Total Characters: {statistics['total_characters']}")
    print(f"Total Words: {statistics['total_words']}")
    print(f"Average Word Length: {statistics['average_word_length']:.2f}")
    print(f"Total Sentences: {statistics['total_sentences']}")
    print("Most Common Words:")
    for word, count in statistics['most_common_words']:
        print(f"  - '{word}': {count} times")

if __name__ == "__main__":
    main()
