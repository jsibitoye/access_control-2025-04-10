Here's an example of a simple access control mechanism using Java. This program will create a `User` class with a username and role, and a `AccessControl` class to manage access to certain operations based on the role of the user.

```java
// User class to hold user information
class User {
    private String username;
    private String role;

    public User(String username, String role) {
        this.username = username;
        this.role = role;
    }

    public String getUsername() {
        return username;
    }

    public String getRole() {
        return role;
    }
}

// AccessControl class to manage access to certain operations
class AccessControl {
    public void grantAccess(User user, String operation) {
        // Check user role before granting access
        if (user.getRole().equals("admin")) {
            System.out.println("Access granted to " + user.getUsername() + " for operation " + operation);
        } else {
            System.out.println("Access denied to " + user.getUsername() + " for operation " + operation);
        }
    }
}

// Main class to test the access control mechanism
public class Main {
    public static void main(String[] args) {
        User admin = new User("admin", "admin");
        User user = new User("user", "user");

        AccessControl ac = new AccessControl();
        ac.grantAccess(admin, "delete");
        ac.grantAccess(user, "delete");
    }
}
```

In this program, only users with the role "admin" are allowed to perform the "delete" operation. If a user with a different role tries to perform this operation, the access control mechanism will deny access. This is a simple example, but you can extend this concept to create more complex access control mechanisms.

Note: In a real-world scenario, you might want to use more sophisticated methods for access control, such as Access Control Lists (ACLs) or Role-Based Access Control (RBAC), and you would likely integrate with a database or other persistent storage to manage users and roles.