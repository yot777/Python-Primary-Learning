package com.yty.test4;

public class Person {
	public static int num=0;
	public String name;
	public int n;

	public void Person(String name) {
		this.name = name;
		n=0;
		n=n+1;
		num=num+1;
		System.out.println("name="+this.name);
		System.out.println("n="+n);	
		System.out.println("Person.num="+num);			
	}

}
