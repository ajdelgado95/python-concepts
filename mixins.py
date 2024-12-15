class LoggingMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class FileProcessor(LoggingMixin):
    def process(self, file_name):
        self.log(f"Processing file: {file_name}")
        # File processing logic here
        print(f"File {file_name} processed.")

class DataAnalyzer(LoggingMixin):
    def analyze(self, data):
        self.log(f"Analyzing data: {data}")
        # Data analysis logic here
        print(f"Data {data} analyzed.")

# Usage
processor = FileProcessor()
processor.process("data.txt")

analyzer = DataAnalyzer()
analyzer.analyze({"key": "value"})


from datetime import datetime

class TimestampMixin:
    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_timestamp(self):
        self.updated_at = datetime.now()

class Post(TimestampMixin):
    def __init__(self, content):
        super().__init__()
        self.content = content

    def edit_content(self, new_content):
        self.content = new_content
        self.update_timestamp()

# Usage
post = Post("Initial content")
print(f"Created at: {post.created_at}")
print(f"Updated at: {post.updated_at}")

post.edit_content("Updated content")
print(f"Updated at (after edit): {post.updated_at}")


import json

class SerializationMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class User(SerializationMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Product(SerializationMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Usage
user = User("john_doe", "john@example.com")
product = Product("Laptop", 1200)

print(user.to_json())   # {"username": "john_doe", "email": "john@example.com"}
print(product.to_json())  # {"name": "Laptop", "price": 1200}
