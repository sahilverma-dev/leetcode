# https://leetcode.com/problems/average-waiting-time/


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        total_wait_time = 0
        current_time = 0

        for arrival, prep_time in customers:
            # Update current time if the chef is free
            current_time = max(current_time, arrival)

            # Calculate finish time for this customer
            finish_time = current_time + prep_time

            # Calculate wait time for this customer
            wait_time = finish_time - arrival

            # Add to total wait time
            total_wait_time += wait_time

            # Update current time to when this order is finished
            current_time = finish_time

        # Calculate average wait time
        return total_wait_time / len(customers)


s = Solution()

print("Example 1:", s.averageWaitingTime([[1, 2], [2, 5], [4, 3]]))  # 5.00000
