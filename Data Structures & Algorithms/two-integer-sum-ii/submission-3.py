class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        offsetX = 0
        offsetY = len(numbers) - 1

        x = numbers[offsetX]
        y = numbers[offsetY]

        

        while offsetX < offsetY:
            x = numbers[offsetX]
            y = numbers[offsetY]

            if x + y > target:
                offsetY -= 1

            elif x + y < target:
                offsetX += 1

            else:
                return [offsetX + 1, offsetY + 1]
            