def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not
    """

    slow_runner = linked_list.head
    fast_runner = linked_list.head

    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
        if slow_runner == fast_runner:
            return True
    return False

