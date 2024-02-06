import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for tc in range(1,T+1):
    N,K = map(int, input().split()) # N: 연잎의 개수, K: 점프 수
    leaf_list = list(map(int, input().split()))
    result = 0

    pre_v = 0 # 이전 점프 거리
    cur_p =0 # 현재 위치

    for _ in range(K):
        next_v = leaf_list[cur_p]
        if next_v > 0 and pre_v <0 : # 직전에 뒤로 점프한 경우
            next_v -= pre_v

            pre_v = leaf_list[cur_p]
            cur_p += next_v  # 개구리 점프
            if cur_p < 0 or cur_p >= N :
                break
            result += leaf_list[cur_p]

    print(f'#{tc} {result}') # 수정!