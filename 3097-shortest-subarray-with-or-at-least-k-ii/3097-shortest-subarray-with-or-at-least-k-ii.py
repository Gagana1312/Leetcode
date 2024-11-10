class Solution:
    def minimumSubarrayLength(self, A: List[int], k: int) -> int:
        bits_freq = [0 for _ in range(32)]


        def get_or(bits_freq):
            b_or =0
            for bit in range(32):
                if bits_freq[bit]>0:
                    b_or |=(1<<bit)
            return b_or

        def add_to_bits_freq(bits_freq,a):
            for bit in range(32):
                if(a>>bit)&1:
                    bits_freq[bit]+=1
        def remove_from_bits_freq(bits_freq,a):
            for bit in range(32):
                if(a>>bit)&1:
                    bits_freq[bit]-=1

        inf,n = float('inf'), len(A)
        i,best = 0, inf         
        for j in range(n):
            #expand
            add_to_bits_freq(bits_freq,A[j])

            curr_or = get_or(bits_freq)
            #while collapse condition
            while i<=j and curr_or >=k:
                #collapse
                best = min(best, j-i+1)
                remove_from_bits_freq(bits_freq,A[i])
                curr_or = get_or(bits_freq)
                i+=1        

        return best if best != inf else -1