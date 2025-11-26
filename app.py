def greet(name, language="en"):
    if language == "en":
        print(f"Hello, {name}! Welcome to our amazing app.")
        print("This is version 4 of our app.")
        print(f"Hello, {name}! This is a GitHub change.")
        print("Have a nice day!")
    elif language == "vi":
        print(f"Xin chào, {name}!")
        print("Đây là phiên bản 2 của ứng dụng.")
        print("Chúc bạn một ngày tốt lành!")
    else:
        print(f"Hello, {name} (language not supported).")

if __name__ == "__main__":
    greet("Phuc", "vi")
