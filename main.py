# Factorial
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Fibonacci
def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Structure-to-Dictionary Conversion
class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "branch": self.branch
        }

if __name__ == "__main__":
    print("Factorial 5:", factorial(5))
    print("Fibonacci 7:", fibonacci(7))
    s = Student("Kismat", "101", "CSE")
    print("Converted Dictionary:", s.to_dict())
