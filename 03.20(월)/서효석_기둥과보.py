def solution(n, build_frame):
    answer = []
    for i in build_frame:
        [c,n-r,a,b] = i
        visited[r][c]=a
        
    for i in range(n+1):
        for j in range(n+1):
            if visited[i][j]!=2
            answer.append([])
        
    
    return answer

def main():
    n=int(input())
    build = input()
    visited=[[2]*(n+1) for _ in range(n+1)]
