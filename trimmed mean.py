# method 1
# def solve(N,score):

#     limit = 5*N
       
#     while N:
        
#         score.remove(max(score))
#         score.remove(min(score))
#         N -=1

#     print(sum(score)/len(score))

# method 2

def solve(N,score):
        
        score.sort()
        avg = sum(score[1*N:-1*N])/(len(score)-(2*N))
      

        print(avg)

if __name__ == "__main__":
    N = int(input())
    
    score = list(map(int,input().split()))[:5*N]
    solve(N,score)