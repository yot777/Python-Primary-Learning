public class Test5 {
  public static void main(String[] args) {
    int m,n,s;
    for(m=0;m<5;m++)
      System.out.println("m="+m);
    System.out.println('\n');
    for(n=5;n<9;n++)
      System.out.println("n="+n);
    System.out.println('\n');
    for(s=0;s<10;s+=3)
      System.out.println("s="+s);
    System.out.println('\n');
 /*Java只支持步长为正数，不支持步长为负数*/
  }
}