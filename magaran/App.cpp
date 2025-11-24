#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cctype>
#include <chrono>
#include <algorithm>
#include <fstream>

using namespace std;

// Structure to store word and its part-of-speech tag
struct Word {
    string text;
    string pos; // e.g., "NOUN", "VERB", "DET", "ADJ", "PREP", "ADV"
};

// Load dictionary with POS tags
vector<Word> load_dictionary(const string& filename = "wordlist.txt") {
    vector<Word> dictionary;
    ifstream file(filename);
    
    if (!file.is_open()) {
        cerr << "Warning: Could not open wordlist file '" << filename << "'. Using fallback dictionary." << endl;
        // Fallback dictionary tailored for "My name is tama" and general use
        return {
            {"my", "DET"}, {"the", "DET"}, {"a", "DET"}, {"an", "DET"},
            {"tama", "NOUN"}, {"man", "NOUN"}, {"name", "NOUN"}, {"sam", "NOUN"},
            {"cat", "NOUN"}, {"dog", "NOUN"}, {"he", "NOUN"}, {"she", "NOUN"},
            {"is", "VERB"}, {"am", "VERB"}, {"was", "VERB"}, {"say", "VERB"},
            {"smile", "VERB"}, {"sing", "VERB"}, {"play", "VERB"},
            {"big", "ADJ"}, {"small", "ADJ"}, {"happy", "ADJ"},
            {"in", "PREP"}, {"on", "PREP"}, {"with", "PREP"},
            {"only", "ADV"}, {"yes", "ADV"}
        };
    }

    string line;
    while (getline(file, line)) {
        size_t comma = line.find(',');
        if (comma != string::npos) {
            string word = line.substr(0, comma);
            string pos = line.substr(comma + 1);
            word.erase(remove_if(word.begin(), word.end(), ::isspace), word.end());
            pos.erase(remove_if(pos.begin(), pos.end(), ::isspace), pos.end());
            if (!word.empty() && all_of(word.begin(), word.end(), [](char c) { return isalpha(c); })) {
                transform(word.begin(), word.end(), word.begin(), ::tolower);
                dictionary.push_back({word, pos});
            }
        }
    }

    file.close();
    if (dictionary.empty()) {
        cerr << "Error: No valid words loaded from '" << filename << "'. Using fallback dictionary." << endl;
        return {
            {"my", "DET"}, {"the", "DET"}, {"a", "DET"}, {"an", "DET"},
            {"tama", "NOUN"}, {"man", "NOUN"}, {"name", "NOUN"}, {"sam", "NOUN"},
            {"cat", "NOUN"}, {"dog", "NOUN"}, {"he", "NOUN"}, {"she", "NOUN"},
            {"is", "VERB"}, {"am", "VERB"}, {"was", "VERB"}, {"say", "VERB"},
            {"smile", "VERB"}, {"sing", "VERB"}, {"play", "VERB"},
            {"big", "ADJ"}, {"small", "ADJ"}, {"happy", "ADJ"},
            {"in", "PREP"}, {"on", "PREP"}, {"with", "PREP"},
            {"only", "ADV"}, {"yes", "ADV"}
        };
    }

    cout << "Loaded " << dictionary.size() << " words from '" << filename << "'" << endl;
    
    // Sort by word length (descending) to prioritize longer words
    sort(dictionary.begin(), dictionary.end(),
         [](const Word& a, const Word& b) { return a.text.length() > b.text.length(); });
    // Remove duplicates based on word text
    dictionary.erase(unique(dictionary.begin(), dictionary.end(),
                           [](const Word& a, const Word& b) { return a.text == b.text; }),
                     dictionary.end());
    
    return dictionary;
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

// Subtract letters of word from letter counts
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

// Calculate total used letters
int sum_used_letters(const map<char, int>& used_letters) {
    int sum = 0;
    for (const auto& pair : used_letters) sum += pair.second;
    return sum;
}

// Update progress bar based on letters used
void update_progress_bar(int used_letters, int total_letters, int attempt_count) {
    int percent = (used_letters * 100) / total_letters;
    int length = 50;
    int filled = (used_letters * length) / total_letters;
    string bar(filled, '#');
    bar += string(length - filled, '-');
    cout << "\rProgress: " << used_letters << "/" << total_letters << " letters used |" << bar << "| "
         << percent << "% (Attempt #" << attempt_count << ")" << flush;
}

// Check if sentence is grammatically valid
bool is_grammatical(const vector<Word>& sentence) {
    if (sentence.size() < 2) return false;
    bool has_noun = false, has_verb = false;
    for (size_t i = 0; i < sentence.size(); ++i) {
        const auto& word = sentence[i];
        if (word.pos == "NOUN" || word.pos == "PRONOUN") has_noun = true;
        if (word.pos == "VERB") has_verb = true;
        // Encourage patterns: DET-NOUN, NOUN-VERB
        if (i == 0 && (word.pos == "DET" || word.pos == "NOUN" || word.pos == "PRONOUN")) continue;
        if (i > 0 && word.pos == "NOUN" && sentence[i-1].pos == "DET") continue;
        if (i > 0 && word.pos == "VERB" && (sentence[i-1].pos == "NOUN" || sentence[i-1].pos == "PRONOUN")) continue;
    }
    return has_noun && has_verb;
}

// Recursive function to find anagram sentence
bool find_anagram_sentence(map<char, int>& letters, const vector<Word>& dictionary, int total_letters,
                           vector<Word>& current_sentence, map<char, int>& used_letters, int depth,
                           int& attempt_count, vector<Word>& result) {
    string indent(depth * 2, ' ');

    // Base case: no letters remain and sentence is grammatical
    if (letters.empty() && is_grammatical(current_sentence)) {
        cout << "\n" << indent << "Found valid sentence: ";
        for (const auto& word : current_sentence) cout << word.text << " ";
        cout << endl;
        update_progress_bar(sum_used_letters(used_letters), total_letters, attempt_count);
        result = current_sentence;
        return true;
    }

    // Stop after too many attempts
    if (attempt_count > 1000000) {
        cout << "\n" << indent << "Maximum attempts reached. Stopping search." << endl;
        return false;
    }

    for (const auto& word : dictionary) {
        attempt_count++;
        // Log every 1000 attempts
        if (attempt_count % 1000 == 0) {
            cout << "\n" << indent << "Attempt #" << attempt_count << ": Trying word " << word.text
                 << " (" << word.pos << "), current sentence: ";
            for (const auto& w : current_sentence) cout << w.text << " ";
            cout << ", remaining letters: {";
            for (const auto& pair : letters) cout << pair.first << ":" << pair.second << " ";
            cout << "}" << endl;
            update_progress_bar(sum_used_letters(used_letters), total_letters, attempt_count);
        }

        if (can_form_word(word.text, letters)) {
            // Try word
            auto new_letters = subtract_letters(word.text, letters);
            current_sentence.push_back(word);
            auto new_used_letters = used_letters;
            for (char c : word.text) new_used_letters[tolower(c)]++;
            update_progress_bar(sum_used_letters(new_used_letters), total_letters, attempt_count);

            // Recurse
            if (find_anagram_sentence(new_letters, dictionary, total_letters, current_sentence,
                                     new_used_letters, depth + 1, attempt_count, result)) {
                return true;
            }

            // Backtrack
            current_sentence.pop_back();
        }
    }
    return false;
}

string rearrange_sentence(const string& sentence, const vector<Word>& dictionary) {
    // Get letter counts
    auto letter_counts = get_letter_counts(sentence);
    int total_letters = 0;
    for (const auto& pair : letter_counts) total_letters += pair.second;
    cout << "Input sentence: '" << sentence << "'" << endl;
    cout << "Letter counts: {";
    for (const auto& pair : letter_counts) cout << pair.first << ":" << pair.second << " ";
    cout << "}, total letters: " << total_letters << endl;

    // Filter dictionary
    vector<Word> filtered_dict;
    for (const auto& word : dictionary) {
        if (can_form_word(word.text, letter_counts)) {
            filtered_dict.push_back(word);
        }
    }
    cout << "Filtered dictionary size: " << filtered_dict.size() << " words" << endl;
    if (filtered_dict.empty()) {
        cout << "No words in dictionary can be formed from input letters." << endl;
        return "No valid rearrangement found.";
    }

    // Sort filtered dictionary by length (descending)
    sort(filtered_dict.begin(), filtered_dict.end(),
         [](const Word& a, const Word& b) { return a.text.length() > b.text.length(); });

    // Find anagram sentence
    vector<Word> current_sentence, result;
    map<char, int> used_letters;
    int attempt_count = 0;
    cout << "Progress: 0/" << total_letters << " letters used |" << string(50, '-') << "| 0%" << flush;

    if (find_anagram_sentence(letter_counts, filtered_dict, total_letters, current_sentence, used_letters,
                             0, attempt_count, result)) {
        string result_str;
        for (size_t i = 0; i < result.size(); ++i) {
            result_str += result[i].text;
            if (i < result.size() - 1) result_str += " ";
        }
        return result_str;
    }
    return "No valid rearrangement found.";
}

int main() {
    // Load dictionary
    auto dictionary = load_dictionary("wordlist.txt");

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
