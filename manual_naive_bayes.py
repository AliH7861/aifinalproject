import csv
import math
import re
from collections import Counter


class ManualNaiveBayes:
    def __init__(self):
        self.spam_word_counts = Counter()
        self.ham_word_counts = Counter()
        self.spam_docs = 0
        self.ham_docs = 0
        self.spam_total_words = 0
        self.ham_total_words = 0
        self.vocabulary = set()
        self.classes_ = ["not spam", "spam"]

    def tokenize(self, text):
        return re.findall(r"[a-zA-Z0-9']+", text.lower())

    def fit(self, texts, labels):
        for text, label in zip(texts, labels):
            words = self.tokenize(text)

            if label == "spam":
                self.spam_docs += 1
                self.spam_word_counts.update(words)
                self.spam_total_words += len(words)
            else:
                self.ham_docs += 1
                self.ham_word_counts.update(words)
                self.ham_total_words += len(words)

            self.vocabulary.update(words)

    def _log_scores(self, text):
        words = self.tokenize(text)
        total_docs = self.spam_docs + self.ham_docs

        if total_docs == 0:
            raise ValueError("Model has not been trained yet.")

        vocab_size = max(len(self.vocabulary), 1)

        spam_score = math.log(self.spam_docs / total_docs)
        ham_score = math.log(self.ham_docs / total_docs)

        for word in words:
            spam_word_prob = (self.spam_word_counts[word] + 1) / (
                self.spam_total_words + vocab_size
            )
            ham_word_prob = (self.ham_word_counts[word] + 1) / (
                self.ham_total_words + vocab_size
            )

            spam_score += math.log(spam_word_prob)
            ham_score += math.log(ham_word_prob)

        return ham_score, spam_score

    def predict(self, texts):
        predictions = []

        for text in texts:
            ham_score, spam_score = self._log_scores(text)
            predictions.append("spam" if spam_score > ham_score else "not spam")

        return predictions

    def predict_proba(self, texts):
        probabilities = []

        for text in texts:
            ham_score, spam_score = self._log_scores(text)

            max_score = max(ham_score, spam_score)
            ham_exp = math.exp(ham_score - max_score)
            spam_exp = math.exp(spam_score - max_score)
            total = ham_exp + spam_exp

            probabilities.append([ham_exp / total, spam_exp / total])

        return probabilities


def load_training_data(csv_path):
    texts = []
    labels = []

    with open(csv_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            texts.append(row["text"])
            labels.append(row["label"])

    return texts, labels
