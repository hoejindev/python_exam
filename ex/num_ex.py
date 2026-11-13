import numpy as np

arr = np.array([[3, 6, 9],
                [2, 4, 8],
                [5, 7, 1]])

# 문제
# 1. arr의 shape과 ndim을 출력하시오.
print('shape :', arr.shape)
print('ndim :', arr.ndim)

# 2. 열 방향 평균을 구하시오.
print('열 방향 평균(axis=0) :', arr.mean(axis=0))

# 3. 행 방향 최댓값을 구하시오.
print('행 방향 최대값(axis=1) :', arr.max(axis=1))

# 4. arr을 전치행렬로 만든 후 shape을 출력하시오.
arr_t = arr.T
print('전치 shape:', arr_t.shape)

# 5. arr을 1차원으로 펼친 뒤 최솟값을 구하시오.
flat = arr.flatten()
print(flat.min())
# 6. arr을 (1, 9) 형태로 reshape 하시오.
reshaped = arr.reshape(1,9)
print('reshape(1,9) :',arr.reshape(-1))