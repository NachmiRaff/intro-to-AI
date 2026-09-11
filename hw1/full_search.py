from one.search import search as search_one
from two.search import search as search_two
from three.search import search as search_three
from four.search import search as search_four
from five.search import search as search_five
from five.state import create as create
from greedy.search import search as search_greedy

import pandas as pd
import copy


searches = [
    search_one,
    search_greedy,
    search_two,
    search_three,
    search_four,
    search_five
]

runs = 100
sizes = [3, 4, 5]

output = []

for num in sizes:
    for _ in range(runs):
        board = create(num)
        for j, search in enumerate(searches):
            result = search(copy.deepcopy(board))
            output.append([
                j + 1,
                num,
                result[1],
                result[2],
                result[3],
                result[4],
                result[0]
            ])

df = pd.DataFrame(output, columns=["algorithm", "size", "pushed", "popped", "cost", "success", "raw"])


df["algorithm"] = df["algorithm"].replace({
    1: "Uniform",
    2: "Greedy",
    3: "Tiles",
    4: "Manhattan",
    5: "Weighted",
    6: "Linear Combinations"
})

size_3 = df[df["size"] == 3]

table_3 = size_3.groupby("algorithm")[["pushed", "popped", "cost", "success"]].mean()

table_3.columns = ["average pushed", "average checked", "average cost", "success rate"]

table_3["max pushed"] = size_3.groupby("algorithm")["pushed"].max()
table_3["max checked"] = size_3.groupby("algorithm")["popped"].max()
table_3["max cost"] = size_3.groupby("algorithm")["cost"].max()

table_3



size_4 = df[df["size"] == 4]

table_4 = size_4.groupby("algorithm")[["pushed", "popped", "cost", "success"]].mean()

table_4.columns = ["average pushed", "average checked", "average cost", "success rate"]

table_4["max pushed"] = size_4.groupby("algorithm")["pushed"].max()
table_4["max checked"] = size_4.groupby("algorithm")["popped"].max()
table_4["max cost"] = size_4.groupby("algorithm")["cost"].max()

table_4



size_5 = df[df["size"] == 5]

table_5 = size_5.groupby("algorithm")[["pushed", "popped", "cost", "success"]].mean()

table_5.columns = ["average pushed", "average checked", "average cost", "success rate"]

table_5["max pushed"] = size_5.groupby("algorithm")["pushed"].max()
table_5["max checked"] = size_5.groupby("algorithm")["popped"].max()
table_5["max cost"] = size_5.groupby("algorithm")["cost"].max()

table_5


with open("results.md", "w") as f:
    f.write("# Size 3\n\n")
    f.write(table_3.to_markdown())
    
    f.write("\n\n# Size 4\n\n")
    f.write(table_4.to_markdown())
    
    f.write("\n\n# Size 5\n\n")
    f.write(table_5.to_markdown())



# I increased the amount run to 15,000 This significantly decreased error rate. I also gave all the of them the same 100 boards to make data clearer.

# Size 3

# | algorithm           |   average pushed |   average checked |   average cost |   success rate |   max pushed |   max checked |   max cost |
# |:--------------------|-----------------:|------------------:|---------------:|---------------:|-------------:|--------------:|-----------:|
# | Greedy              |          2473.19 |           2377.73 |          24.37 |           0.85 |        15000 |         15000 |        173 |
# | Linear Combinations |            16.93 |              9.74 |           6.15 |           1    |          133 |            80 |         13 |
# | Manhattan           |            18.59 |             10.72 |           6.15 |           1    |          193 |           113 |         13 |
# | Tiles               |            33.82 |             19.2  |           6.15 |           1    |          390 |           221 |         13 |
# | Uniform             |           538.23 |            315.23 |           6.15 |           1    |         6393 |          3717 |         13 |
# | Weighted            |            29.95 |             17.13 |           6.57 |           1    |          389 |           225 |         26 |

# # Size 4

# | algorithm           |   average pushed |   average checked |   average cost |   success rate |   max pushed |   max checked |   max cost |
# |:--------------------|-----------------:|------------------:|---------------:|---------------:|-------------:|--------------:|-----------:|
# | Greedy              |         11973    |          11907.3  |          84.67 |           0.21 |        15000 |         15000 |        179 |
# | Linear Combinations |           316.47 |            150.85 |          16.12 |           1    |         4168 |          1968 |         28 |
# | Manhattan           |           624.54 |            298.19 |          16.12 |           1    |         9229 |          4356 |         28 |
# | Tiles               |          4239.52 |           3579.72 |          31.47 |           0.8  |        15000 |         15000 |        100 |
# | Uniform             |         12873.6  |          12409.8  |          81.71 |           0.2  |        15000 |         15000 |        100 |
# | Weighted            |          2234.77 |           1524.11 |          26.38 |           0.94 |        15000 |         15000 |        100 |

# # Size 5

# | algorithm           |   average pushed |   average checked |   average cost |   success rate |   max pushed |   max checked |   max cost |
# |:--------------------|-----------------:|------------------:|---------------:|---------------:|-------------:|--------------:|-----------:|
# | Greedy              |         15000    |          15000    |         100    |           0    |        15000 |         15000 |        100 |
# | Linear Combinations |          7570.7  |           6592    |          57.62 |           0.61 |        15000 |         15000 |        100 |
# | Manhattan           |          9326.12 |           8373.73 |          65.27 |           0.49 |        15000 |         15000 |        100 |
# | Tiles               |         14076.3  |          13918.3  |          93.6  |           0.08 |        15000 |         15000 |        100 |
# | Uniform             |         15000    |          15000    |         100    |           0    |        15000 |         15000 |        100 |
# | Weighted            |         10327.9  |           8872.65 |          75.12 |           0.48 |        15000 |         15000 |        100 |


# Questions

# A. No, it is not. One indication is that it has a higher average cost. If you look at the 3X3 and compare, they had a 100% success rate, but this had a larger max cost (6.57 vs 6.15), which is proof that it is not admissible.

# B. 1. Yes, it is proven in the paper that you linked. Also, you can see it has the same average. The intuition is that to get around a piece you need to move down and up, so you should add that to Manhattan distance (the blog version overcounts, so that is not admissible).
    # 2. No, it would overcount (also tests gave higher count).
    # 3. No. This also will overcount (also tests gave higher count).
    # 4. In my tests (data is here HW1\five\questions), the average cost of successful runs is higher the more you weight linear conflicts. The other seemed a little better in speed, with 2 times seeming the fastest.

# C. ID managed to do 11%, BFS and Uniform Cost both managed to do 13%. (When I changed the seed, I got data like the one above. However, I used the same seed for all in this question, so it remains consistent.) The data is in the output.txt of the corresponding dirs.
