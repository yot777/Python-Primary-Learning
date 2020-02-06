package com.yty.test2;

public class Cat extends Animal{
	
	public String ear;

	public Cat(String types, String name, int age, String ear) {
		super(types, name, age);
		this.ear = ear;
	}
		@Override
		public void intro(){
			System.out.println("我是一只"+this.types+",名字是"+this.name+",年龄是"+this.age+"岁,耳朵长度是"+this.ear);
		}
		
		public void catches(){
			System.out.println("我会抓老鼠");
		}
}
