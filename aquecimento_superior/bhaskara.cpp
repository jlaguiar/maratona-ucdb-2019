#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
   double A, B, C, Delta, R1, R2;

   cin>>A;
   cin>>B;
   cin>>C;

   Delta = pow(B,2) - (4 * A * C);

   R1 = (-B + sqrt (Delta))/(2*A);
   R2 = (-B - sqrt (Delta))/(2*A);

   if (A == 0 || Delta<0){
      cout<<"Impossivel calcular\n";
   }

   else {
   std::cout << std::fixed;
   std::cout << std::setprecision(5);
   cout<<"R1 = "<<R1<<"\n";
   cout<<"R2 = "<<R2<<"\n";
   }

   return 0;
}

