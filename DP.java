import java.util.*;
public class DP {
public static Scanner scn = new Scanner (System.in);
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//totalWaysToChangeCoins();
		minCostPath();
	}
	public static void totalWaysToChangeCoins() {
		 int coins[] = {2,5,3,6};
		 int total = 10;
		 int n = coins.length;
		 int[][] dp = new int[coins.length+1][total+1];
		 System.out.println(totalWaysToChangeCoins(coins.length-1,total, dp, coins));
		 return;
	}
	public static int totalWaysToChangeCoins(int idx,int sum, int[][]dp, int[] coins) {
	//	System.out.println(sum);
		if(sum==0)return 1;
		if(sum<0 || idx<0)return 0;
		if(dp[idx][sum]!=0)return dp[idx][sum];

		dp[idx][sum]=(totalWaysToChangeCoins(idx-1,sum, dp, coins)+
				totalWaysToChangeCoins(idx,sum-coins[idx], dp, coins));
		return dp[idx][sum];
	}
	public static void minCostPath() {
		int[][]path = {{1,3,5,8},{4,2,1,7},{4,3,2,3}};
		int n = path.length;
		int m = path[0].length;
		int[][] dp = new int[n+1][m+1];

		for(int i = 0;i<=m;i++)dp[0][i] = 1000;
		for(int i = 0;i<=n;i++)dp[i][0] = 1000;

		for(int i = 1;i<=n;i++) {
			for(int j = 1;j<=m;j++) {
				int val = Math.min(dp[i-1][j],dp[i][j-1])==1000?0:Math.min(dp[i-1][j],dp[i][j-1]);
				dp[i][j] = path[i-1][j-1]+val;
			}
		}
		for(int i = 0;i<=n;i++) {
			for(int j = 0;j<=m;j++) {
				System.out.print(dp[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println(dp[n][m]);
	}
}
