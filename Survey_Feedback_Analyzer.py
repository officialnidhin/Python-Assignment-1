# ============================================
# MODULE END ASSIGNMENT 4
# PROJECT: SURVEY FEEDBACK ANALYZER
# ============================================

# STEP 1: PRELOADED FEEDBACK DATA

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print("Survey Feedback Analyzer")
print("Initial feedbacks loaded:", len(feedback_data['Name']))


# ============================================
# STEP 2: ADD MORE FEEDBACKS
# ============================================

number_of_feedbacks = int(input("How many more feedbacks do you want to add? "))

for i in range(number_of_feedbacks):

    print("\nEnter details for feedback", i + 1)

    # Automatically generate serial number
    serial_number = len(feedback_data['S_No']) + 1

    # Get user inputs
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    # Validate rating between 1 and 5
    while True:
        try:
            rating = int(input("Enter rating (1-5): "))

            if 1 <= rating <= 5:
                break
            else:
                print("Invalid rating! Please enter a number between 1 and 5.")

        except ValueError:
            print("Please enter a valid integer.")

    # Add the new information to the dictionary
    feedback_data['S_No'].append(serial_number)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

    print("Feedback added successfully!")

# ============================================
# STEP 3: TEXT CLEANING
# ============================================

for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]

    # Remove punctuation
    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")
    feedback = feedback.replace("!", "")
    feedback = feedback.replace("?", "")

    # Remove extra spaces and leading/trailing spaces
    feedback = " ".join(feedback.split())

    # Convert text to lowercase
    feedback = feedback.lower()

    # Store the cleaned feedback
    feedback_data['Feedback'][i] = feedback

print("\nText cleaning completed successfully!")

# ============================================
# STEP 4: WORD COUNT INSIGHTS
# ============================================

def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        words = feedback.split()

        if word.lower() in words:
            count += 1

    return count


# Display word count insights
print("\nWord Count Insights")

print("Feedbacks containing 'good':",
      count_word_in_feedbacks("good"))

print("Feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))

print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))


# ============================================
# STEP 5: FINAL SUMMARY AND INSIGHTS
# ============================================

print("\n" + "=" * 40)
print("FINAL SUMMARY AND INSIGHTS")
print("=" * 40)

# 1. Calculate average rating
total_rating = sum(feedback_data['Rating'])
number_of_feedbacks = len(feedback_data['Rating'])

if number_of_feedbacks > 0:
    average_rating = total_rating / number_of_feedbacks
    print("Average Rating:", round(average_rating, 2))
else:
    print("No ratings available.")

# 2. Find the longest feedback
if feedback_data['Feedback']:
    longest_feedback = max(
        feedback_data['Feedback'],
        key=len
    )
    print("Longest Feedback:", longest_feedback)
else:
    print("No feedback available.")

# 3. Find unique words
unique_words = set()

for feedback in feedback_data['Feedback']:
    words = feedback.split()
    unique_words.update(words)

print("Number of Unique Words:", len(unique_words))
print("Unique Words:", sorted(unique_words))

# 4. Display total feedback count
print("Total Number of Feedbacks:",
      len(feedback_data['Feedback']))

print("=" * 40)
print("Analysis completed successfully!")
