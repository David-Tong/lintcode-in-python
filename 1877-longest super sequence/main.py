class Solution:
    """
    @param nums: the input array
    @return: return the longest super sequence
    """
    def longestSuperSequence(self, nums):
        # write your code here
        # pre-process
        from collections import defaultdict
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        reverseds = defaultdict(list)
        for count in counts:
            reverseds[counts[count]].append(count)
        # print(reverseds)

        cnts = list()
        for key in sorted(reverseds.keys()):
            cnts.append(len(reverseds[key]))
        # print(cnts)
        postsums = list()
        presum = 0
        total = sum(cnts)
        for cnt in cnts:
            postsums.append(total - presum)
            presum += cnt
        # print(postsums)

        # process
        # condition 1 - all numbers have same counts
        if len(reverseds) == 1:
            for key in reverseds:
                # condition 1.1 - only one number
                if len(reverseds[key]) == 1:
                    return nums
                # condition 1.2 - only two numbers
                elif len(reverseds[key]) == 2:
                    return nums[1:]
                else:
                    # condition 1.3 - more than one number but with count one
                    if key == 1:
                        return nums
                    # condition 1.4 - more than one number, select any number and keep only one for it
                    else:
                        reduced = reverseds[key][0]
                        selected = reverseds[key][1:]
                        selected_count = key
                        break
        # condition 2 - find the longest numbers with same counts
        else:
            maxi = 0
            for idx, key in enumerate(sorted(reverseds.keys())):
                expected = postsums[idx] * key + 1
                if expected > maxi:
                    # print(expected)
                    maxi = expected
                    selected_count = key
                    selected_idx = idx

            # condition 2.1 - select a number with counts larger than selected count and reduce it to once
            selected = list()
            reduced = -1
            if selected_idx == 0:
                for idx, key in enumerate(sorted(reverseds.keys())):
                    if idx == 0:
                        selected.extend(reverseds[key])
                    else:
                        if reduced == -1:
                            selected.extend(reverseds[key])
                            reduced = reverseds[key][0]
                        else:
                            selected.extend(reverseds[key])
            # condition 2.2 - select a number with counts less than selected count and reduce it to once
            else:
                for key in sorted(reverseds.keys())[selected_idx:]:
                    selected.extend(reverseds[key])
                reduced = reverseds[sorted(reverseds.keys())[0]][0]

        # output
        ans = list()
        insert = False
        ans = list()
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            if num == reduced and not insert:
                ans.append(num)
                insert = True
            elif num in selected:
                if dicts[num] < selected_count:
                    ans.append(num)
                    dicts[num] += 1
        return ans


nums = [1,1,1,1]
nums = [1,1,1,1,1,1,1]
nums = [1,1,1,3,2,2,2,3]
nums = [1,1,1,3,2,2,2,3,3]
nums = [1,1,3,3,3,3,2,2,2]
nums = [1,1,3,3,3,3,2,2,2,2]
nums = [1,2,3,3,2,1,4,4,5,5,5,5,4]
nums = [x + 1 for x in range(3000)]
nums = [0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1]
nums = [1,1,1,2,2,2]

solution = Solution()
print(solution.longestSuperSequence(nums))
