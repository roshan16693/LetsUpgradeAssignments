                                             # Lists

list=["Roshan",1993,123,[12.36,1,4]]
print(list)
print(list[1])
print(list[3][2])
list.append("Its Append")
print("Appending Value",list)
list.pop()
print("Popping Value",list)
print("Getting Count of Element",list.count(123))
list.remove(1993)
print("Removing Value with Specific name",list)
print("Printing Index Value",list.index(123))
list.insert(1,"new")
print("Inserting New Value",list)

lst=[4,6,8,9,7,5,1,3,2]
lst.sort()
print("Sorting A List",lst)
lst.extend(list)
print("Extending list with other list",lst)
newlist=lst.copy()
print("Copying old value of list to new one",newlist)
lst.reverse()
print("Reversing values",lst)
lst.clear()
print("Emptied the whole list",lst)

# ---------------------------------------------------------------------------------------------------------------

                                        # Tuples


tup=(1,2,"Roshan","Facebook",23.5,True,2)
print("Printing Index of 2",tup.index(2))
print("Counting Element 2 in tuple",tup.count(2))

# ---------------------------------------------------------------------------------------------------------------


                                        # Sets

set1={2,5,6,7,100,3}
set2={2,"Roshan",4,5,2}
set3=set1.copy()
set4=set3.copy()
set5=set1.copy()
print("Printing Set3 Which is a replica of set1",set3)
set3.remove(2)
print("Remove an element of set",set3)
print("Checking if set2 is a subset of set1",set2.issubset(set1))
print("Checking if set1 is a superset of set2",set1.issuperset(set2))
print("Union of Set1 and Set2",set1.union(set2))
print("Checking if set1 is a Disjoint of set2",set1.isdisjoint(set2))
print("Checking Values of set1 which is not present in set2",set1.difference(set2))
set1.difference_update(set2)
print("The difference which is there in set1 is updated to set1",set1)
print("Prints the elements which are not matching in both sets",set1.symmetric_difference(set3))
set4.symmetric_difference_update(set1)
print("The difference which is there in set1 is updated to set4",set4)
print("Intersection Only matching values",set1.intersection(set3))
set5.intersection_update(set1)
print("Intersection Update",set5)
set5.discard(3)
print("Discarding element 3 of set5",set5)
set5.add(150)
print("Adding Element element 150 to set5",set5)
set5.pop()
print("Deleting element from start",set5)
set5.update(set4)
print("Merging data of set4 to set5",set5)
print("Clearing data ",set5.clear())

# ---------------------------------------------------------------------------------------------------------------
                                         #Dictionaries

users_username={"roshan":"roshan1@123",
                "Manish":"Manish@123",
                "vikas":"vikas1@123",
                "joel":"joel1@123"}

print("\nStarting dictionaries\n")
print("Printing all the values of dictionary",users_username.values())
print("Printing all the keys of dictionary",users_username.keys())
print("Printing all the key and value pairs of dictionary",users_username.items())
print("Updating value of a key",users_username.update(joel="joel@123"))
print("Getting the email id of specific user",users_username.get("joel"))
new_user={}.fromkeys(["name","bio","password"],"unknown")
print("New user keys with specific values with fromkeys function",new_user)
print("delete the bio key",new_user.pop("bio"))
print("delete the last pair",new_user.popitem())
print("delete the whole dict",new_user.clear())
print(users_username)

# ---------------------------------------------------------------------------------------------------------------

                                        # Strings

Strings=" "
print("\nStarting Strings\n")
print("Counting repeating letters",Strings.count("l"))
print("getting index of letter specified",Strings.index("e"))
print("Capitalizing string",Strings.upper())
print("Casefolding string",Strings.casefold())
print("Replacing string",Strings.replace("Hello","New Hello"))
print("Checking Starting of  string",Strings.startswith("Hello"))
print("Checking Ending of string",Strings.endswith("World"))
print("Can split string with , or space or any of string",Strings.split())
print("finding a character in string",Strings.find("o"))
print("Checking if its alpha ",Strings.isalpha())
print("Checking if its alpha numeric",Strings.isalnum())
print("Checking if String is ascii characters",Strings.isascii())
print("Checks whether there is a character in the string or not.",Strings.isspace())
print("There are many more functions")
