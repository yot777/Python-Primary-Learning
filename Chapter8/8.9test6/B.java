package com.yty.test6;

import com.yty.test5.A;

public class B {
	public void B(){
		System.out.println("This is init function of B");			
	}
	public static void main(String[] args) {
		//导入了A类之后，必须实例化一个A类的对象a，才能调用A类的方法
		A a = new A();
		a.A();
		B b = new B();
		b.B();
	}
}
