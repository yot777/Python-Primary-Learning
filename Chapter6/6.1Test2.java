import java.util.Scanner;
public class Test2 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Age of the dog: ");
    int dog_age = sc.nextInt();
    if(dog_age == 1){
      System.out.println("This dog is about 14 human years old.");
    }else if(dog_age == 2){
      System.out.println("This dog is about 22 human years old.");
    }else if(dog_age > 2){
      int human_age = 22 + (dog_age -2)*5;
      System.out.println("This dog is about "+human_age+" human years old.");
    }else{
      System.out.println("Input Error!");
    }
    sc.close();
  }
}