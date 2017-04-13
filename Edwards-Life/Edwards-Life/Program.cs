//Conways-The game of life

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace Edwards_Life
{
    class Program
    {
        //void Life(uint, uint);
        //void displayBoard(int[,] board, int a, int b);

        static void Main(string[] args)
        {
            uint x = 80;
            uint y = 24;

            Life(x,y);
        }

        static void Life(uint x, uint y)
        {
            //max number of generations
            const int MAXGEN = 100;

            int generation = 0;
    
            bool game = true;

            int[,] current = new int[x, y];
            int[,] next = new int[x, y];

            //initially alive cells
            current[5, 5] = 2;
            current[5, 6] = 2;
            current[5, 7] = 2;
            current[6, 5] = 2;
            current[6, 6] = 2;
            current[7, 6] = 2;
            current[7, 8] = 2;
            current[14, 8] = 2;
            current[11, 9] = 2;
            current[9, 8] = 2;

            ///displays the initial board
            displayBoard(current, current, x, y);
            Console.WriteLine("Generation : " + generation);
            Console.WriteLine();
            Thread.Sleep(50);
            Console.Clear();

            //runs the game, while game method is true and generation is under set number 
            while (game == true && generation < MAXGEN)
            {
                PlayOne(current, next, x, y);
                game = GameOver(current, next, x, y );
                if (game == false)
                { break; }
                displayBoard(current, next, x, y);
                ++generation;
                Console.WriteLine("Generation : " + generation);
                Thread.Sleep(50);
                Console.Clear();
                

            }
        }

        static void PlayOne(int[,] Old, int[,] New, uint a, uint b)
        {
            int neighbors = 0;
            
            for (int x = 0; x < a; x++)
            {
                for (int y = 0; y < b; y++)
                {
                    //check for horizontal neighbors
                    if (x == 0)
                    {
                        if (Old[x + 1,y] >= 1)
                        {
                            ++neighbors;
                        }
                    }
                    else if (x == (a-1))
                    {
                        if (Old[x - 1, y] >= 1)
                        {
                            ++neighbors;
                        }
 
                    }
                    else
                    {
                        if (Old[x - 1,y] >= 1)
                        {
                            ++neighbors;
                            
                        }
                        if (Old[x + 1,y] >= 1)
                        {
                            ++neighbors;
                            
                        }
                        
                    }

                    //check for vertical neighbors
                    if (y == 0)
                    {
                        if (Old[x, y + 1] >= 1)
                        {
                            ++neighbors;
                        }
                    }
                    else if (y == (b - 1))
                    {
                        if (Old[x, y - 1] >= 1)
                        {
                            ++neighbors;
                        }

                    }
                    else 
                    {
                        if (Old[x,y - 1] >= 1)
                        {
                            ++neighbors;
                           
                        }
                        if (Old[x,y + 1] >= 1)
                        {
                            ++neighbors;
                            
                        }
                    }

                    //check for diagonal neighbors
                    if (x == 0 && y == 0)
                    {
                        if (Old[1, 1] >= 1)
                        {
                            ++neighbors;
                        }
                    }
                    else if (x == (a - 1) && y == 0)
                    {
                        if (Old[x-1, 1] >= 1)
                        {
                            ++neighbors;
                        }
                    }
                    else if (x == 0 && y == (b-1))
                    {
                        if (Old[1,y-1] >= 1)
                        {
                            ++neighbors;
                        }
                    }
                    else if (x == (a - 1) && y == (b - 1))
                    {
                        if (Old[x - 1, y - 1] >= 1)
                        {
                            ++neighbors;
                        }
                    }
                    else if(x == 0)
                    {
                        //upper right
                        if (Old[x + 1, y - 1] >= 1)
                        {
                            ++neighbors;
                        }
                        //Lower right
                        if (Old[x + 1, y + 1] >= 1)
                        {
                            ++neighbors;
                        }
                    }
                    else if (x == (a - 1))
                    {
                        //upper left
                        if (Old[x - 1, y - 1] >= 1)
                        {
                            ++neighbors;
                        }
                        //Lower left
                        if (Old[x - 1, y + 1] >= 1)
                        {
                            ++neighbors;
                        }
 
                    }
                    else if (y == 0)
                    {
                        //Lower left
                        if (Old[x - 1, y + 1] >= 1)
                        {
                            ++neighbors;
                        }
                        //Lower right
                        if (Old[x + 1, y + 1] >= 1)
                        {
                            ++neighbors;
                        }
                    }
                    else if (y == (b - 1))
                    {
                        //upper left
                        if (Old[x - 1, y - 1] >= 1)
                        {
                            ++neighbors;
                        }
                        //upper right
                        if (Old[x + 1, y - 1] >= 1)
                        {
                            ++neighbors;
                        }
                    }
                    else
                    {
                        //upper left
                        if (Old[x - 1, y - 1] >= 1)
                        {
                            ++neighbors;
                        }
                        //Lower left
                        if (Old[x - 1, y + 1] >= 1)
                        {
                            ++neighbors;
                        }
                        //upper right
                        if (Old[x + 1, y - 1] >= 1)
                        {
                            ++neighbors;
                        }
                        //Lower right
                        if (Old[x + 1, y + 1] >= 1)
                        {
                            ++neighbors;
                        }

                    }
                    //**********************************

                    //checks how many neighbors the cell has
                    if (neighbors <= 1 )
                    {
                        //dieing cells are changed to 0
                        New[x, y] = 0;
                    }
                    else if (neighbors == 2 )
                    {
                        if (Old[x, y] >= 1)
                        {
                            //living cell is set to 2
                            New[x, y] = 2;
                        }
  
                    }
                    else if (neighbors == 3)
                    {
                        //new cell is set to 3
                        New[x, y] = 3;
                        
                    }
                    else if (neighbors >= 4)
                    {
                        //over crowded dead cell is set to 0
                        New[x, y] = 0;
                    }
                    
                    neighbors = 0;
                }
            }
            
        }

        //displays the board, - is for dead cells, O is for living old cells, N is for new living cells
        static void displayBoard(int [,] old , int[,] board, uint a, uint b)
        {
            for (int y = 0; y < b; y++)
            {
                for (int x = 0; x < a; x++)
                {
                    if (board[x, y] <= 1)
                    {
                        Console.ForegroundColor = ConsoleColor.White;
                        Console.Write(" ");
                    }
                    else if (board[x, y] >= 4)
                    {
                        Console.ForegroundColor = ConsoleColor.Gray;
                        Console.Write(" ");
                    }
                    else if (board[x, y] == 2)
                    {
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.Write("O");
                    }
                    else if (board[x, y] == 3)
                    {
                        Console.ForegroundColor = ConsoleColor.Blue;
                        Console.Write("N");
                    }
                    
                    old[x, y] = board[x, y];
                     
                }
                Console.WriteLine();
            }
        }

        //check for game over, returns true if game is continueing false if empty or two repeated generation in a row
        static bool GameOver(int [,] old , int[,] board, uint a, uint b)
        {
            int different = 0;
            for (int y = 0; y < b; y++)
            {
                for (int x = 0; x < a; x++)
                {
                    if (old[x,y] != board[x,y])
                    {
                        ++different;
                    }
                }
            }
                if (different > 1)
                {
                    return true;
                }
                else
                {
                    return false;
                }
        }
    }
}
