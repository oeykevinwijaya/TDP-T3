from flask import Flask, render_template, request
from webscraping.main import chatbot_function  # Adjust the import path as needed
import csv

app = Flask(__name__)

# Load and process FAQ data from the local csv file
faq_data = []
<<<<<<< HEAD
with open("faq_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        faq_data.append({"Question": row["Question"], "Answer": row["Answer"]})
=======
# Initialize a list to store the conversation history
conversation_history = []
>>>>>>> main


# Define a route for the homepage
@app.route("/")
def home():
    # Check if there is an answer to display
    greeting = "Hello! How may I assist you with Swinburne Online's FAQ today?"
    # Render the homepage template and pass the answer to it
    return render_template("index.html", answer=greeting)


# Define a route to handle user input and display responses
@app.route("/ask", methods=["POST"])
def ask():
    # Get the user's question from the form
<<<<<<< HEAD
    user_question = request.form.get("user_question")

    # Check if user selected a suggestion
    selected_suggestion = request.form.get("selected_suggestion")

    if selected_suggestion:
        # User selected a suggestion, find the corresponding answer
        selected_answer = next(
            faq["Answer"] for faq in faq_data if faq["Question"] == selected_suggestion
        )
        return render_template("index.html", answer=selected_answer, suggestions=None)

    # If no suggestion is selected, pass the question and FAQ data to the chatbot function
    response, suggestions = chatbot_function(user_question, faq_data)

    if suggestions:
        # Define the default message if suggestions are available
        default_message = "Here are some suggestions for you."
    else:
        # If no suggestions, set the default message to an empty string
        default_message = ""

    # Render the homepage template with the default message, response, and suggestions
    return render_template(
        "index.html",
        answer=default_message if default_message else response,
        suggestions=suggestions,
    )

=======
    user_question = request.form.get('user_question', '')
    
    # If the user has selected a suggestion, use it as the user_question
    selected_suggestion = request.form.get('selected_suggestion')
    if selected_suggestion:
        user_question = selected_suggestion
    
    # Call chatbot_function to get a response and suggestions
    response, suggestions = chatbot_function(user_question, faq_data)
    
    # If a suggestion was selected, find the corresponding answer
    if selected_suggestion:
        response = next(faq["Answer"] for faq in faq_data if faq["Question"] == selected_suggestion)
        suggestions = None  # No need to display suggestions if one is selected
    
    # Update conversation history
    conversation_history.append({"User Query": user_question, "Response": response or suggestions})
    
    # Render the template with all necessary variables
    return render_template(
        'index.html', 
        conversation_history=conversation_history,
        answer=response or "Here are some suggestions for you.", 
        suggestions=suggestions, 
        user_question=user_question
    )
>>>>>>> main

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
