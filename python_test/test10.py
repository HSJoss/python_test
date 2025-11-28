import gc
import torch

a = torch.randn(3, 3)  # 텐서 a 생성
print(gc.get_count())  # 가비지 컬렉션 상태 확인

b = a  # b는 a를 참조
del a  # a를 삭제하지만, b가 여전히 텐서를 참조
print(gc.get_count())  # 여전히 객체는 메모리에 남아 있음

del b  # b를 삭제
print(gc.get_count())  # 이제 객체는 더 이상 참조되지 않아서 메모리에서 해제됨
gc.collect()  # 강제로 가비지 컬렉션 실행
