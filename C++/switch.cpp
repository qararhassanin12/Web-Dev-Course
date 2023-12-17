#include<iostream>
using namespace std;
int main()
{
	cout<<"\t\t\t\tName    : Nasir Ullah\n";
	cout<<"\t\t\t\tRoll no : 211128\n\n";
	void cal(int, char, int);
	int n1, n2;
	char op;
	cout<<"Enter first number then arithmetic operator and then second number "<<endl;
	cin>>n1>>op>>n2;
	cal(n1, op, n2);
}
void cal(int x, char aop, int y)
{
	switch(aop)
	{
		case '+':
			cout<<x<<" + "<<y<<" = "<<x+y;
			cout<<endl<<"WoW Nice";
			break;
		case '-':
			cout<<x<<" - "<<y<<" = "<<x-y;
			cout<<endl<<"WoW Nice";
			break;
		case '*':
			cout<<x<<" * "<<y<<" = "<<x*y;
			cout<<endl<<"WoW Nice";
			break;
		case '/':
			cout<<x<<" / "<<y<<" = "<<x/y;
			cout<<endl<<"WoW Nice";
			break;
		case '%':
			cout<<x<<" % "<<y<<" = "<<x%y;
			cout<<endl<<"WoW Nice";
			break;
		default:
		cout<<"Invalid input";
	}
}