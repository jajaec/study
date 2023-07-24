import time
start = time.time()

print('work something')
time.sleep(1)

end = time.time()

# f-string 포매팅
print(f'time = {(end - start):.3f}s')

# 파이썬 데코레이터 설정
# 참고 사이트: https://hello-bryan.tistory.com/214
def time_trace(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        rt = func(*args, **kwargs)
        print(f'### {func.__name__}({args}) time : {time.time() - st:.2f}ms')
        return rt
    return wrapper

@time_trace
def work1():
    print('작업 1 시작')
    time.sleep(0.5)
    print('작업 1 끝')

@time_trace
def work2():
    print('작업 2 시작')
    time.sleep(1.2)
    print('작업 2 끝')

if __name__ == '__main__':
    work1()
    work2()