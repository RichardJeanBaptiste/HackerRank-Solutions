#
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up
# score. You are given scores. Store them in a list and find the score of the runner-up.
#  
#  Sample Input
#
#  5
#  2 3 6 6 5
#  
#  Sample Output
#  5 
# #


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    max = ""
    runnerUp = ""
    
    for x in arr:
        if max == "":
            max = x
        elif runnerUp == "" and x != max:
            runnerUp = x
        
        if x > max:
            runnerUp = max
            max = x
        elif x > runnerUp and x != max:
            runnerUp = x
        
        
    print runnerUp