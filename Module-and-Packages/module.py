# import <module_name>
# import rating as helper

# from <module_name> import <variable>, <function1>.......etc
from rating import analysis_ratings, PI

ls1 = [1, 2, 3, 4, 5]
ls2 = [6, 7]
ls3 = None


# print(helper.analysis_rating(ls1))
# print(helper.analysis_rating(ls2))
# print(helper.analysis_rating(ls3))

print(f"Hello from {__name__}")

print("-------------------------")

print(analysis_ratings(ls1))
print(analysis_ratings(ls2))
print(analysis_ratings(ls3))

print(PI)
