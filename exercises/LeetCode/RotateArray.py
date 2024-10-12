class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        n = len(nums)
        # criar nova array para receber o tamanho da nums onde será colocado os valores rotacionados
        rotated = [0] * n

        for i in range(n):
            # a posição nums[i] irá para a nova posição (i+k)%n da nova array 
            # %n garante que a posição ficará restrita ao tamanho de nums
            # i+k desloca o a posição i para direita kx 
            rotated[(i+k)%n] = nums[i]
        
        for i in range(n):
            #looping para que a array rotated vire a nums
            nums[i] = rotated[i]

        