class User:
    def __init__(self):
        self.__password = None

    def set_password(self, password: str):
        """Set the user's password."""
        self.__password = password

    def is_valid_password(self, password: str) -> bool:
        """Check if the provided password matches the user's password."""
        return password == self.__password

# Example usage
if __name__ == "__main__":
    user = User()
    user.set_password("Test User")
    provided_password = input("Enter a password: ")  # Get user input
    if user.is_valid_password(provided_password):
        print("Password is valid.")
    else:
        print("Invalid password.")

