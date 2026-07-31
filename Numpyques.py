import numpy as np

#Q1
arr = np.array([[-15,45,120],[0,-99,85],[105,50,-1]])
arr[arr < 0] = 0
arr[arr > 100] = 100
print("Q1")
print(arr)

#Q2
arr = np.array([1,2,3,4,5,6,7,8,9,10])
k = 3
print("Q2")
print(np.convolve(arr, np.ones(k)/k, "valid"))

#Q3
points = np.array([[1,2],[4,6],[8,1],[2,3]])
query = np.array([3,3])
d = np.linalg.norm(points-query, axis=1)
print("Q3")
print(points[np.argmin(d)])

#Q4
matrix = np.array([[0,0,1,0],[0,1,1,0],[0,0,0,0],[1,0,0,1]])
ans = np.argmax(matrix, axis=1)
ans[np.sum(matrix, axis=1)==0] = -1
print("Q4")
print(ans)

#Q5
X = np.array([[10,20,30],[5,5,5],[2,4,6]], dtype=float)
mean = X.mean(axis=1, keepdims=True)
std = X.std(axis=1, keepdims=True)
std[std==0] = 1
print("Q5")
print((X-mean)/std)

#Q6
n = 5
board = np.zeros((n,n), dtype=int)
board[::2,1::2] = 1
board[1::2,::2] = 1
print("Q6")
print(board)

#Q7
arr = np.array([1,3,7,1,2,6,3,4,1])
print("Q7")
print(arr[1:-1][(arr[1:-1]>arr[:-2]) & (arr[1:-1]>arr[2:])])

#Q8
matrix = np.array([[1,2],[3,4],[1,2],[5,6],[3,4]])
_, index = np.unique(matrix, axis=0, return_index=True)
print("Q8")
print(matrix[np.sort(index)])

#Q9
points = np.array([1,4,6], dtype=float)
ans = np.abs(points[:,None]-points)
np.fill_diagonal(ans, -1)
print("Q9")
print(ans)

#Q10
matrix = np.array([[10,50,30,20],[90,10,40,80],[5,25,15,35]])
k = 2
ans = np.sort(matrix, axis=1)
print("Q10")
print(ans[:,-k:][:,::-1])
