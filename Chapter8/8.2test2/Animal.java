package com.yty.test2;

public class Animal {
	public String types;
	public String name;
	public int age;	
	
	public Animal(String types,String name,int age){
		this.types = types;
		this.name = name;
		this.age = age;
	}
	
	public void intro(){
		System.out.println("我是一只"+this.types+",名字是"+this.name+",年龄是"+this.age+"岁");
	}
	
	public void run(){
		System.out.println("我飞快的跑");
	}
}
