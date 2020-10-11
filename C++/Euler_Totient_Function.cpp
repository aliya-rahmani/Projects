#include<iostream>
using namespace std;
int main()
{
	int t=0;
	std::cin>>t;
	
	while(t--)
	{
		int n=0;
		std::cin>>n;
		int result = n;
		for(int i=2;i*i<=n;i+=1)
		{
			if(n%i==0)
			{
				while(n%i==0)
					n/=i;
				result -= (result/i);
			}
		}
		if(n>1)
			result -= (result/n);
		std::cout<<result;
		
	}
	return 0;
}
