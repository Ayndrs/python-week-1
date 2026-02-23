from wordcount.exmath import add, sub

def test_add():
    assert add(1, 1) == 2

def test_sub():
    assert sub(2, 1) == 1

if __name__ == "__main__":
    print("This is exmath")