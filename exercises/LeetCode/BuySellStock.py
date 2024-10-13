class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # definir buy como o primeiro elemento
        buy = prices[0]
        profit = 0

        #percorrer i a partir do segundo elemento 
        for i in range(1, len(prices)):
            # se o a posição i for menor q buy, buy assume a posição i
            if prices[i] < buy:
                buy = prices[i]
            #senão, ver profit assumir novo valor de i - buy
            elif prices[i] - buy > profit:
                #ao assumir o max valor, ficará nesse mesmo valor até o fim do looping
                profit = prices[i] - buy
        return profit 

