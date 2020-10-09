#include<iostream>
#include<cmath>
using namespace std;


int main()
{
int kode, kodeconv;
double nil;


cout << "====================================" << endl;
cout << "             KONVERSI SUHU          " << endl;
cout << "       www.ssngeblog.blogspot.com   " << endl;
cout << " celcius, Fahrenheit, Reamur, Kelvin" << endl;
cout << "====================================" << endl;
cout<<"Masukkan nilai awal = ";cin>>nil;
cout<< "Masukkan suhu dalam: "<<endl;
cout<<"1. Celcius"<<endl;
cout<<"2. Fahrenheit"<<endl;
cout<<"3. Reamur"<<endl;
cout<<"4. Kelvin"<<endl;
cout<<"kode = ";cin>>kode;
cout<< "Dikonversikan ke dalam: "<<endl;
cout<<"1. Celcius"<<endl;
cout<<"2. Fahrenheit"<<endl;
cout<<"3. Reamur"<<endl;
cout<<"4. Kelvin"<<endl;
cout<<"kode = ";cin>>kodeconv;

if (kode==1 and kodeconv ==1)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Celcius : " <<nil<<endl;
}
else if (kode == 1 and kodeconv == 2)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " fahrenheit : " <<(nil*1.8+32)<<endl;

}
else if (kode == 1 and kodeconv == 3)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Reamur  : " <<(nil*0.8)<<endl;

}
else if (kode == 1 and kodeconv == 4)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Kelvin : " <<(nil+ 273.15)<<endl;

}
else if (kode==2 and kodeconv ==1)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Celcius : " <<((nil+459.67)/1.8)<<endl;
}
else if (kode == 2 and kodeconv == 2)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " fahrenheit : " <<nil<<endl;

}
else if (kode == 2 and kodeconv == 3)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Reamur  : " <<((nil-32)/2.25)<<endl;

}
else if (kode == 2 and kodeconv == 4)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Kelvin : " <<((nil-32)/1.8)<<endl;

}
else if (kode == 3 and kodeconv ==1)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Celcius : " <<(nil/0.8)<<endl;
}
else if (kode == 3 and kodeconv == 2)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " fahrenheit : " <<(nil*2.25+32)<<endl;

}
else if (kode == 3 and kodeconv == 3)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Reamur  : " <<nil<<endl;

}
else if (kode == 3 and kodeconv == 4)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Kelvin : " <<(nil/0.8+273.15)<<endl;

}
else if (kode == 4 and kodeconv ==1)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Celcius : " <<(nil-273.15)<<endl;
}
else if (kode == 4 and kodeconv == 2)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " fahrenheit : " <<(nil*1.8-459.67)<<endl;

}
else if (kode == 4 and kodeconv == 3)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Reamur  : " <<((nil-273.15)*0.8)<<endl;

}
else if (kode == 4 and kodeconv == 4)
{
cout<<endl;
cout << "=============================" << endl;
cout << "HASIL KONVERSI SUHU" << endl;
cout << "=============================" << endl;
cout << " Kelvin : " <<nil<<endl;

}
else
{
    cout<<"Kode yang Anda masukkan salah";
}

}
