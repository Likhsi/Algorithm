# 숫자가 쓰인 카드들이 N X M 형태로 놓여있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

n, m = map(int, input().split())

result = 0

for i in range(n):
	data = list(map(int, input().split()))
	# 가장 작은 수 찾기 min() 함수
	min_value = min(data)
	# 가장 작은 수들 중에서 가장 작은 큰 수 찾기
	result = max(result, min_value) # result 및 min_value에서 가장 큰 수를 찾는다. for문이 n번 반복하는데 반복 할때마다 가장 큰수를 확인한다.

print(result)
