package com.yty.test2;

public class AnimalTest {

	public static void main(String[] args) {
		Dog dog1 = new Dog("泰迪","小黑",3,"棕色");
		dog1.intro();
		dog1.run();
		dog1.look();

		Dog dog2 = new Dog("拉布拉多","旺财",5,"金黄色");
		dog2.intro();
		dog2.run();
		dog2.look();
		
		Cat cat1 = new Cat("波斯猫","小咪",2,"短耳");
		cat1.intro();
		cat1.run();
		cat1.catches();
		
		Cat cat2 = new Cat("暹罗猫","花花",4,"长耳");
		cat2.intro();
		cat2.run();
		cat2.catches();
	}

}
