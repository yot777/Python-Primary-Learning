package com.yty.test2;

public class Dog extends Animal{

	public String hair;

	public Dog(String types, String name, int age, String hair) {
		super(types, name, age);
		this.hair = hair;
	}
		@Override
		public void intro(){
			System.out.println("我是一只"+this.types+",名字是"+this.name+",年龄是"+this.age+"岁,毛发颜色是"+this.hair);
		}
		
		public void look(){
			System.out.println("我会看家门");
		}
}
