# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
When I first ran the game, it seemed to do so correctly with being able to take in inputs of numbers and given hints based upon what was put in. Then, I realized that the hints were guiding in the wrong direction when it was supposed to be higher it said lower and vice versa. Additionally, the ranges for the difficulty needed to be adjusted as it was originally 1-50 for hard when it should be 1-100 and there were less guesses as well. 
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Select hard difficulty|Range should be the highest|Range was 1-50 which was smaller than normal's 1-100 |error in get_range_for_difficulty |
|Guess number lower than secret|Hint should say "go higher"|Hint says "go lower"|error in check_guess function |
|Guess on even attempts |Guess should be correctly compared to the secret number|Secret set to string so hints and score incorrect|Error in check_guess|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

On this project, I used Claude. One example of an AI suggestion that was correct was the hint messages being swapped and verified this by testing different guesses to make sure that the same result was being produced. After fixing, the game was rerun to see if the error is corrected. An incorrect or misleading suggestion was somewhat overcomplicating what was needing to be fixed such as with changing the ranges of the difficulties so I ended up fixing this bug myself in the code.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I decided whether a bug was really fixed by running a test case to see if it had changed. For example, by checking 70 and 50 I made sure that the outcome of "Too High" had a hint of "go lower" instead of "go higher" like it was previously doing. The test cases from Claude also had helped to ensure that the code was running smoothly after changing the bugs that I had encountered in the code. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Reruns are where it goes through the entire script from top to bottom everytime something happens. By using session state, it allows for Streamlit to preserve the data between each run to remember what has happened before. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One habit or strategy from this project that I want to reuse in future labs or projects is coming up with targeted pytest cases when fixing bugs. By doing this, it was helpful to run them to make sure everything was running as it should be and can be rerun. 
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently next time I work with AI on a coding task would be giving it more precise directions. This is because by using clearer prompts it would help to ensure expected results.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project changed the way that I think about AI generated code can look like it is correct but still have logic errors within it when using test cases. As a result, it is good to think of it as a starting point that I should go through and make changes where necessary to provide the best possible finished product in the end.
