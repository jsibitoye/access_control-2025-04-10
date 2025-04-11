Here is a simple Python program that simulates an access control system. The system allows users to create an account, login, logout, and access a restricted resource. The system also ensures that only logged-in users can access the restricted resource.

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

class AccessControlSystem:
    def __init__(self):
        self.users = {}

    # Function to create a new user account
    def create_account(self, username, password):
        if username in self.users:
            return "Username already exists. Please choose a different username."
        else:
            self.users[username] = User(username, password)
            return "Account created successfully."

    # Function to log in a user
    def login(self, username, password):
        if username in self.users:
            if self.users[username].password == password:
                self.users[username].logged_in = True
                return "Logged in successfully."
            else:
                return "Invalid password."
        else:
            return "Invalid username."

    # Function to log out a user
    def logout(self, username):
        if username in self.users:
            if self.users[username].logged_in:
                self.users[username].logged_in = False
                return "Logged out successfully."
            else:
                return "User is not logged in."
        else:
            return "Invalid username."

    # Function to access a restricted resource
    def access_resource(self, username):
        if username in self.users:
            if self.users[username].logged_in:
                return "Access granted."
            else:
                return "Access denied. Please log in first."
        else:
            return "Invalid username."

# Test the Access Control System
acs = AccessControlSystem()
print(acs.create_account("testuser", "testpassword"))
print(acs.login("testuser", "testpassword"))
print(acs.access_resource("testuser"))
print(acs.logout("testuser"))
print(acs.access_resource("testuser"))
```

In this program, I used a dictionary to store the users of the system. The keys in the dictionary are the usernames, and the values are User objects, which store the user's username, password, and login status. This design allows for efficient lookup, creation, and modification of users.

I also encapsulated the functionality of the system in an AccessControlSystem class, which provides methods for creating an account, logging in, logging out, and accessing a restricted resource. This design makes the code easy to read, understand, and maintain.