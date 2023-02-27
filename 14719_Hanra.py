[h, w] = list(map(int, input().split(" ")))
blocks = list(map(int, input().split(" ")))

left = 0
right = w-1
height = min(blocks[left], blocks[right])
water = 0

while left < right:
    # print("start", left, right, height)
    if blocks[left] < blocks[right]:
        left += 1
        # print(left, height, height - blocks[left])
        water += max(0, height - blocks[left])
        if blocks[left] > height:
            # print("here", blocks[left], blocks[right], height)
            height = min(blocks[right], blocks[left])
    else:
        right -= 1
        # print(right, height, height - blocks[right])
        water += max(0, height - blocks[right])
        if blocks[right] > height:
            # print("here", blocks[left], blocks[right], height)
            height = min(blocks[left], blocks[right])

print(water)