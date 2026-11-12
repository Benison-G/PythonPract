def assignCookies(children, cookies):
    children.sort()
    cookies.sort()

    child = 0
    cookie = 0

    while child < len(children) and cookie < len(cookies):
        if (children[child] <= cookies[cookie]):
            child = child + 1
        cookie = cookie + 1

    return child

print(assignCookies([1,2,3], [1,1]))