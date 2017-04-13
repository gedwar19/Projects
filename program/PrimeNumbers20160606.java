/*The following class extends Thread.
It determines the prime numbers within a given range.
It stores those prime numbers in an array list.
*/
import java.util.ArrayList;

class PrimeThread extends Thread{
	private int start;//starting number
	private int end;//ending number
	private ArrayList<Integer> primes;
	public ArrayList<Integer> getPrimes(){
		return primes;
	}
	public PrimeThread(){
		super("No name");
		start = 3;
		end = 1000;
		primes = new ArrayList<Integer>();
	}
	public PrimeThread(String name, int start, int end){
		super(name);
		int temp;
		if (start > end){
			temp =start;
			start = end;
			end = temp;
		}
		this.end = end;
		if (start % 2 == 0){
			this.start = start + 1;
		}else {
			this.start = start;
		}
		primes = new ArrayList<Integer>();
	}
	public void run(){
		for (int i = start ; i <=end; i++){
			if (isPrime(i)){
				primes.add(i);
				System.out.println("Thread-" + getName() + ": " + i);
			}
		}
	}
	public boolean isPrime(int num){
		if (num == 0){
			return false;
		}else if (num == 1){
			return false;
		}else if (num % 2 == 0){
			return false;
		}else{
			for (int i = 3; i <= Math.sqrt(num); i = i + 2){
				if (num % i == 0){
					return false;
				}
			}
			return true;
		}
	}
}

public class PrimeNumbers20160606{
	public static void main(String[] args){
		/*Create multiple threads.
		place them in an array list
		tell each thread to start.
		coordinate the finishing of those threads (join)
		when all the threads are finished, print the prime numbers that each found
		*/
		ArrayList<PrimeThread> threads = new ArrayList<PrimeThread>();
		threads.add(new PrimeThread("1",1,249999));
		threads.add(new PrimeThread ("2", 250000, 499999));
		threads.add(new PrimeThread ("3", 500000, 749999));
		threads.add(new PrimeThread ("4", 750000, 999999));
		for (PrimeThread pt : threads){
			pt.start();
		}
		for (PrimeThread pt : threads){
			try{
				pt.join();
				System.out.println("Done with thread " + pt.getName());
			}catch (Exception ex){
				System.out.println("Something bad happened");
			}
		}
		System.out.println("Here are all the prime numbers");
		ArrayList<Integer> primes;
		for (PrimeThread pt : threads){
			primes = pt.getPrimes();
			for (Integer i : primes){
				System.out.println(i);
			}
		}
	}
}