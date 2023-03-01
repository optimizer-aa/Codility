def solution(N):
    # Implement your solution here
    dig=0
    binary =0
    while (N>0):
        dig = int(N%2)
        binary = int((binary*10) + dig)
        N=int(N/2)
    check = str(binary)
    new=check.split("1")
    return len(max(new))
