# Spam Email Classifier

This project is a simple web app that checks whether an email message looks like **spam** or **not spam**.

It was built with:

- **Python** for the programming logic
- **Streamlit** for the web interface
- **scikit-learn** for the machine learning model
- A saved **vectorizer** and **model** so the app can make predictions instantly

The app is designed to be easy to run locally on your computer. You paste in an email, click a button, and the app gives you:

- A result such as `Likely Spam` or `Looks Clean`
- A confidence score shown as a percentage
- A cleaner visual breakdown showing how strongly the model leans toward each result

## What Is In This Project

- `app.py`  
  The main Streamlit app. This is what creates the page, loads the saved files, accepts email text, and shows the result.

- `model.pkl`  
  The trained machine learning model. This is the part that decides whether the text looks like spam or not.

- `vectorizer.pkl`  
  The text converter. It turns normal email text into numbers the model can understand.

- `requirements.txt`  
  The list of Python libraries needed to run the app.

## How The Project Works In Simple Terms

Think of the app like this:

1. You paste an email into the box.
2. The app breaks that text into a machine-readable format.
3. The trained model compares the text to patterns it learned earlier.
4. The app shows whether it thinks the message is spam or not spam.
5. It also shows how confident it is about that decision.

In plain English:

- The **vectorizer** is like a translator. It changes words into numbers.
- The **model** is like a decision-maker. It looks at those numbers and guesses the category.
- **Streamlit** is what turns everything into a simple page with a text box and button.

## How It Was Built

This project appears to have been built in three main parts:

### 1. A spam detection model was trained earlier

Someone first trained a machine learning model outside this app using email or message examples labeled as:

- `spam`
- `not spam`

That trained model was then saved into:

- `model.pkl`

### 2. A text vectorizer was saved

Machine learning models do not understand raw sentences directly. Because of that, a text vectorizer was also created and saved into:

- `vectorizer.pkl`

Its job is to take a piece of text like:

`Congratulations, you won a free prize`

and convert it into a pattern of numbers the model can use.

### 3. A Streamlit app was added

The `app.py` file loads both saved files and creates a small website where the user can:

- Paste email text
- Click `Analyze Email`
- See the prediction and confidence scores

The current version of the app also includes:

- A cleaner centered layout
- Custom styling for the text box and button
- A more polished result card
- Percentage bars for spam vs not spam confidence

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

Open PowerShell and move into the project folder:

```powershell
cd C:\Users\alihu\Projects\aifinalporject
```

## 2. Create A Fresh Virtual Environment

This creates a clean Python environment just for this project:

```powershell
py -m venv .venv
```

If `py` does not work, try:

```powershell
python -m venv .venv
```

## 3. Activate The Virtual Environment

In PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, run this once in the same PowerShell window:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, you should usually see something like `(.venv)` at the start of the terminal line.

## 4. Install The Required Packages

Run:

```powershell
pip install -r requirements.txt
```

This installs:

- Streamlit
- scikit-learn
- pandas
- numpy

## 5. Start The App

Run:

```powershell
streamlit run app.py
```

Streamlit should open a browser tab automatically. If it does not, PowerShell will show a local URL, usually something like:

`http://localhost:8501`

Open that in your browser.

## 6. Stop The App

When you are done, go back to the terminal and press:

```text
Ctrl + C
```

## Simple Usage Guide For A Non-Technical Person

If you have never used a coding project before, this is the easiest way to think about it:

1. Start the app.
2. A page opens in your browser.
3. Copy the email message you want to check.
4. Paste it into the big text box.
5. Click the `Analyze Email` button.
6. Read the result shown on the screen.

You will see one of these:

- `Likely Spam`
- `Looks Clean`

You will also see numbers that show confidence. A higher number means the model feels more sure about its answer.

Example:

- `Likely Spam` with `92% confidence` means the app is very confident the message looks suspicious.
- `Looks Clean` with `88% confidence` means the app is quite confident the message looks safe.

## Full Step-By-Step Example

Here is a simple example of how someone would use the project from start to finish:

1. Open PowerShell.
2. Go to the project folder.
3. Activate the virtual environment.
4. Run `streamlit run app.py`.
5. Wait for the browser page to open.
6. Paste an email such as:

```text
Congratulations! You have won a free gift card. Click here now to claim your reward.
```

7. Click `Analyze Email`.
8. Read the result.
9. Try another email if you want.
10. Press `Ctrl + C` in PowerShell when finished.

## Example Emails To Try

You can copy and paste these into the app to see how it behaves.

### Example 1: Likely Spam

```text
Congratulations! You have won a free gift card. Click here now to claim your reward. This offer expires today.
```

Why it may be flagged:

- It uses urgent wording
- It promises a reward
- It asks the user to click quickly

### Example 2: Likely Not Spam

```text
Hi Sarah, just checking if we are still meeting tomorrow at 2 PM in the office. Please let me know if you want to move it to 3 PM instead.
```

Why it may be seen as normal:

- It sounds like a regular work message
- It does not ask for money or personal details
- It does not use suspicious reward language

### Example 3: Another Likely Spam Example

```text
Dear customer, your account has been selected for a special cash bonus. Verify your details immediately to receive your payment.
```

### Example 4: Another Likely Not Spam Example

```text
Hello team, the weekly report is attached. Please review it before Friday and share any comments by the end of the day.
```

Note:

These are good test messages for the app, but the exact result and confidence percentage can vary depending on how the model was trained.

## What The User Sees In The App

The app now has a simple but cleaner layout:

- A title: `Spam Checker`
- A short instruction telling the user to paste an email below
- A large text box
- A button called `Analyze Email`
- A result card showing either `Likely Spam` or `Looks Clean`
- A confidence breakdown with percentage bars for `Spam` and `Not Spam`

This makes it easy for someone to use the project without understanding the code.

## What Happens Behind The Scenes

When the user presses the button, this is what happens:

1. The app checks whether the text box is empty.
2. If it is empty, it shows a warning asking the user to enter text.
3. If text is present, the app sends the email text to the vectorizer.
4. The vectorizer converts the text into a numerical format.
5. The model predicts the class.
6. The model also calculates class probabilities.
7. The app displays:
   - the final label
   - the confidence percentage
   - the spam and not spam confidence bars

## Who This Project Is For

This project is good for:

- Students learning about machine learning
- Beginners learning Streamlit
- Small demos or classroom presentations
- People who want a simple example of text classification

## Limitations

This project is useful as a demo, but it is important to understand its limits:

- It only knows what it learned from the data it was trained on
- It may be wrong on unusual or tricky emails
- It should not be used as the only security tool for real-world email protection
- The training script and training dataset are not included in this folder

## Troubleshooting

### Problem: `streamlit` is not recognized

Try:

```powershell
python -m streamlit run app.py
```

or:

```powershell
py -m streamlit run app.py
```

Make sure the virtual environment is activated first.

### Problem: package install fails

Make sure Python is installed correctly:

```powershell
py --version
```

If that does not work, try:

```powershell
python --version
```

### Problem: the included `venv` does not work

Delete or ignore the old `venv` folder and create a new one:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Problem: nothing happens when clicking the button

Make sure:

- you pasted email text into the box
- the app is still running in the terminal
- the browser page has not disconnected from Streamlit

## Quick Start

If you just want the shortest version:

```powershell
cd C:\Users\alihu\Projects\aifinalporject
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Summary

This is a beginner-friendly spam email classification app built with Streamlit and a pre-trained machine learning model.

The basic flow is:

1. User pastes email text
2. Text is converted into numbers
3. Model predicts spam or not spam
4. App shows the result and confidence

If you want to improve the project later, the next natural upgrades would be:

- add the model training notebook or script
- include example test emails
- show cleaner confidence percentages
- deploy the app online
