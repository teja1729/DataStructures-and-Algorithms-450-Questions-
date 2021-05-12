'''Quesiton :You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different
 day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example Input : [7,1,5,3,6,4] expected output : 5 (which is 6-1)
constraints: 1 <= prices.length <= 10^5,0 <= prices[i] <= 10^4 so max here is 10^9
So expected time complexity is O(n) or lower
Algorithm:Timecomplexity :O(n),logic- we need to find minimum value and right max for that min value
step1: low = 9999(maximum value that array shouldn't contain),maxprofit = 0
step2: traversing the array and if price <low then low = price
step3: else find profit(price - low) and if its > maxprofit then maxprofit = price-low
step4: return the maxprofit
'''
def maxProfit(prices):
	low = 9999
	maxprofit = 0
	for price in prices:#O(n)
		if price < low:
			low = price
		else:
			maxprofit = max(price - low , maxprofit)
	return maxprofit
if __name__ == '__main__':
	prices = [7,1,5,3,6,4]
	print(maxProfit(prices))
	#output: 5