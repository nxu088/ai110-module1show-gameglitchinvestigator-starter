# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- This is a number guessing game where the player chooses a difficulty and a number is generated within a range and guesses until they are correct or out of attempts and receives a score based on it.
- hard diffculty range (1-50) was easier than normal (1-100)
-hint messages were swapped, "too high" said go higher and "too low" said go lower
-the score added 5 points for wrong "too high" guesses on even numbered tries
-"new game" button reset attempts to 0 and not 1

- changed hard range from (1,50) to (1,100) and normal from (1,100) to (1,50) and the number of attempts to 5,6,8 respectively
-changed hint messages so that "too high" displays "go lower" and "too low" displays go higher"
-update_score subtracts 5 for wrong guesses on all attempts
-updated new game to reset attempts to 1 as well as score, status, and history

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Launch the app with `python -m streamlit run app.py the game is loaded with normal difficulty (if the answer is 64)
2. Enter 20 and click Submit. The hint says "Go HIGHER!" the score decreases by 5 points. Attempts left is 6.
3. Enter 70 and click Submit. The hint says "Go LOWER!" and the score again decreases by 5. Attempts left is 5.
4. Enter 64 and click Submit. The game displays "🎉 Correct!", balloons appear, and the final score is shown.
5. Click "New Game" to guess a new number. The score resets to 0, attempts are reset, and the history is cleared.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

==================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\nxu08\Documents\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 15 items                                                                                                                                   

tests\test_game_logic.py ...............                                                                                                       [100%]

# ========================= 15 passed in 0.15s =========================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]