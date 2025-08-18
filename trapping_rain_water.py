#42. Trapping Rain Water

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


def trap(self, height):
    if not height:
        return 0
    l, r = 0, len(height)-1
    maxL, maxR = height[l], height[r]
    res = 0

    while l < r:
        if maxL < maxR:
            l += 1
            maxL = max(maxL, height[l])
            res += maxL - height[l]

        else:
            r -= 1
            maxR = max(maxR, height[r])
            res += maxR - height[r]

    return res