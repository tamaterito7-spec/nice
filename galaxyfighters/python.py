from collections import Counter
import string
import time
from tqdm import tqdm
import sys

def load_dictionary():
    # Sample dictionary (replace with /usr/share/dict/words or another word list)
    return [
        'the', 'he', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
        'i', 'it', 'for', 'not', 'on', 'with', 'as', 'you', 'do', 'at',
        'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her',
        'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there',
        'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get',
        'which', 'go', 'me', 'big', 'dwarf', 'only', 'jumps', 'dog', 'cat',
        'run', 'is', 'are', 'was', 'were', 'sing', 'play', 'take', 'read'
    ]

def get_letter_counts(text):
    # Convert text to lowercase and count only letters
    text = text.lower()
    return Counter(char for char in text if char in string.ascii_lowercase)

def can_form_word(word, letter_counts):
    # Check if a word can be formed with the available letter counts
    word_counts = Counter(word.lower())
    return all(word_counts[char] <= letter_counts.get(char, 0) for char in word_counts)

def subtract_letters(word, letter_counts):
    # Subtract the letters of the word from letter counts
    result = letter_counts.copy()
    for char in word.lower():
        if char in result:
            result[char] -= 1
            if result[char] == 0:
                del result[char]
    return result

def update_progress_bar(pbar, used_letters, total_letters):
    # Update the overall progress bar based on letters used
    used_count = sum(used_letters.values())
    pbar.n = used_count
    pbar.set_description(f"Overall Progress: {used_count}/{total_letters} letters used")
    pbar.refresh()

def find_anagram_sentence(letters, dictionary, total_letters, pbar, current_sentence=None, used_letters=None, depth=0, attempt_count=[0]):
    if current_sentence is None:
        current_sentence = []
    if used_letters is None:
        used_letters = Counter()

    indent = "  " * depth

    # Base case: if no letters remain, we have a valid sentence
    if not letters:
        print(f"\n{indent}Found valid sentence: {' '.join(current_sentence)}")
        update_progress_bar(pbar, used_letters, total_letters)
        return current_sentence

    for word in dictionary:
        attempt_count[0] += 1
        # Log progress every 500 attempts
        if attempt_count[0] % 500 == 0:
            print(f"\n{indent}Attempt #{attempt_count[0]}: Trying word '{word}', "
                  f"current sentence: {' '.join(current_sentence)}, "
                  f"remaining letters: {dict(letters)}")
            update_progress_bar(pbar, used_letters, total_letters)

        if can_form_word(word, letters):
            # Log the attempt (less frequently)
            if attempt_count[0] % 500 == 0:
                print(f"{indent}Trying word '{word}' at depth {depth}, "
                      f"current sentence: {' '.join(current_sentence + [word])}, "
                      f"remaining letters: {dict(letters)}")

            # Try adding this word
            new_letters = subtract_letters(word, letters)
            current_sentence.append(word)
            update_progress_bar(pbar, used_letters + Counter(word.lower()), total_letters)
            
            # Recurse
            result = find_anagram_sentence(new_letters, dictionary, total_letters, pbar,
                                         current_sentence, used_letters + Counter(word.lower()),
                                         depth + 1, attempt_count)
            if result:
                return result
            
            # Backtrack
            current_sentence.pop()
            if attempt_count[0] % 500 == 0:
                print(f"{indent}Backtracking from '{word}' at depth {depth}, "
                      f"current sentence: {' '.join(current_sentence)}, "
                      f"remaining letters: {dict(letters)}")
            update_progress_bar(pbar, used_letters, total_letters)

    return None

def rearrange_sentence(sentence, dictionary):
    # Get letter counts from input sentence
    letter_counts = get_letter_counts(sentence)
    total_letters = sum(letter_counts.values())
    
    print(f"Starting with input sentence: '{sentence}'")
    print(f"Letter counts: {dict(letter_counts)}, total letters: {total_letters}")
    
    # Filter dictionary to only include valid words
    dictionary = [word for word in dictionary if can_form_word(word, letter_counts)]
    print(f"Filtered dictionary size: {len(dictionary)} words")
    
    # Initialize overall progress bar
    with tqdm(total=total_letters, file=sys.stdout, leave=True) as pbar:
        pbar.set_description(f"Overall Progress: 0/{total_letters} letters used")
        # Find a valid anagram sentence
        result = find_anagram_sentence(letter_counts, dictionary, total_letters, pbar)
    
    if result:
        # Verify the result uses exactly the same letters
        result_counts = get_letter_counts(''.join(result))
        if result_counts == letter_counts:
            return ' '.join(result)
        else:
            return "No valid rearrangement found (result doesn't match input letters)."
    else:
        return "No valid rearrangement found."

# Main function to process input and output
def main():
    # Load dictionary
    dictionary = load_dictionary()
    
    # Get input sentence
    sentence = input("Enter a sentence to rearrange: ")
    
    # Get and print the rearranged sentence
    start_time = time.time()
    result = rearrange_sentence(sentence, dictionary)
    end_time = time.time()
    print(f"\nRearranged sentence: {result}")
    print(f"Processing time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
