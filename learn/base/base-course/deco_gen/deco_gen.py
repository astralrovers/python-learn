def coroutine(func):
    print('start deco')
    def start(*args,**kwargs):
        print('start gen')
        cr = func(*args,**kwargs)
        next(cr)
        return cr
    return start

if __name__ == '__main__':
    @coroutine
    def grep(pattern):
        print("Looking for %s" % pattern)
        while True:
            line = (yield)
            if pattern in line:
                print(line),

    g = grep("python") #grep(start) 是一个函数,它生产并启动了一个生成器
    # Notice how you don't need a next() call here
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
