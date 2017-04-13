/***************************************************************************
Name: Gilbert Edwards
Date: 12/7/16
Lab: Final
SUMMARY: Displays the states from the users input
**************************************************************************/
#include <iostream>
#include<string>
#include <iomanip>
#include<fstream>
#include <vector>
#include <time.h>
using namespace std;

/****Output file information****/
ofstream ofs("Edwards_labFinal.txt");
//string head = "Gilbert Edwards, 12/7/16, CIS-2542-001, Lab Final";
//string foot = "Summary:Displays the states from the users input.";
//string endOF = "EOF MESSAGE, Gilbert Edwards, 12/7/16, CIS-2542-001, Lab Final";

string name1 = " __               __                 ";
string name2 = "/ _ .||_  _ _|_  |_  _|    _  _ _| _ ";
string name3 = "(__)|||_)(-| |_  |__(_|(()(_|| (_|_) ";
string course1 = " __  __     __   __      __       __   __    ";
string course2 = "/  |(_  __   _) |_  |__|  _) __  /  ) /  ) /|";
string course3 = "(__|__)     /__ __)    | /__    (__/ (__/   |";

string date1 = "   __    ___       __ "; 
string date2 = "/|  _) /   / / /| /__ ";
string date3 = " | /__/   / /   | \__)";

string project1 ="__            ";
string project2 ="|_  o __  _  |";
string project3 ="|   | | |(_| |";

string EOF1 =" __ __  __       __ __ __     __  __";
string EOF2 ="|_ /  )|_   |\/||_ (_ (_  /) / _ |_ ";
string EOF3 ="|__(__/|    |  ||____)__)/--\(__)|__";

string summary1 =" __                   __            __        ";
string summary2 ="(_     _  _  _  _    |__)| _    _  (_ | _ |_ _";
string summary3 ="__)|_|||||||(_|| \/  |   |(_|\/_)  __)|(_)|__)";

const int pageWidth = 82;
const int consoleWidth = 79;
int lineRemainder;
string bar = "|";
string dashline = "|--------------------------------------------------------------------------------|";



double probability = .3;
int wins = 0;
int loses = 0;

double wallet=0.00;
double maxWallet=10000.00;

//three 7’s, diamonds, cherry, 3 bags of money, lightening, clover(wild card)


string seven[] = {  
	"_________",
	"| _____ |",
	"|/__   /|",
	"|  /  / |",
	"| /  /  |",
	"|/__/   |",
	"|_______|"};

string diamond[] ={

	"_________",
	"| _____ |",
	"|/\   /\|",
	"|\/' '\/|",
	"| \   / |",
	"|  \./  |",
	"|___V___|"};

string cherry[]={
	"_________",
	"|       |",
	"| |\    |",
	"| \|_\_ |",
	"|  (_)_)|",
	"|    (_)|",
	"|_______|"};

string bagOfMoney[]={
	"_________",
	"|       |",
	"|    )  |",
	"| .-'-. |",
	"|(     )|",
	"| `-=-' |",
	"|_______|"};
string lighting[]={
	"_________",
	"|  \ \  |",
	"|   \_\ |",
	"|    \\ |",
	"|    \\ |",
	"|     \ |",
	"|_______|"};

string clover[]={
	"_________",
	"| .. .. |",
	"| ( | ) |",
	"| .-|-. |",
	"|(_ |._)|",
	"| '-|-' |",
	"|___|___|"};



void format(string sentence)
{
	lineRemainder = pageWidth - 1 - sentence.length();
	ofs << bar << sentence << setw(lineRemainder) << bar << endl;
	cout<<bar<<sentence<<setw(lineRemainder) << bar << endl;
}
/*Standard Header.*/
void hdr()
{
	ofs << dashline << endl;
	cout<<dashline << endl; 
	format(head);
	ofs << dashline << endl;
	cout<<dashline << endl; 
}
/****************
prints the footer
****************/
void ftr()
{
	ofs << dashline << endl;
	cout<<dashline << endl; 
	format(foot);

}

/****************
prints the End of File message
****************/
void eof()
{
	ofs << dashline << endl;
	cout<<dashline << endl; 
	format(endOF);
	ofs << dashline << endl;
	cout<<dashline << endl; 
}


void manageFunds()
{
	double addFund;
	cout<<"You currently have $"<< wallet<<endl;
	cout<<"The maximum wallet size is "<< maxWallet<<endl;
	cout<<"Please enter the amount you would like to add. ";
	cout<<"Between 0-"<<maxWallet - wallet<<endl;
	cin>>addFund;

	while (!((addFund >=0.00) && (addFund <=(maxWallet - wallet))))
	{
		cout<<"invalid entry, please enter a value between 0 and"<<maxWallet - wallet<<endl;
		cin>>addFund;

	}
	if((addFund >=0.00) && (addFund <=(maxWallet - wallet)))
	{
		wallet = wallet+addFund;
	}

	cout << "Your funds have been added. "<<endl;
	cout<<"Your current balance is "<< wallet<< endl;
}

void game()
{
	int field[3][3];

	int pattern;
	int shape;
	srand (time(NULL));
	bool winner;

	if (double(wins)/double(loses) <= probability)
	{
		winner = true;
	}
	else
	{
		winner = false;
	}
	/*
	//pattern = rand() % (10- probability)+1;
	for(int a =0; a<10;a++)
	{
	pattern = rand() % (10- probability)+1;
	cout<< pattern<<endl;
	}
	*/

	for(int a =0; a<3;a++)
	{
		for(int b =0; b<3;b++)
		{
			field[a][b]= rand() %3+1;

		}
	}


}

void body()
{
	srand (time(NULL));
	int choice = 0;
	string response;
	while (choice != 4)
	{
		/*********
		print menu
		*******/
		cout<<"\nMenu \n";
		cout<< "1. Display the rules \n";
		cout<<"2. Wallet- how much starting out money or add \n";
		cout<<"3. Play the game \n";
		cout<<"4. Quit \n";

		game();

		cin >> choice;
		//if (isdigit(choice))
		//{
		system("CLS");
		switch (choice){

		case 1:
			cout<<"one line pays what you bet, ";
			cout<<"three lines you win double, ";
			cout<<"five lines, you win triple."<<endl;
			cout<<"There is a minimum bet of 10, and a maximum bet of "<< maxWallet<<endl;
			cout<<"Any funds exceeding "<< maxWallet<<" are automatically paid out."<<endl;
			break;
		case 2:
			cout<<"Your current wallet balance is "<<wallet<<endl;
			cout<<"Would you like to add additional funds?"<<endl;
			cout<<"Please enter Y to add funds, or enter any other key to return to the main menu"<<endl;
			cin>> response;
			if (response =="Y" || response== "y")
			{manageFunds();}
			break;

		case 3:
			cout<<"You selected to play the game"<<endl;
			break;

		case 4:

			cout<<"Goodbye cruel world!"<<endl;
			break;

		default:
			cout<<"Still Invalid choice, please choose an integer number 1-4 ";
			break;
		}
		//}
		//else {cout<<"outerInvalid choice, please choose an integer number 1-4 ";}
	}
}



int main() {
	hdr();
	//system("pause");
	//system("CLS");
	body();
	//system("CLS");
	ftr();
	eof();
	system("pause");
	return 0;
}