package com.yty.test2;

public class Cat extends Animal{
	
	public String ear;

	public Cat(String types, String name, int age, String ear) {
		super(types, name, age);
		this.ear = ear;
	}
		@Override
		public void intro(){
			System.out.println("����һֻ"+this.types+",������"+this.name+",������"+this.age+"��,���䳤����"+this.ear);
		}
		
		public void catches(){
			System.out.println("�һ�ץ����");
		}
}
