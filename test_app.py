import pytest
from ui import run_interview_bot

def test_empty_answer_validation():
    """
    UNIT TEST: Ensures the backend gracefully catches empty user strings
    before wasting external cloud API tokens.
    """
    print("\nRunning automated validation check on empty text inputs...")
    
    # 1. Simulate a user hitting 'Submit' with an empty string of spaces
    mock_user_input = "   " 
    
    # 2. Execute the updated backend function (Now passing all 4 parameters!)
    test_result = run_interview_bot(
        job_domain="Python Developer Intern", 
        current_question="What is a decorator in Python?",  # Added this matching parameter!
        user_answer=mock_user_input, 
        action_type="Evaluate Answer"
    )
    
    # 3. Assert (verify) that the function output matches our defensive alert exactly
    expected_warning = "⚠️ Validation Error: Please type an answer in the text box before submitting for evaluation!"
    
    assert test_result == expected_warning
    print("✅ Test Passed: Backend successfully blocked an empty submission!")

if __name__ == "__main__":
    # Run the test directly if executed as a script
    test_empty_answer_validation()