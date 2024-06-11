class Solution {
    public int fib(int n) {
        int a= 0;
        int b= 1;
        int c= 1;
        int res =0;
        if(n==0){
            return res;
        }
        if(n==1||n==2){
            res=1;
        }
        for(int i=2;i<n;i++){
            a=b;
            b=c;
            c = a+b;
            res = c;
        }
        return res;
    }
}