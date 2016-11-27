import java.util.ArrayList;
import java.util.HashMap;

public class EulerTwentyOne {

	public static void main(String[] args) {
		HashMap<Integer,Integer> matches = new HashMap<Integer,Integer>();
		matches.put(1, -1000);
		for (int i = 2; i < 10000; i++) {
			matches.put(i, sumFactors(i));
		}
		int sumAmicable = 0;
		for (int i = 2; i < 10000; i++) {
			if (matches.containsKey(matches.get(i)) ? (i == matches.get(matches.get(i)) && i != matches.get(i)) : false) {
				System.out.println(i + " " + matches.get(i));
				sumAmicable += i;
				
			}
		}
		System.out.println(sumAmicable);
	}
	
	public static int sumFactors(int n) {
		ArrayList<Integer> factors = new ArrayList<Integer>();
		factors.add(1);
		for (int i = 2; i < Math.ceil(Math.sqrt(n)); i++) {
			if (n%i==0) {
				factors.add(i);
				factors.add((int) n/i);
			}
		}
		
		int sum = 0;
		for (int i : factors) sum+=i;
		return sum;
	}
	
}
