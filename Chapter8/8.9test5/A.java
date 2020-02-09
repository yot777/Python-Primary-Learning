package com.yty.test5;

public class A extends Base{
	public void A() {
		//调用父类Base的构造函数
		super.Base();
		System.out.println("This is init function of A");		
	}
}
