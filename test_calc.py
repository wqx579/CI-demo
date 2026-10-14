from calc import add
def test_add1():
    assert add(1,2) == 3

# 你可以故意写一个失败用例用来演示阻断合并
# def test_add_fail():
#     assert add(1,2) == 100