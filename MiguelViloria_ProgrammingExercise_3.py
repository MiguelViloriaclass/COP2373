# Author: Miguel Viloria
# Date: September 19, 2026


def get_spam_keywords():
    """
    Returns a list of common spam keywords and phrases.

    Parameters:
        None

    Variables:
        spam_keywords (tuple): A tuple containing 30 spam terms.

    Logic:
        1. Define a tuple of 30 common spam words and phrases.
        2. Return the tuple.

    Return:
        tuple: A collection of 30 spam keywords.
    """
    # Define a list of 30 spam words and phrases to check
    spam_keywords = (
        "buy now", "free money", "earn extra cash", "no cost",
        "act now", "limited time", "guaranteed", "100% free",
        "winner", "congratulations", "urgent", "risk free",
        "double your income", "click here", "cash bonus", "special promotion",
        "passwords", "verify account", "bank transfer", "investment opportunity",
        "miracle cure", "cheap drugs", "exclusive deal", "unsubscribed",
        "apply now", "credit card required", "payout", "risk-free trial",
        "instant approval", "make money online"
    )
    return spam_keywords


def analyze_spam_score(email_text, spam_keywords):
    """
    Scans email text against spam terms and calculates score and matches.

    Parameters:
        email_text (str): The body text entered by the user.
        spam_keywords (tuple): Collection of spam terms to search.

    Variables:
        normalized_text (str): Lowercase version of input message.
        score (int): Cumulative counter of spam occurrences.
        matches (list): List of detected keywords or phrases.
        count (int): Occurrences of a single keyword.

    Logic:
        1. Convert email text to lower case for case insensitivity.
        2. Initialize score counter and empty matches list.
        3. Loop through spam keywords and count occurrences.
        4. Add occurrences to score and store matched terms.
        5. Return the total score and list of matches.

    Return:
        tuple: The calculated spam score and list of matched terms.
    """
    # Convert email to lower case for easy pattern matching
    normalized_text = email_text.lower()

    # Track overall spam points accumulated
    score = 0

    # Store any triggered spam words found in text
    matches = []

    # Check each spam phrase against the email body
    for word in spam_keywords:
        # Count occurrences of current word in text
        count = normalized_text.count(word)

        # If found, accumulate score and track the word
        if count > 0:
            score += count
            matches.append(word)

    return score, matches


def evaluate_spam_likelihood(score):
    """
    Rates the likelihood of email being spam based on calculated score.

    Parameters:
        score (int): Total accumulated spam score.

    Variables:
        None

    Logic:
        1. Evaluate score against defined thresholds.
        2. Return qualitative risk rating.

    Return:
        str: Description of spam likelihood level.
    """
    # Return risk rating based on score ranges
    if score == 0:
        return "Low (Unlikely to be Spam)"
    elif 1 <= score <= 4:
        return "Moderate (Possible Spam)"
    else:
        return "High (Very Likely Spam)"


def main():
    """
    Main function to run spam detector tool and present output.

    Parameters:
        None

    Variables:
        keywords (tuple): Retrieved list of spam phrases.
        user_email (str): Message text entered by user.
        total_score (int): Total calculated spam score.
        detected_words (list): List of phrases found in email.
        likelihood (str): Qualitative spam risk level.

    Logic:
        1. Load spam keywords database.
        2. Ask user for email message input.
        3. Calculate score and list triggered terms.
        4. Evaluate spam likelihood.
        5. Display final scan summary report.

    Return:
        None
    """
    # Print application header
    print("=" * 60)
    print("           EMAIL SPAM DETECTOR & RISK ANALYZER          ")
    print("=" * 60)

    # Load spam terms database
    keywords = get_spam_keywords()

    # Prompt user for email message text
    user_email = input("\nEnter the email message text to analyze:\n\n> ")

    # Calculate spam points and collect triggered terms
    total_score, detected_words = analyze_spam_score(user_email, keywords)

    # Determine risk level from accumulated points
    likelihood = evaluate_spam_likelihood(total_score)

    # Display analysis report summary
    print("\n" + "=" * 60)
    print("                    ANALYSIS RESULTS                    ")
    print("=" * 60)
    print(f"Spam Score accumulated : {total_score}")
    print(f"Spam Likelihood Rating : {likelihood}")

    # Output matched words list if present
    if detected_words:
        print("\nTriggered Keywords / Phrases Found:")
        for item in detected_words:
            print(f" - '{item}'")
    else:
        print("\nNo common spam keywords/phrases were detected in this message.")

    print("=" * 60)


if __name__ == "__main__":
    main()