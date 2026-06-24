from logic_utils import check_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win 🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High 📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low 📈 Go HIGHER!"

def test_guess_edge_cases():
    # Test edge cases for the check_guess function
    assert check_guess(1, 1) == "Win 🎉 Correct!"
    assert check_guess(100, 100) == "Win 🎉 Correct!"
    assert check_guess(0, 50) == "Too Low 📈 Go HIGHER!"
    assert check_guess(101, 50) == "Too High 📉 Go LOWER!"


# --- Bug-targeted tests ---

# Bug: check_guess had reversed hint direction (Go HIGHER when should be LOWER, and vice versa)
def test_too_high_message_says_go_lower():
    result = check_guess(75, 50)
    assert "LOWER" in result
    assert "HIGHER" not in result

def test_too_low_message_says_go_higher():
    result = check_guess(25, 50)
    assert "HIGHER" in result
    assert "LOWER" not in result


# Bug: get_range_for_difficulty had Hard (1–50) and Normal (1–100) swapped
def test_hard_difficulty_range_is_widest():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    _, easy_high = get_range_for_difficulty("Easy")
    assert hard_high > normal_high > easy_high

def test_hard_difficulty_max_is_100():
    _, high = get_range_for_difficulty("Hard")
    assert high == 100

def test_normal_difficulty_max_is_50():
    _, high = get_range_for_difficulty("Normal")
    assert high == 50

def test_easy_difficulty_max_is_20():
    _, high = get_range_for_difficulty("Easy")
    assert high == 20


# Bug: update_score used (attempt_number + 1) making first-win score 80 instead of 90
def test_win_on_first_attempt_score():
    score = update_score(0, "Win", 1)
    assert score == 90  # 100 - 10*1; buggy version gave 100 - 10*2 = 80

def test_win_on_second_attempt_score():
    score = update_score(0, "Win", 2)
    assert score == 80  # 100 - 10*2; buggy version gave 100 - 10*3 = 70


# Bug: update_score gave +5 on even attempts for "Too High" instead of always -5
def test_too_high_always_subtracts_on_odd_attempt():
    score = update_score(100, "Too High", 1)
    assert score == 95

def test_too_high_always_subtracts_on_even_attempt():
    # Buggy version returned current_score + 5 on even attempts
    score = update_score(100, "Too High", 2)
    assert score == 95  # should not be 105

def test_too_low_always_subtracts():
    assert update_score(100, "Too Low", 1) == 95
    assert update_score(100, "Too Low", 2) == 95
