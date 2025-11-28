"""def A(a=0):
    result = int(a + 3)
    return result

def B():
    return 5

# eval 사용
k = "B()"
c = A(a=eval(k))  # OK

# exec 사용하려면 이렇게 해야 해요:
exec("temp = B()")  # B() 실행해서 temp라는 변수에 저장
c = A(a=temp)

print(c)  # 출력: 8"""

"""def A(**kwargs):
    # 키 'a'의 값을 평가해서 숫자로 변환하고 +3
    value = eval(kwargs['a'])  # "B()" → 실행해서 5가 됨
    result = int(value + 3)
    return result

def B():
    return 5

k = {'a': "B()"}  # 문자열 형태로 저장

c = A(**k)  # 딕셔너리를 키워드 인자로 펼쳐서 전달

print(c)  # 출력: 8"""


"""#eval("__import__('os').system('rm -rf /')")  # 이건 진짜 위험해요...!

def safe_eval(expr, allowed_funcs=None):
    
    #안전한 eval: 지정한 함수들만 사용 가능
    
    if allowed_funcs is None:
        allowed_funcs = {}

    return eval(expr, {"__builtins__": None}, allowed_funcs)

def B():
    return 5

k = {'a': "B()"}

# 안전한 함수 목록을 딕셔너리로 정의
safe_functions = {
    'B': B
}

result = safe_eval(k['a'], allowed_funcs=safe_functions)

print(result)  # 출력: 5


def B():
    return 5

def safe_eval(expr, allowed_funcs=None):
    if allowed_funcs is None:
        allowed_funcs = {}
    return eval(expr, {"__builtins__": None}, allowed_funcs)

def A(**kwargs):
    value = safe_eval(kwargs['a'], allowed_funcs={'B': B})
    return int(value + 3)

k = {'a': "B()"}

c = A(**k)
print(c)  # 출력: 8
"""

"""
방법	보안 수준	설명
eval()	❌ 위험	아무 코드나 실행 가능
safe_eval()	✅ 안전	허용한 함수만 사용 가능
ast.literal_eval()	✅ 매우 안전	기본 자료형만 평가 (함수 호출은 불가)
"""
"""
def A(**kwargs):
    result = int(kwargs['a'] + 3)
    return result

def B():
    return 5

# 바깥에서 eval 실행
k = {'a': eval("B()")}  # "B()"를 평가 → 5가 들어감

c = A(**k)

print(c)  # 출력: 8
"""
"""def B():
    return 5

def A(**kwargs):
    result = int(kwargs['a'] + 3)
    return result

def safe_eval(expr, allowed_funcs=None):
    if allowed_funcs is None:
        allowed_funcs = {}
    return eval(expr, {"__builtins__": None}, allowed_funcs)

# 미리 평가하고 넘김
k = {'a': safe_eval("B()", allowed_funcs={'B': B})}

c = A(**k)
print(c)  # 출력: 8
"""

def A(**kwargs):
    def B():
        return 5
    
    # B를 사용하여 표현식 반환
    return kwargs['a']  # 표현식이 들어있는 값만 반환

# k 딕셔너리에서 eval을 호출할 때
k = {'a': "B()"}  # 'a'에는 B()라는 문자열이 들어있음

# A를 호출하여 표현식 반환
expression = A(**k)  # 'B()'라는 문자열이 반환됨

# 이제 외부에서 eval을 처리
result = eval(expression, {"__builtins__": None}, {'B': lambda: 11})  # B() 실행, 5 반환

# 결과에 3을 더함
c = result + 3
print(c)  # 출력: 8
