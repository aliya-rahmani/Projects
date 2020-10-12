class lcs{
    int LCS(String s1,String s2,int m,int n){
        int L[][] = new int[m+1][n+1];
        for(int i=1;i<m+1;i++){
            for(int j=1;j<n+1;j++){
                if(s2.charAt(j-1)==s1.charAt(i-1))
                    L[i][j]=L[i-1][j-1]+1;
                else
                    L[i][j] = Math.max(L[i-1][j],L[i][j-1]);
            }
        }
        return L[m][n];
    }
    public static void main(String[] args) {
        lcs obj = new lcs();
        String s1 = "asdsdqd";
        String s2 = "axsasdsd";
        System.out.println(obj.LCS(s1,s2,s1.length(),s2.length()));
    }
}