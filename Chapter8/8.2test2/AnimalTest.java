package com.yty.test2;

public class AnimalTest {

	public static void main(String[] args) {
		Dog dog1 = new Dog("̩��","С��",3,"��ɫ");
		dog1.intro();
		dog1.run();
		dog1.look();

		Dog dog2 = new Dog("��������","����",5,"���ɫ");
		dog2.intro();
		dog2.run();
		dog2.look();
		
		Cat cat1 = new Cat("��˹è","С��",2,"�̶�");
		cat1.intro();
		cat1.run();
		cat1.catches();
		
		Cat cat2 = new Cat("����è","����",4,"����");
		cat2.intro();
		cat2.run();
		cat2.catches();
	}

}
