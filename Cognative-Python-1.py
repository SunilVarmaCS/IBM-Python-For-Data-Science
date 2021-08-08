# First Program

# Types
 
print(11)
print(type(12))
print(type(12.00))
print(type("asea"))

print(int(12.00))

#print(int("A")) :: -- Value Error

print(bool(1))
print(bool(0))

print(True)
print(False)

print((10+20)*20)

#Variables

Your_Name = 100
print(Your_Name)

total_min = 43 + 42 + 57
total_hr = total_min / 60
print(total_hr)
print(int(total_hr))

# Strings Contains Two and One Quotes :

String_Name = "Robert Saverin"

print(String_Name[1:])
print(String_Name[2:4])
print(String_Name[0:4])
print(String_Name[-1:-2])
print(String_Name[-5:-2])

#String Stride : 2 Indicates Every Second Variable

print(String_Name[::2])
print(String_Name[0:2:2])

print(len(String_Name))

New_Value = (String_Name + "is the Co - Founder of Xyz Company")
print(New_Value)

print(3*String_Name)
#print(10*New_Value)

# \ - backslash ::

print("New \nline")

print(New_Value.upper())
print(New_Value.lower())

#Replace Method

Name = String_Name
New_Name = Name.replace("Robert","Eduardo")

print(New_Name)

# Find Method 

print(New_Name.find("Ed"))

# Tuples

First_Tuple = ("New",10,20,[100.22,2])
print(type(First_Tuple))

print(First_Tuple)

print(First_Tuple[3:4])

#Length of a Tuple 

print(len(First_Tuple))

# Sorted Numbers 

Numbers = (12,11,23,32,122,10,12,34,9,90)
print(sorted(Numbers))

# Nesting Process in Tuple 

Nesting = (10,(12.2,20,89),(12,34,"Icon"),"tear","ea",(12,1))
print(Nesting[0:])
print(len(Nesting))

print(Nesting[1][0:3])
print(Nesting[5][0:2])

# Lists 

Test = [10, 20, [12.0], ("Jack Dorsey")]
print(Test)
print(type(Test))

print(len(Test))
print(Test[0:3])

New_Test = Test+["Adding_ME",New_Name]
print(New_Test)

#New_Tuple = Test + ("Add_Me",New_Name)
#print(New_Tuple) --- > Error Message to Concatenate Tuple

NewL = ["acer",12]
print(NewL)

Rew = NewL.append(12)
print(NewL)

Rew = NewL.extend("obj")
print(NewL)

Rew = "Car".split()
print(Rew)

# List Aliasing

Friends = ["Pavan and Keyan are Good Friends"]
New_Friends = ["Pavan and Keyan","are Good Friends"]
Friends = New_Friends
print(New_Friends)
print(Friends)

Friends[1]="are Bed Friends"
print(Friends)

# Try Alising in Tuple 

Rahul = ("Mayan and Rahul are Good Friends")
print(type(Rahul))

print(Rahul)

old = Rahul.replace("Good","Bed")#("Mayan","Aman")
print(old)

#help(Test)

#Sets are in Curly Brackets

New_Set = {"Amazon","Google","Google","Facebook","Tesla"}
print(New_Set)

#Type Casting

#New_St = (set(Test))
#print(New_St)

Jams = ["Jka","Aka",12,11,234]
Jams_set = (set(Jams))
print(Jams_set)
print(type(Jams_set))

#Add and Remove Method

Set_1 = {"New Add on", "New Break Line", "Compound Line"}
Set_1.add("Easy to Understand")
print(Set_1)

Set_1.remove("New Add on")
print(Set_1)

#"in" Method

print("Hardwork" in Set_1)
print("Compound Line" in Set_1)

#Overlapping in Sets

Overlap_1 = {"Education","Motel","Subdomain","Top Level Domain","SubSet"}
Overlap_2 = {"Helthcare","Hotel","Subdomain","Center","SubSet","Excellent"}

Overlap_3 = (Overlap_1 & Overlap_2)
print(Overlap_3)

#Union of The Set

print(Overlap_1.union(Overlap_2))

#SubSet of Venn Diagram

print(Overlap_3.issubset(Overlap_1))
print(Overlap_3.issubset(Overlap_2))

#Python Dictionaries :
Dic_1 = {"Gujarat":"Ahmedabad","Maharashtra":"Mumbai","Bihar":"Patna","UP":"Lucknow"}
print(type(Dic_1))

print(Dic_1)

#Define a Value in Dictionary
print(Dic_1["Bihar"])
print(Dic_1["Maharashtra"])

#Add a New Value in Dictionary
Dic_1 ["Maharashtra"]="Puna"
print(Dic_1)

Dic_1 ["Oppo"]="Vivo"
print(Dic_1)

#Del a Value in Dictionary
del(Dic_1["Bihar"])

print(Dic_1)

#in Command Dictionary : True and False

print("Mumbai" in Dic_1)
print("Puna" in Dic_1)
print("Gujarat" in Dic_1)

#See Keys and Values in Dictionaries :

print(Dic_1.keys())
print(Dic_1.values())

#Conditions and Branching

# ----------------- > NEXT ----------.............














