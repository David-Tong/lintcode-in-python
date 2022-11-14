class Solution:
    """
    @param time_series: the Teemo's attacking ascending time series towards Ashe
    @param duration: the poisoning time duration per Teemo's attacking
    @return: the total time that Ashe is in poisoned condition
    """
    def find_poisoned_duration(self, time_series, duration):
        # Write your code here
        if len(time_series) == 0:
            return 0

        left = time_series[0]
        right = time_series[0] + duration

        ans = 0
        for time_serie in time_series[1:]:
            if time_serie <= right:
                right = time_serie + duration
            else:
                ans += right - left
                left = time_serie
                right = time_serie + duration

        ans += right - left
        return ans


time_series = [1,4]
duration = 2

time_series = [1,2]
duration = 2

time_series = []
duration = 2

time_series = [10]
duration = 2

solution = Solution()
print(solution.find_poisoned_duration(time_series, duration))
