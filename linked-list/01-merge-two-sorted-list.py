from ListNode import ListNode, build_list, print_list


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next


# Call functions directly
list1 = build_list([1, 3, 5])
list2 = build_list([2, 4, 6])

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the result
print_list(merged_list)
