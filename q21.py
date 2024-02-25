def average(array):
    # your code goes here
    st = set(array)
    sumof = sum(st)
    length = len(st)
    avg = sumof/length

    return avg

    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)



