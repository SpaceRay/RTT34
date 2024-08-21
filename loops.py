# Function to capitalize a name
def capitalize(name):
    return name.title()  # Use title() if you want to capitalize each word

# Get user input for a name
user_name = input("Enter a name to capitalize: ").strip()  # Remove leading/trailing whitespace

# Capitalize and print the user input
capitalized_user_name = capitalize(user_name)
print(capitalized_user_name)