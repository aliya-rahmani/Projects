#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	vector<float> v[4];	
	cout<<"enter x1,x2,bias,tgt\n";

	cout<<"******************************************************************************\n";
	cout<<"x1\tx2\tbias\ttarget\tyin\tw1\tw2\tb\terror\n";

	float error[4];
	int test=3;
	for(int i=0;i<4;i++){
		float x1,x2,bias,t;
		cin>>x1>>x2>>bias>>t;
		v[i].push_back(x1);
		v[i].push_back(x2);
		v[i].push_back(bias);
		v[i].push_back(t);
	}
	float w[3],learningrate=.001;//w[2]=b
	float tErro=1.4;
	w[0]=w[1]=w[2]=.1;
		int k=1;
while(k++){
	cout<<"iteration->>"<<k-1<<"\n\n";
	
		float yin;

	for(int i=0;i<4;i++){
		float yin=w[2];
		for(int j=0;j<v[i].size()-2;j++){
			yin+=w[j]*v[i][j];
		}
		for(int j=0;j<3;j++){
			w[j]+=learningrate*(v[i][3]-yin)*v[i][j];
		}
		error[i]=(v[i][3]-yin)*(v[i][3]-yin);
	cout<<v[i][0]<<"\t"<<v[i][1]<<"\t"<<v[i][2]<<"\t"<<v[i][3]<<"\t"<<yin<<"\t"<<w[0]<<"\t"<<w[1]<<"\t"<<w[2]<<"\t"<<error[i]<<"\n";

	}
	float errorsum=0;
	for(int j=0;j<4;j++){
		errorsum+=error[j];
	}
	cout<<"errorsum"<<errorsum<<"\n";
	cout<<"threshold"<<tErro<<"\n";
	
	if(errorsum<tErro){
		break;
	}
	}
}