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
		System.out.println("����һֻ"+this.types+",������"+this.name+",������"+this.age+"��");
	}
	
	public void run(){
		System.out.println("�ҷɿ����");
	}
}
