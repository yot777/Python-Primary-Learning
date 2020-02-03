public class Test3 {
  public static void main(String[] args) {
    int n = 100;
    int sum = 0;
    int counter = 1;
    while(counter <= n){
      sum = sum + counter;
      counter += 1;
    }
    System.out.printf("Sum of 1 until %d is %d",n,sum);
  }
}
