#生成器的使用，以及判断的使用
def odd():
    print('step 1')
    yield (1) 
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o=odd()
while True:
    try:
        x=next(o)
        print('o:',x)
    except StopIteration as e:
        print('Generation return value:',e.value)
        break
 