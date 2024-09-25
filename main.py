from math import *
import itertools

PI = pi
x = 23


print("log", log(8, 2))
print(log(x))

print(ord('s')) # returns the ASCII code
print("aaa", end = "") # special argument
print(exp(-1))

s = "True"
print(s.lower())
print(s.upper())

s2 = " Hello World "
print(s2.strip()) 

# format(item, format-specifier)
#conversion code
# precision code


print(format(123.2313, '10.2f'))
print(format(2.12, '10.2f'))
print(format(10.2332313123, "10.2e")) # scientific
print(format(1313.22323), '10.2%') 

print(floor(2.4))

# set demonstration


# operation of sets

# Combinations (Number of combinations, not concerned with order)
def combinations(s, k):
    return list(itertools.combinations(s, k))
def numOfCombinations(s, k):
    return "The number of combinations with ", k, "-element is: ", len(combinations(s, k))

# Permutations (Number of combinations, concerned with order)
def permutations(s, k):
    return list(itertools.permutations(s, k))
def numOfPermutations(s, k):
    return "The number of permutation with ", k, "-element is: ", len(permutations(s, k))


# Power Set (List of all subsets)
def powerSet(s):
    listOfAllSubsets = []
    for i in range(len(s) + 1):
        listOfAllSubsets.extend(itertools.combinations(s, i))
    return listOfAllSubsets

# exampleSet1.union(exampleSet2) - takes all the elements from set1 to set2
# exampleSet1.symmetric_dfference(exampleSet2) - takes all the elements not intersecting set 1 and set 2
# exampleSet1.intersection(exampleSet2) - takes all the elements in common inside both sets

emptySet = set()
myFavMealComb = {'rice', 'fried chicken', 'egg', 'tea'}
jamesFavMealComb = {'rice', 'fried chicken', 'corned beef', 'coke'}
commonMealThatEveryonePicks = {'rice', 'fried chicken'}

universalSet = myFavMealComb | jamesFavMealComb

# option 1
commonFavMealOpt1 = myFavMealComb & jamesFavMealComb
mealsThatILikeButJamesOpt1 = myFavMealComb - jamesFavMealComb
mealsThatILikeButJames2Opt1 = universalSet - jamesFavMealComb # complement opt 1
mealsThatJamesLikeButIOpt1 = jamesFavMealComb - myFavMealComb
mealsThatJamesLikeButI2Opt1 = universalSet - myFavMealComb # complement opt 1
mealsThatWeLikeButNotInCommonOpt1 = mealsThatILikeButJamesOpt1 | mealsThatJamesLikeButIOpt1
mealsThatWeLikeButNotInCommon2Opt1 = myFavMealComb ^ jamesFavMealComb



# option 2
commonFavMealOpt2 = myFavMealComb.intersection(jamesFavMealComb)
mealsThatILikeButJamesOpt2 = myFavMealComb.difference(jamesFavMealComb)
mealsThatILikeButJames2Opt2 = universalSet.difference(myFavMealComb) # complement opt 2
mealsThatJamesLikeButIOpt2 = jamesFavMealComb.difference(myFavMealComb)
mealsThatJamesLikeButI2Opt2 = universalSet.difference(myFavMealComb) # complement opt 2
mealsThatWeLikeButNotInCommonOpt2 = mealsThatILikeButJamesOpt2.union(mealsThatJamesLikeButIOpt2)
mealsThatWeLikeButNotInCommon2Opt2 = mealsThatILikeButJamesOpt2.symmetric_difference(mealsThatJamesLikeButIOpt2)


# print(mealsThatILikeButJamesOpt2)
# print(numOfCombinations(myFavMealComb, 2))
# print(numOfPermutations(myFavMealComb, 4))
# print(combinations(myFavMealComb, 2))
# print(permutations(myFavMealComb, 4))
# print(powerSet(myFavMealComb))
# print(set(itertools.product(myFavMealComb, jamesFavMealComb)))
print(commonMealThatEveryonePicks.issubset(myFavMealComb))
print(commonMealThatEveryonePicks.issuperset(myFavMealComb))
print("Empty set is a subset of any sets: ", emptySet.issubset(myFavMealComb))
print(myFavMealComb.isdisjoint(jamesFavMealComb))
    

# 0000
# 0001

print(degrees(pi/2))
print(radians(23))
print(degrees(0.40))
print(12%16)