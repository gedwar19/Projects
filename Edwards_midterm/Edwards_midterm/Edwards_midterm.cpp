/***************************************************************************
Name: GIlbert Edwards
Date: 10/11/16
Lab: Midterm
SUMMARY: This code simulates picking lotto ticket.Results are displayed in txt file
**************************************************************************/
#include <iostream>
#include<string>
#include <iomanip>
#include<fstream>
#include <vector>
#include <time.h>
using namespace std;

/****Output file information****/
ofstream ofs("Edwards_lab16.txt");
string head = "Gilbert Edwards, CIS-2542-001, 10/18/16 , Midterm";
string name1 = " __               __                 ";
string name2 = "/ _ .||_  _ _|_  |_  _|    _  _ _| _ ";
string name3 = "(__)|||_)(-| |_  |__(_|(()(_|| (_|_) ";
string course1 = " __  __     __   __      __       __   __    ";
string course2 = "/  |(_  __   _) |_  |__|  _) __  /  ) /  ) /|";
string course3 = "(__|__)     /__ __)    | /__    (__/ (__/   |";
string date1 = "     __        __        __ ";
string date2 = " /| /  ) / /| (__) / /| /__ ";
string date3 = "  | (__//   | (__)/   | (__)";
string project1 = "|)/|. _||_ _ _ _ ";
string project2 = "|  ||(_||_(-| |||";
string EOF1 =" __ __  __       __ __ __     __  __";
string EOF2 ="|_ /  )|_   |\/||_ (_ (_  /) / _ |_ ";
string EOF3 ="|__(__/|    |  ||____)__)/--\(__)|__";
string summary1 =" __                   __                        ";
string summary2 ="(_     _  _  _  _( ).|__)| _ ( ) _  |   _ |_|_ _ ";
string summary3 ="__)|_|||||||(_||  | .|   |(_| | _)  |__(_)|_|_(_)";
/*
string foot = "Summary:Pick Lotto tickets.";
string endOF = "EOF MESSAGE, Gilbert Edwards, 10/11/16, CIS-2542-001, Lab 12";
*/
/*
Powerball big letters
*/
string pbPrint1 =" __  __      __ __  __           ";   
string pbPrint2 ="|__)/  )|  ||_ |__)|__) /) |  |  ";  
string pbPrint3 ="|   (__/|/)||__| ( |__)/--)|__|__";
string pbPrint4 =" __  __      __ __  __           ";
string pbPrint5 ="|__)/  )|  ||_ |__)|__)|   /)(_) ";
string pbPrint6 ="|   (__/|/)||__| ( |   |__/--)|  ";
const int pageWidth = 82;
const int consoleWidth = 79;
int lineRemainder;
string bar = "|";
string dashline = "|--------------------------------------------------------------------------------|";

int choice =0;

/**format the box
******************/
void format(string sentence)
{
	lineRemainder = pageWidth - 1 - sentence.length();
	ofs << bar << sentence << setw(lineRemainder) << bar << endl;
}
/*Standard Header.*/
void hdr()
{
	ofs << dashline << endl;
	format(name1);
	format(name2);
	format(name3);
	format(course1);
	format(course2);
	format(course3);
	format(date1);
	format(date2);
	format(date3);
	format(project1);
	format(project2);
	ofs << dashline << endl;
}
/****************
prints the footer
****************/
void ftr()
{
	ofs << dashline << endl;
	format(summary1);
	format(summary2);
	format(summary3);

}

/****************
prints the End of File message
****************/
void eof()
{
	ofs << dashline << endl;
	format(EOF1);
	format(EOF2);
	format(EOF3);
	format(name1);
	format(name2);
	format(name3);
	format(course1);
	format(course2);
	format(course3);
	format(date1);
	format(date2);
	format(date3);
	format(project1);
	format(project2);
	ofs << dashline << endl;
}

/*****************
prints the ticket
*****************/
void displayTicket(int *ticket, int powerball,string type, int draw)
{
	ofs<< "ILLINOIS"<<endl;
	ofs<<pbPrint1<<endl;
	ofs<<pbPrint2<<endl;
	ofs<<pbPrint3<<endl;
	ofs<<pbPrint4<<endl;
	ofs<<pbPrint5<<endl;
	ofs<<pbPrint6<<endl;
	ofs<<"POWERBALL JACKPOT IS $425 \n MILLION IN THE WORDS OF \n MOTHER - 'EAT YOUR VEGGIES \n AND GO PLAY!'- GIL"<<endl;

	ofs<< "POWER PLAY: "<<"NO" <<endl;
	/*
	Prints loto numbers
	*/
	for (int a = 0; a < 5; a++ )
	{
		//cin>> arr1[a];
		ofs<< ticket[a]<<" ";	
	}

	ofs<<type <<"-"<< "PBall: "<< powerball<<type<<endl;
	ofs<< draw<<"draw(s) 10/19/2016"<<endl;
	ofs<<"TOTAL    $"<<draw*2<<endl<<endl; 
	ofs<<"LOTO  08/08/2016  $4.95MILL"<<endl;
	ofs<< "PWRB 08/07/2016  $425MILL"<<endl;
	ofs<< "MEGA 08/09/2016  $28MILL"<<endl<<endl;

	ofs<<"015026 9727-06346162-129627 180471-00"<<endl;
	ofs<<"10/19/2016 12:46:19"<<endl;
	ofs<<"|||  |  | |||| |||| | || ||||| | | |||"<<endl<<endl;


}
/*********************
generates loto ticket
********************/
void body()
{

	srand (time(NULL));

	/***Size of the array*/
	const int size1 = 5;
	//const int size2 = 200;
	/**Array 1 and array 2****/
	int arr1[size1];
	int arr2[size1];

	/****************
	holds powerball number and quickpicks
	****************/
	int powerball = 0;
	int quick = rand() % 10 + 1;
	
	/*************************************
	The range of random numbers from 1-69
	for lotto and 1-26 for powerball
	*************************************/
	int range = 69;
	int range2 =26;
	int number = 0;
	int count = 0;

	while (choice != 5)
	{
		/*********
		print menu
		*******/
		cout<<"\nMenu \n";
		cout<< "1. One Quick Pick \n";
		cout<<"2. Five Quick Pick’s  \n";
		cout<<"3. Any Number of Quick Picks \n";
		cout<<"4. Your selected numbers, including the Power Ball \n";
		cout<<"5. Quit \n";

		cin >> choice;
		switch (choice){

		/*************
		1 quick pick
		*************/
		case 1:

			cout<<"One Quick pick choosen: ";

			/*********************************
			Creates  numbers for array 1
			*********************************/
			for (int a = 0; a < size1; a++ )
			{
				//cin>> arr1[a];
				arr1[a] = rand() % range + 1;

			}
			powerball = rand() % range2 + 1;


			displayTicket(arr1, powerball, "QP", 1);
			break;

		case 2:
		/*************
		5 quick pick
		*************/
			cout<<"Five Quick pick choosen: ";

			for (int b = 0; b < 5; b++ )
			{
				/*********************************
				Creates  numbers for array 1
				*********************************/
				for (int a = 0; a < size1; a++ )
				{
					//cin>> arr1[a];
					arr1[a] = rand() % range + 1;

				}
				powerball = rand() % range2 + 1;


				displayTicket(arr1, powerball, "QP", 5);
			}
			break;
		case 3:
		/*************
		random quick picks
		*************/
			cout<<"Any Number of Quick Picks choosen: ";

			for (int b = 0; b < quick; b++ )
			{
				/*********************************
				Creates  numbers for array 1
				*********************************/
				for (int a = 0; a < size1; a++ )
				{
					//cin>> arr1[a];
					arr1[a] = rand() % range + 1;

				}
				powerball = rand() % range2 + 1;


				displayTicket(arr1, powerball, "QP", quick);
			}
			break;
		case 4:
		/*************
		user picks
		*************/
			cout<<"Please select numbers between 1-69: "<<endl;
			while (count < 5)
			{
				cout<< "Please Enter number: ";
				cin>> number;
				if (number <70 && number>0)
				{
					arr1[count] = number;
					count = count + 1;
				}
				else{
					cout<< "Invalid input. Please enter a number 1-69 \n";
				}
			}
			 
			powerball = 0;
			while(powerball <1 || powerball>26)
			{
				cout<<"Please select Powerball number between 1-26: "<<endl;
				cin >> powerball;
			}
			displayTicket(arr1, powerball, "SP", 1);
			break;
		case 5:
		/****
		quit
		****/
			break;
		default:
			cout<<"Please give a value between 1-5!";
			break;
		}
	}
}


int main() {
	hdr();
	body();
	ftr();
	eof();

	return 0;
}