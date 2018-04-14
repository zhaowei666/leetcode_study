def max_area(height):
    left, right = 0, len(height) - 1
    res = 0
    while left < right:
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        area = (right - left) * min(height[left], height[right])
        if area > res:
            res = area
    return res