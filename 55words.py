#!/usr/bin/env python3
import sys
import re

def normalize_text(text):
    """
    Normalize fancy quotes, apostrophes, and dashes to simplified versions.
    """
    replacements = {
        '‘': "'", '’': "'",  # Curly single quotes to straight apostrophe
        '“': '"', '”': '"',  # Curly double quotes to straight double quote
        '—': '-', '–': '-',  # Em dashes and en dashes to hyphen
        '…': '...',          # Ellipsis to three dots
    }
    for fancy, simple in replacements.items():
        text = text.replace(fancy, simple)
    return text

def count_words(text):
    """
    Count words based on the rules provided:
    - Contractions (like "he'll" and "skull's") count as one word.
    - Hyphenated words that can stand alone (like "blue-green") count as multiple words.
    """
    # Regex pattern to match words, including contractions
    word_pattern = re.compile(
        r"\b[A-Za-z0-9]+(?:'[a-zA-Z]+)?\b"  # Handles contractions like "he's"
        r"|\b[A-Z]\."                       # Handles initials like "J.K."
    )
    
    words = word_pattern.findall(text)
    count = 0

    for word in words:
        # Check if it's a hyphenated word
        if '-' in word:
            parts = word.split('-')
            # Count as multiple words if both parts are valid standalone words
            if all(part.isalpha() for part in parts) and len(parts) > 1:
                count += len(parts)
            else:
                count += 1
        else:
            count += 1

    return count

def main():
    # Read the entire content from stdin
    content = sys.stdin.read().strip()
    
    # Normalize the text to replace fancy quotes, apostrophes, and other characters
    content = normalize_text(content)
    
    # Count words in the body content
    body_word_count = count_words(content)
    print(f"Body word count: {body_word_count} (limit is 55 words)")
    
    if body_word_count > 55:
        print("Error: Exceeded the 55-word limit.")
        sys.exit(1)

if __name__ == "__main__":
    main()
