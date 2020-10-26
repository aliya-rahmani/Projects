import sys
def findTheMaxProfit(numOfGivenDays, givenSharePrices):
    day = numOfGivenDays-1
    nextHighestSharePrice = 0
    maxProfit = 0
    while day>=0:
        nextHighestSharePrice = max(nextHighestSharePrice,givenSharePrices[day])
        maxProfit = max(maxProfit,nextHighestSharePrice-givenSharePrices[day])
        day-=1
    return maxProfit


def main():
    line = input().split()
    numOfGivenDays = int(line[0])
    givenSharePrices = list(map(int, line[1:]))
    answer = findTheMaxProfit(numOfGivenDays, givenSharePrices)
    print(answer)

if __name__ == '__main__':
    main()
