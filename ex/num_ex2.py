import numpy as np

arr = np.array([[1.5, 2.5, 3.5, 4.5],
                [5.5, 6.5, 7.5, 8.5]])

# 문제
# 1. arr의 dtype과 itemsize를 출력하시오.
print('arr.dtype : ', arr.dtype)
print('arr itemsize : ', arr.itemsize)


# 2. axis=0 기준 합을 구하시오.
print('열 방향 합계(axis=0) :', arr.sum(axis=0))

# 3. axis=1 기준 평균을 구하시오.
print('행 방향 평균(axis=1) :', arr.mean(axis=1))

# 4. arr을 (4,2) 형태로 reshape 하시오.
re = arr.reshape(4,2)
print('arr (4,2) reshape : ', re)

# 5. reshape한 배열을 전치한 결과의 shape을 구하시오.
print('reshape 한 배열 전치한 결과 shape :', re.T.shape)

# 6. arr.flatten()으로 만든 배열의 shape은 무엇인가?
flat = arr.flatten()
print('arr.flatten()으로 만든 배열의 shape :',flat.shape)