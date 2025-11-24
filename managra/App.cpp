#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cctype>
#include <chrono>
#include <algorithm>

using namespace std;

// Dictionary (sample, replace with file loading if needed)
vector<string> load_dictionary() {
    return {
        "the", "he", "be", "to", "of", "and", "a", "in", "that", "have",
        "i", "it", "for", "not", "on", "with", "as", "you", "do", "at",
        "this", "but", "his", "by", "from", "they", "we", "say", "her",
        "she", "or", "an", "will", "my", "one", "all", "would", "there",
        "their", "what", "so", "up", "out", "if", "about", "who", "get",
        "which", "go", "me", "big", "dwarf", "only", "jumps", "dog", "cat",
        "run", "is", "are", "was", "were", "sing", "play", "take", "read"
    };
}

// Convert string to letter counts
map<char, int> get_letter_counts(const string& text) {
    map<char, int> counts;
    for (char c : text) {
        if (isalpha(c)) {
            counts[tolower(c)]++;
        }
    }
    return counts;
}

// Check if a word can be formed with available letters
bool can_form_word(const string& word, const map<char, int>& letter_counts) {
    map<char, int> word_counts;
    for (char c : word) {
        word_counts[tolower(c)]++;
    }
    for (const auto& pair : word_counts) {
        if (letter_counts.find(pair.first) == letter_counts.end() || letter_counts.at(pair.first) < pair.second) {
            return false;
        }
    }
    return true;
}

// Subtract word's letters from letter counts
map<char, int> subtract_letters(const string& word, const map<char, int>& letter_counts) {
    map<char, int> result = letter_counts;
    for (char c : word) {
        c = tolower(c);
        if (result[c] > 1) {
            result[c]--;
        } else {
            result.erase(c);
        }
    }
    return result;
}

// Update progress bar based on letters used
void update_progress_bar(int used_letters, int total_letters, int attempt_count) {
    int percent = (used_letters * 100) / total_letters;
    int length = 50;
    int filled = (used_letters * length) / total_letters;
    string bar(filled, '#');
    bar += string(length - filled, '-');
    cout << "\rOverall Progress: " << used_letters << "/" << total_letters << " letters used |" << bar << "| "
         << percent << "% (Attempt #" << attempt_count << ")" << flush;
}

// Recursive function to find anagram sentence
bool find_anagram_sentence(map<char, int>& letters, const vector<string>& dictionary, int total_letters,
                           vector<string>& current_sentence, map<char, int>& used_letters, int depth,
                           int& attempt_count, vector<string>& result) {
    string indent(depth * 2, ' ');

    // Base case: no letters remain
    if (letters.empty()) {
        cout << "\n" << indent << "Found valid sentence: ";
        for (const auto& word : current_sentence) cout << word << " ";
        cout << endl;
        update_progress_bar(sum_used_letters(used_letters), total_letters, attempt_count);
        result = current_sentence;
        return true;
    }

    for (const string& word : dictionary) {
        attempt_count++;
        // Log every 500 attempts
        if (attempt_count % 500 == 0) {
            cout << "\n" << indent << "Attempt #" << attempt_count << ": Trying word '" << word
                 << "', current sentence: ";
            for (const auto& w : current_sentence) cout << w << " ";
            cout << ", remaining letters: {";
            for (const auto& pair : letters) cout << pair.first << ":" << pair.second << " ";
            cout << "}" << endl;
            update_progress_bar(sum_used_letters(used_letters), total_letters, attempt_count);
        }

        if (can_form_word(word, letters)) {
            // Try word
            if (attempt_count % 500 == 0) {
                cout << indent << "Trying word '" << word << "' at depth " << depth
                     << ", current sentence: ";
                for (const auto& w : current_sentence) cout << w << " ";
                cout << word << ", remaining letters: {";
                for (const auto& pair : letters) cout << pair.first << ":" << pair.second << " ";
                cout << "}" << endl;
            }

            auto new_letters = subtract_letters(word, letters);
            current_sentence.push_back(word);
            auto new_used_letters = used_letters;
            for (char c : word) new_used_letters[tolower(c)]++;
            update_progress_bar(sum_used_letters(new_used_letters), total_letters, attempt_count);

            // Recurse
            if (find_anagram_sentence(new_letters, dictionary, total_letters, current_sentence,
                                     new_used_letters, depth + 1, attempt_count, result)) {
                return true;
            }

            // Backtrack
            current_sentence.pop_back();
            if (attempt_count % 500 == 0) {
                cout << indent << "Backtracking from '" << word << "' at depth " << depth
                     << ", current sentence: ";
                for (const auto& w : current_sentence) cout << w << " ";
                cout << ", remaining letters: {";
                for (const auto& pair : letters) cout << pair.first << ":" << pair.second << " ";
                cout << "}" << endl;
            }
            update_progress_bar(sum_used_letters(used_letters), total_letters, attempt_count);
        }
    }
    return false;
}

// Helper to calculate total used letters
int sum_used_letters(const map<char, int>& used_letters) {
    int sum = 0;
    for (const auto& pair : used_letters) sum += pair.second;
    return sum;
}

string rearrange_sentence(const string& sentence, const vector<string>& dictionary) {
    // Get letter counts
    auto letter_counts = get_letter_counts(sentence);
    int total_letters = 0;
    for (const auto& pair : letter_counts) total_letters += pair.second;
    cout << "Starting with input sentence: '" << sentence << "'" << endl;
    cout << "Letter counts: {";
    for (const auto& pair : letter_counts) cout << pair.first << ":" << pair.second << " ";
    cout << "}, total letters: " << total_letters << endl;

    // Filter dictionary
    vector<string> filtered_dict;
    for (const auto& word : dictionary) {
        if (can_form_word(word, letter_counts)) {
            filtered_dict.push_back(word);
        }
    }
    cout << "Filtered dictionary size: " << filtered_dict.size() << " words" << endl;

    // Find anagram sentence
    vector<string> current_sentence, result;
    map<char, int> used_letters;
    int attempt_count = 0;
    cout << "Overall Progress: 0/" << total_letters << " letters used |" << string(50, '-') << "| 0%" << flush;

    if (find_anagram_sentence(letter_counts, filtered_dict, total_letters, current_sentence, used_letters,
                             0, attempt_count, result)) {
        string result_str;
        for (size_t i = 0; i < result.size(); ++i) {
            result_str += result[i];
            if (i < result.size() - 1) result_str += " ";
        }
        return result_str;
    }
    return "No valid rearrangement found.";
}

int main() {
    // Load dictionary
    auto dictionary = load_dictionary();

    // Get input
    string sentence;
    cout << "Enter a sentence to rearrange: ";
    getline(cin, sentence);

    // Process and time
    auto start = chrono::high_resolution_clock::now();
    string result = rearrange_sentence(sentence, dictionary);
    auto end = chrono::high_resolution_clock::now();
    cout << "\nRearranged sentence: " << result << endl;
    cout << "Processing time: " << chrono::duration<double>(end - start).count() << " seconds" << endl;

    return 0;
}
