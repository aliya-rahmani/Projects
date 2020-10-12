import java.io.*;
import java.util.*;

public class Permutation {
	
	public static void main(String[] args) {
		FastScanner sc=new FastScanner();
        String s = sc.next();
        System.out.println("All the permutation are : ");
        //List<String> ans = gen(s);
        List<String> result = gen_with_dup(s);
        //for(String str: ans){
           // System.out.println(str);
        //}
        for (String str : result) {
            System.out.println(str);
        }
        System.out.println("*done*");
    }
    
    public static List<String> gen(String s){
        List<String> ans = new ArrayList<>();
        if(s==null)
            return null;
        if(s.length()==0){
            ans.add("");
            return ans;
        }
        char c = s.charAt(0);
        List<String> sub = gen(s.substring(1));
        for(String word : sub) {
            for(int i =0; i<=word.length(); i++){
                ans.add(insert(word,i,c));
            }
        }

        return ans;
    }

    public static String insert(String s, int idx, char c){
        return s.substring(0,idx)+c+s.substring(idx);
    }

    public static List<String> gen_with_dup(String s) {
        List<String> ans = new ArrayList<>();
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray())
            map.put(c, map.getOrDefault(c, 0) + 1);

        endgame(map,"",s.length(),ans);
        return ans;
    }

    public static void endgame(HashMap<Character, Integer> map, String prefix, int remaining, List<String> ans){
        if(remaining == 0){
            ans.add(prefix);
            return ;
        }

        for(char c : map.keySet()){
            int count = map.get(c);
            if(count>0){
                map.put(c,count-1);
                endgame(map,prefix+c,remaining-1,ans);
                map.put(c,count);
            }
        }
    }

	static final Random random = new Random();
	
	static void sort(int[] a) {
		int n = a.length;
		for(int i =0; i<n; i++) {
			int val = random.nextInt(n);
			int cur = a[i];
			a[i] = a[val];
			a[val] = cur;
		}
		Arrays.sort(a);
	}
	
	static void sortl(long[] a) {
		int n = a.length;
		for(int i =0; i<n; i++) {
			int val = random.nextInt(n);
			long cur = a[i];
			a[i] = a[val];
			a[val] = cur;
		}
		Arrays.sort(a);
	}
	
	static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
		String next() {
			while (st == null  || !st.hasMoreTokens()) {
				try {
					st=new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}
		String nextLine() { 
            String str = ""; 
            try
            { 
                str = br.readLine(); 
            } 
            catch (IOException e) 
            { 
                e.printStackTrace(); 
            } 
            return str; 
		} 
		int nextInt() {
			return Integer.parseInt(next());
		}
		int[] readArray(int n) {
			int[] a=new int[n];
			for (int i=0; i<n; i++) a[i]=nextInt();
			return a;
		}
		long nextLong() {
			return Long.parseLong(next());
		}
		double nextDouble() { 
            return Double.parseDouble(next()); 
        } 
	}

}
