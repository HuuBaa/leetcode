一、Reverse Linked List

反转链表

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #递归  
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head,None)

    def helper(self,node,prev):
        if node:            
            cur=node.next
            node.next=prev
            return self.helper(cur,node)
        else:
            return prev

  #######################################################   
  #迭代   
  def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        while head:
            curr=head
            head=head.next
            curr.next=prev
            prev=curr
        return prev 

        ###简洁

        pre=None
        curr=head
        while curr:
            curr.next,pre,curr=pre,curr,curr.next
        return pre    

 

二、 Reverse Linked List II
给定链表和m,n两位置,反m-n位置之间的链表

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for i in range(m-1):
            pre=pre.next
        curr=pre.next
        rev=None
        for i in range(n-m+1):   
            tmp=curr.next
            curr.next=rev
            rev=curr
            curr=tmp
     ##反转中间一段后连接   
        pre.next.next=curr
        pre.next=rev         
        return dummy.next



if m==n:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for i in range(m-1):
            pre=pre.next
        curr=pre.next
        then=curr.next
        ##不断把then换到pre后面
        for i in range(n-m):      
            curr.next=then.next
            then.next=pre.next
            pre.next=then
            then=curr.next

        return dummy.next