import string
from collections import Counter

def get_word_frequency(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    word_counts = Counter(words)
    return word_counts

def compare_texts(text1, text2, threshold=0.8):
    freq1 = get_word_frequency(text1)
    freq2 = get_word_frequency(text2)
    dot_product = sum(freq1[word] * freq2[word] for word in freq1 if word in freq2)
    magnitude1 = sum(freq1[word] ** 2 for word in freq1)
    magnitude2 = sum(freq2[word] ** 2 for word in freq2)
    similarity = dot_product / ((magnitude1 * magnitude2) ** 0.5)
    return similarity >= threshold

text1 = "sdagasd gsd fasdf ."
text2 = "The quick brown dog jumps over the lazy fox."

if compare_texts(text1, text2):
    print("Plagiarism detected!")
else:
    print("No plagiarism detected.")