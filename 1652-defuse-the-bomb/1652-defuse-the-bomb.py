class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length_of_code = len(code)
        decrypted_code = [0] * length_of_code
        if k == 0:
            return decrypted_code
        prefix_sum = list(accumulate(code + code, initial=0))
        for i in range(length_of_code):
            if k > 0:
                decrypted_code[i] = prefix_sum[i + k + 1] - prefix_sum[i + 1]
            else:
                decrypted_code[i] = prefix_sum[i + length_of_code] - prefix_sum[i + k + length_of_code]
        return decrypted_code
        