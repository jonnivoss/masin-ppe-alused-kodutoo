import csv
from collections import Counter
import math

# Read and preprocess training data
train_data = []
with open("bbc_train.csv", encoding="utf-8") as f:
    rd = csv.reader(f)
    for genre, text in rd:
        words = [w.lower() for w in text.split() if len(w) > 3]
        train_data.append((genre, words))#adds the training data into a list

# Calculate probabilities for each word and genre
genre_word_probs = {genre: Counter(words) for genre, words in train_data}
genre_probs = {genre: len(words) for genre, words in train_data}

# Implement Naive Bayes classifier
def predict_genre(article):
    words = [w.lower() for w in article.split() if len(w) > 3]
    log_probs = {genre: math.log(len(words) / (genre_probs[genre] + sum(genre_word_probs[genre].values()) + len(set(words))))
                 + sum(math.log((genre_word_probs[genre][word] + 1) / (genre_probs[genre] + len(set(words))))
                       for word in words)
                 for genre in genre_probs}

    return max(log_probs, key=log_probs.get)

countOfArticles = 0
countOfCorrectlyGuessedArticles = 0
# Read and classify test data
with open("bbc_test.csv", encoding="utf-8") as f:
    rd = csv.reader(f)
    for topic, text in rd:
        predicted_genre = predict_genre(text)
        print(f"Article topic: {topic}, Predicted genre: {predicted_genre}")
        countOfArticles +=1
        if topic == predicted_genre:
            countOfCorrectlyGuessedArticles += 1

print(f"we correctly guessed {countOfCorrectlyGuessedArticles} out of a {countOfArticles}")