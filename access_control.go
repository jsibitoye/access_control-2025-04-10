Here's a simple Go program that implements an access control system. This program uses a map to store users and their corresponding roles. The program has functions to add users, assign roles, and check if a user has a certain role. 

```go
package main

import (
	"fmt"
)

// User struct represents a user in the system
type User struct {
	Name string
	Role string
}

// AccessControl struct represents the access control system
type AccessControl struct {
	Users map[string]User // map of users with their name as the key
}

// NewAccessControl creates a new access control system
func NewAccessControl() *AccessControl {
	return &AccessControl{Users: make(map[string]User)}
}

// AddUser adds a new user to the access control system
func (ac *AccessControl) AddUser(name string, role string) {
	ac.Users[name] = User{Name: name, Role: role}
}

// AssignRole assigns a role to a user
func (ac *AccessControl) AssignRole(name string, role string) {
	user, exists := ac.Users[name]
	if exists {
		user.Role = role
		ac.Users[name] = user
	}
}

// HasRole checks if a user has a certain role
func (ac *AccessControl) HasRole(name string, role string) bool {
	user, exists := ac.Users[name]
	if exists {
		return user.Role == role
	}
	return false
}

func main() {
	ac := NewAccessControl()

	ac.AddUser("Alice", "admin")
	ac.AddUser("Bob", "user")

	fmt.Println(ac.HasRole("Alice", "admin")) // Output: true
	fmt.Println(ac.HasRole("Bob", "admin"))   // Output: false

	ac.AssignRole("Bob", "admin")

	fmt.Println(ac.HasRole("Bob", "admin")) // Output: true
}
```

This program is a simple representation of an access control system and does not include any kind of authentication or password protection for users. In a real-world application, you would need to implement these features as well as others such as role hierarchies, permissions, etc.