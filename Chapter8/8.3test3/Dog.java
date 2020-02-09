package com.yty.test3;

public class Dog {
	public String types = "泰迪";
	public String name = "小黑";
	public int age = 3;
	//私有属性
	private String hair = "棕色";
	
	public void setHair(String hair) {
		this.hair = hair;
	}
	public String getHair() {
		return hair;
	}
}
