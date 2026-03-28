# Spam Email Classifier

This project is a beginner-friendly Streamlit app that checks whether an email message looks like **spam** or **not spam**.

The current version is built around a **manual Multinomial Naive Bayes implementation** written in Python. That means the classification logic is visible in the project code instead of being hidden entirely inside a machine learning library model.

## What This Project Does

The app lets a user:

1. Paste an email into a text box
2. Click `Analyze Email`
3. See whether the message is likely spam or likely safe
4. View a confidence breakdown for both `Spam` and `Not Spam`

## Project Files

- `app.py`  
  The Streamlit web app that loads the training data, trains the manual classifier, and shows the interface.

- `manual_naive_bayes.py`  
  The core AI implementation. This file contains the manual Naive Bayes algorithm, including tokenization, training, prediction, and probability calculation.

- `data/spam_dataset.csv`  
  The bundled training dataset used by the app. It contains example emails labeled as `spam` or `not spam`.

- `requirements.txt`  
  The Python package list needed to run the app.

- `model.pkl` and `vectorizer.pkl`  
  Older saved files from an earlier library-based version of the project. The current app does not depend on them.

## How The AI Works In Simple Terms

The app learns from example emails. During startup, it reads the dataset and separates the training messages into two groups:

- spam emails
- not spam emails

It then counts how often each word appears in each group. When a new email is entered, the app:

1. Breaks the text into words
2. Looks at which words are common in spam emails
3. Looks at which words are common in non-spam emails
4. Calculates a score for both classes
5. Chooses the class with the higher score

In simple English:

- If a message contains words that often appear in spam, the spam score goes up.
- If a message contains words that often appear in normal messages, the not-spam score goes up.
- The higher score becomes the prediction.

## Manual Naive Bayes Logic

This project uses a manual version of **Multinomial Naive Bayes**.

The algorithm follows these steps:

### 1. Tokenization

The email is converted into lowercase words using a simple tokenizer.

Example:

`Claim your free prize now`

becomes words like:

- `claim`
- `your`
- `free`
- `prize`
- `now`

### 2. Training

During training, the model counts:

- how many spam emails exist
- how many non-spam emails exist
- how many times each word appears in spam emails
- how many times each word appears in non-spam emails

### 3. Prior Probabilities

The model calculates:

- `P(spam)` = spam emails / total emails
- `P(not spam)` = non-spam emails / total emails

These are the starting probabilities before looking at the words.

### 4. Word Likelihoods

For each word, the model calculates:

- `P(word | spam)`
- `P(word | not spam)`

Laplace smoothing is used so that unseen words do not produce zero probability.

### 5. Log Scores

To avoid multiplying many tiny probabilities, the app uses log scores:

- `spam_score = log(P(spam)) + sum(log(P(word | spam)))`
- `ham_score = log(P(not spam)) + sum(log(P(word | not spam)))`

### 6. Final Prediction

If `spam_score` is larger, the app predicts spam. Otherwise, it predicts not spam.

## How It Was Built

This version of the project was built in three simple parts:

### 1. A labeled dataset was added

A CSV file named `data/spam_dataset.csv` was created with example emails labeled as:

- `spam`
- `not spam`

### 2. A manual Naive Bayes classifier was implemented

The file `manual_naive_bayes.py` includes:

- a tokenizer
- word-frequency counting
- prior probability calculation
- likelihood calculation
- log-probability scoring
- prediction and probability output

### 3. A Streamlit interface was connected to the manual model

The `app.py` file:

- loads the dataset
- trains the manual model on startup
- accepts email text from the user
- runs prediction using the manual classifier
- shows the result in a simple UI

## Step-By-Step Setup

These instructions are written for a beginner using **Windows PowerShell**.

## Before You Start

Make sure you have:

- Python 3.10 or newer installed
- Internet access to install packages
- This project folder on your computer

You can download Python from [python.org](https://www.python.org/downloads/).

Important note:

This project already contains a `venv` folder, but on some computers it may not work properly if it was created from a different Python installation. If that happens, create a fresh one using the steps below.

## 1. Open PowerShell In The Project Folder

```powershell
cd C:\Users\alihu\Projects\aifinalporject
```

## 2. Create A Fresh Virtual Environment

```powershell
py -m venv .venv
```

If `py` does not work, try:

```powershell
python -m venv .venv
```

## 3. Activate The Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 4. Install The Required Package

```powershell
pip install -r requirements.txt
```

This app currently needs:

- Streamlit

## 5. Start The App

```powershell
streamlit run app.py
```

Streamlit should open a browser tab automatically. If it does not, open the local address shown in the terminal, usually:

`http://localhost:8501`

## 6. Stop The App

Press:

```text
Ctrl + C
```

## Simple Usage Guide For A Non-Technical Person

1. Start the app.
2. Wait for the page to open in your browser.
3. Copy the email message you want to check.
4. Paste it into the text box.
5. Click `Analyze Email`.
6. Read the result.

You will see either:

- `Likely Spam`
- `Looks Clean`

You will also see confidence percentages for both spam and non-spam.

## Example Emails To Try

### Example 1: Likely Spam

```text
Congratulations! You have won a free gift card. Click here now to claim your reward. This offer expires today.
```

### Example 2: Likely Not Spam

```text
Hi Sarah, just checking if we are still meeting tomorrow at 2 PM in the office. Please let me know if you want to move it to 3 PM instead.
```

### Example 3: Another Likely Spam Example

```text
Dear customer, your account has been selected for a special cash bonus. Verify your details immediately to receive your payment.
```

### Example 4: Another Likely Not Spam Example

```text
Hello team, the weekly report is attached. Please review it before Friday and share any comments by the end of the day.
```

Note:

These are useful test messages, but the exact confidence can vary depending on the dataset and word patterns used by the classifier.

## What The User Sees In The App

The app has:

- a title called `Spam Checker`
- a short instruction message
- a large text box
- an `Analyze Email` button
- a result card
- confidence bars for spam and not spam

## What Happens Behind The Scenes

When the user clicks the button:

1. The app checks that text was entered.
2. The app sends the text to the manual Naive Bayes classifier.
3. The classifier tokenizes the words.
4. The classifier computes spam and not-spam scores using its learned word frequencies.
5. The app shows the final label and confidence percentages.

## Why This Version Better Matches The Assignment

This version is more suitable for an AI assignment because the core algorithm is now visible in code. Instead of only loading a saved library model, the project now shows:

- how the data is read
- how the model is trained
- how probabilities are calculated
- how the final prediction is made

## Limitations

- The bundled dataset is small, so predictions are mainly for demonstration and learning.
- The classifier only looks at email text.
- It does not inspect links, attachments, sender reputation, or metadata.
- Real-world spam filtering systems are much more advanced than this classroom example.

## Quick Start

```powershell
cd C:\Users\alihu\Projects\aifinalporject
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Summary

This project is a simple spam email classifier with a manual Naive Bayes implementation and a Streamlit interface. The user pastes an email, the app compares its words to the training examples, and the system predicts whether the message is spam or not spam.
