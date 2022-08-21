class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        if self.next:
            return f'{self.val} -> {self.next}'
        
        return f'{self.val}' 