def greet_user(username):
    """Displays a simple greeting."""
    return f"Welcome back, {username.title()}!"

# Calling the function and printing the result
message = greet_user("sarah")
print(message)
