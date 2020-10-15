public class ArrayRotation {

	public static void main(String[] args) {
		int a[] = {2,5,6,3,8};
		int l=a.length;
		int ar=a[l-1];
		for(int i=l-1;i>0;i--) {
			a[i]=a[i-1];
		}
		a[0]=ar;
		for(int i=0;i<l;i++) {
			System.out.println(a[i]);
		}
	}

}
