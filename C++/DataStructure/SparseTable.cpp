class RMQ
{
	int _A[OO],spt[OO][10];//the 10 is log2 of N
public:

	RMQ(int n,int A[]){

		for (int i = 0; i < n; ++i)
				_A[i]=A[i],spt[i][0]=i;
		for (int j = 1; (1<<j) <= n; j++)
		{
			for (int i = 0; i+(1<<j)-1 < n; ++i)
				if (_A[spt[i][j-1]]<_A[spt[i+(1<<(j-1))][j-1]])
						spt[i][j]=spt[i][j-1];

				else	spt[i][j]=spt[i+(1<<(j-1))][j-1];
		}
	}
	
	int query(int i,int j){ // returns the idx
		int k=(int)floor(log((double)j-i+1)/log(2.0));
		if(_A[spt[i][k]]<=_A[spt[j-(1<<k)+1][k]])
			return spt[i][k];
		else return spt[j-(1<<k)+1][k];
	}
};
