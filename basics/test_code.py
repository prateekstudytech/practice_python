def findLastOccurence(A, B):
        # code here
        substring_len = len(B)
        for i in range(len(A)-3, -1, -1):
            print("i : ", i)
            print(A[i:i+substring_len])
            if A[i:i+substring_len] == B:
                return i
        return -1

A = "abcdefghijklghifghsd"
B = "ghi"
findLastOccurence(A, B)
