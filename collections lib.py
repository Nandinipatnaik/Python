import collections
##collections lib has 6 modules, 1.counter, 2.defaultdict
# 3.ordereddict,4.deque,5.chain map,6.namedtuple
list1=[1,2,3,4,1,2,6,7,3,8,1]
from collections import Counter
d=collections.Counter(list1)
#### d is a counter object, counter is a data structures from python module,
print(d)
##### O/P Counter({1: 3, 2: 2, 3: 2, 4: 1, 6: 1, 7: 1, 8: 1})

Counter({1:3,2:4})
###it can take dictonary as an argument

####counter has three additional function: elements,most_common,subtrack
cnt = Counter({1:3,2:4})
print(list(cnt.elements()))##it returns all the elimentsin counter object
# ##O/P [1, 1, 1, 2, 2, 2, 2]

list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt.most_common())##You can sort it according to the number of counts in each element
##o/p [(1, 3), (2, 2), (3, 2), (4, 1), (6, 1), (7, 1), (8, 1)]

cnt = Counter({1:3,2:4})
deduct = {1:1, 2:2}
cnt.subtract(deduct)## deducts elements count using that argument
print(cnt)
##O/PCounter({1: 2, 2: 2})

#--------------------------------------------------------------------------------------------------
     #----Defaultdict---------

from collections import defaultdict ##calling defaultdict

nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])##In a normal dictionary, this will force a KeyError.
# But defaultdict initialize the new key with default_factory's default value which is 0 for int.
##O/P 0
count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] +=1## ach item in the list is added to the defaultdict named as count and initialized to 0 based on default_factory. If the
# same element is encountered again, as loop continues, count of that element will be incremented.
print(count)##O/P {'Mike': 5, 'John': 3, 'Anna': 2, 'Britney': 1, 'Smith': 2})


#--------------------------------------------------------------------------------------------------
     #----ordereddict---------

from collections import OrderedDict

od = OrderedDict()## ordered dictonary is a dictonary where key maintains the order in which they are insurted
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)##O/P OrderedDict([('a', 1), ('b', 2), ('c', 3)])

for key, value in od.items():##accessing each element using loop
    print(key, value)##o/P a 1, b 2, c 3

list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(list)
od = OrderedDict(cnt.most_common())##sorting using number of counts
for key, value in od.items():##items() method is used to return the list with all dictionary keys with values.
    print(key, value)##o/p a 4,c 3,b 2

#--------------------------------------------------------------------------------------------------
     #----deque---------

from collections import deque
list = ["a","b","c"]
deq = deque(list)
print(deq)##o/p deque(['a', 'b', 'c'])

deq.append("d")## you can add elements both right and left side of a deque(list)
deq.appendleft("e")
print(deq)##o/p deque(['e', 'a', 'b', 'c', 'd'])

deq.pop()##removing elements from deque
deq.popleft()
print(deq)##deque(['a', 'b', 'c'])
print(deq.clear())##clearing deque

list = ["a","b","c"]
deq = deque(list)
print(deq.count("a"))##counting elements in deque

#--------------------------------------------------------------------------------------------------
     #----chainmap---------

from collections import ChainMap
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)##combine several dictionaries ##o/p [{'b': 2, 'a': 1}, {'c': 3, 'b': 4}]
print(chain_map['a'])##o/p 1

dict2['c'] = 5##ChainMap updates its values when its associated dictionaries are updated
print(chain_map.maps)
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print (list(chain_map.keys()))
print (list(chain_map.values()))##getting keys and values in chain_map##o/p ['b', 'a', 'c'] [2, 1, 3]

dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)##adding dictonary to exisisting
print(new_chain_map)##o/p ChainMap({'f': 6, 'e': 5}, {'a': 1, 'b': 2}, {'b': 4, 'c': 3})


#--------------------------------------------------------------------------------------------------
     #----namedtupple---------
from collections import namedtuple
from collections import namedtuple

Student = namedtuple('Student', 'fname, lname, age')## returns a tuple with names for each position in the tuple
s1 = Student('John', 'Clarke', '13')
print(s1.fname)##   Student(fname='John', lname='Clarke', age='13')
s2 = Student._make(['Adam','joe','18'])##_make create a namedtuple instance with a list
print(s2)
s2 = s1._asdict()##Create a New Instance Using Existing Instance
print(s2)##OrderedDict([('fname', 'John'), ('lname', 'Clarke'), ('age', '13')])


s2 = s1._replace(age='14')##Changing Field Values with _replace() Function
print(s1)##Student(fname='John', lname='Clarke', age='13')
print(s2)##Student(fname='John', lname='Clarke', age='14')





