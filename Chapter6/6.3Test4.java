public class Test4 {
  public static void main(String[] args) {
    String[] edibles = {"ham","eggs","nuts"};
    int i=0;
    for (String food : edibles){
        if(food == "spam"){
            System.out.println("No more spam please!");
            break;
        }
        System.out.println("Great, delicious " + food);
        i=i+1;
    }  //Java的for循环没有最后的else，如果要实现Python里for-else功能需要自己写逻辑
    if(i==edibles.length){
      System.out.println("I am so glad: No spam!");
    }
    System.out.println("Finally, I finished stuffing myself.");
  }
}