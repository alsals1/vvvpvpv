def f(pat, txt, M, N):
    for i in range(N-M+1): # txt에서 비교시작하는 위치 0..... N-M (5-3)=(2)
        for j in range(M):
            if txt[i+j] != pat[j]:  # 불일치면 다음 시작 위치로 간다.
                break
        else:           # 패턴 매칭에 성공하면, # for-else문. for에서 다 돌고 break 되지 않으면
            return 1


T = int(input())
for tc in range(1,T+1):
    pat = input()
    txt = input()
    M = len(pat)
    N = len(txt)

    ans = f(pat, txt, M, N)
    print(f'#{tc} {ans}')
### 이 글은 수정되었습니다.