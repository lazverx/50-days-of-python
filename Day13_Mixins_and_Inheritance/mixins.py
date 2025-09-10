import datetime


class LoggerMixin:
    """Mixin to provide logging capability."""
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class TimestampMixin:
    """Mixin to add created_at and updated_at timestamps."""
    def __init__(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def touch(self):
        """Update the 'updated_at' timestamp."""
        self.updated_at = datetime.datetime.now()


class BaseUser:
    """Base user with simple attributes."""
    def __init__(self, username: str):
        self.username = username


# Inheritance + Mixins
class User(BaseUser, LoggerMixin, TimestampMixin):
    def __init__(self, username: str, email: str):
        BaseUser.__init__(self, username)
        TimestampMixin.__init__(self)
        self.email = email

    def update_email(self, new_email: str):
        self.email = new_email
        self.touch()  # update timestamp
        self.log(f"Email for {self.username} updated to {new_email}")


if __name__ == "__main__":
    user = User("alice", "alice@example.com")
    print(f"User created: {user.username}, email: {user.email}")
    print(f"Created at: {user.created_at}")

    user.update_email("alice@newmail.com")
    print(f"Updated at: {user.updated_at}")
