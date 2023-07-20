def decorator(func):
    def wrapper(stop_words: list, sentence):
        modified_sentence = ['*' if word.lower() in stop_words else word for word in sentence.split(" ")]
        return func(stop_words, modified_sentence)
    return wrapper


@decorator
def function(stop_words: list, sentence):
    return f"Sentence after the changes: '{' '.join(sentence)}'."


stop_words_list = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its',
                   'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']
sentence_about_cat = "The cat sat on the mat and looked at the sky"
print(f"Sentence before the changes: '{sentence_about_cat}'.")
print(function(stop_words_list, sentence_about_cat))
