class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        for i in range(n - 1):
            if number[i] == digit and number[i] < number[i+1]:
                return number[:i] + number[i+1:]
        # no beneficial removal found, remove the last occurrence
        i = number.rfind(digit)
        return number[:i] + number[i+1:]