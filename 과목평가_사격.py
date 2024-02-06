import sys
sys.stdin = open('algo1_sample_in.txt.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 과녁의 크기
    board = [list(map(int, input().split()))for _ in range(N)]

    result = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(1, N-1):
        for j in range(1, N-1):
            cur_score = 0
            for d in dirs:
                ni, nj = i +d[0], j+d[1]
                if 0<=ni<N and 0<=nj<N:
                    cur_score += board[ni][nj]
            cur_score -= board[i][j]
            cur_score = 0 if cur_score < 0 else cur_score
            cur_score = cur_score*2 if cur_score%2==0 else cur_score


            if cur_score > result




