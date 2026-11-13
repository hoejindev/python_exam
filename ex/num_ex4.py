import numpy as np

arr = np.array([[12, 35, 48, 20],
                [55, 18, 72, 30],
                [25, 60, 15, 90]])

# 1. 배열에서 30 이상인 값만 출력해주세요.

print(arr[arr >= 30])


# 2. 배열에서 50 이상인 값은 1, 50 미만인 값은 0으로 변경한 배열을 만들어주세요.

print(np.where(arr >=50, 1, 0))

# 3. 배열에서 40 이상인 원소가 총 몇 개인지 출력해주세요.
print(np.count_nonzero(arr >= 40))

# 4. 각 행에서 최댓값의 인덱스를 출력해주세요.
print(arr.argmax(axis=1))

# 5. 배열 전체에서 최댓값의 위치를 (행, 열) 형태로 출력해주세요.
index = arr.argmax()
print(index)

position = np.unravel_index(index, arr.shape)
print(position)
print(arr[position])


# 6. 배열에서 20 미만인 값은 20으로, 70 초과인 값은 70으로 변경해주세요.
result = np.clip(arr, 20, 70)
print(result)