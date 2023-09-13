# area = min height * difference between indexes
from operator import index
from typing import List

# area = min height * difference between indexes


def max_area(heights: List[int]) -> int:
    pointer_a = 0
    pointer_b = len(heights) - 1
    max_water_area = 0

    for i in range(len(heights) - 1):
        while pointer_a <= pointer_b:
            if heights[pointer_a] < heights[pointer_b]:
                min_height = heights[pointer_a]
                index_diff = abs(index(pointer_a) - index(pointer_b))
                water_area = min_height * index_diff

                if water_area > max_water_area:
                    max_water_area = water_area

            else:
                min_height = heights[pointer_b]
                index_diff = abs(index(pointer_a) - index(pointer_b))
                water_area = min_height * index_diff

                if water_area > max_water_area:
                    max_water_area = water_area

            pointer_b += -1
        pointer_a += 1
        pointer_b = len(heights) - 1

    return max_water_area
