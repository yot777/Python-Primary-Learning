public class Test6 {
  public static void main(String[] args) {
    int a = 2;
    System.out.println(a);
    System.out.println(ChangeInt(a));
    System.out.println(a);
  }
  public static int ChangeInt(int n){
    n = 10;
    return n;
  }
}