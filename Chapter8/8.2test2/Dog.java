package com.yty.test2;

public class Dog extends Animal{

	public String hair;

	public Dog(String types, String name, int age, String hair) {
		super(types, name, age);
		this.hair = hair;
	}
		@Override
		public void intro(){
			System.out.println("����һֻ"+this.types+",������"+this.name+",������"+this.age+"��,ë����ɫ��"+this.hair);
		}
		
		public void look(){
			System.out.println("�һῴ����");
		}
}
