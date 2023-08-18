/*
 * @lc app=leetcode id=225 lang=java
 *
 * [225] Implement Stack using Queues
 */

// @lc code=start

import java.util.ArrayList;

class MyStack {

    private int[] queue = new int[100];
    private int top = -1;

    public MyStack() {
        
    }
    
    public void push(int x) {
        top++;
        queue[top] = x;
    }
    
    public int pop() {
        int last = queue[top];
        top--;
        return last;
    }
    
    public int top() {
        return queue[top];
    }
    
    public boolean empty() {
        return top == -1;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
// @lc code=end

