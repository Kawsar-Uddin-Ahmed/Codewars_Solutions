import difflib

from string import ascii_lowercase,ascii_uppercase

#here maketrans() is used because to change from one to another example : maketrans(from , to).one by one alphabet

def scoobydoo(villian, villians):
    tbl = str.maketrans(ascii_lowercase + ascii_uppercase, (ascii_lowercase[5:] + ascii_lowercase[:5]) * 2)  # THis is used for shifting letter 5 house front(example: a->f)
    villian = villian.replace(" ","")
    villian = villian[-6::-1] + villian[:-6:-1]
    new_villian = ""
    for i , v in enumerate(villian): #i = index number and v is the alphabet of the string
        if i % 2 == 0:
            new_villian+=v
            #print("new-villian1 = ",new_villian)
        else:
            new_villian+=v.translate(tbl)
            #print("new-villian2 = ", new_villian)
    villian = new_villian
    print(villian)

    return difflib.get_close_matches(villian,villians,n=1)[0] #returns a list of close matched strings
    #difflib in Python is used for comparing sequences and calculating similarity, primarily for comparing text files or strings
    #difflib.get_close_matches(the_string,the_array,n=maximum_number_of_the_matched_string_return)[index_number_of_list]


villians = ["Black Knights","Puppet Master","Ghost Clowner","Witch Doctors","Waxed Phantom","Manor Phantom","Ghost Bigfoot","Haunted Horse","Davy Crockett","Captain Injun","Greens Gloobs","Ghostly Manor","Netty Crabbes","King Katazuma","Gators Ghouls","Headless Jack","Mambas Wambas","Medicines Man","Demon Sharker","Kelpy Monster","Gramps Vamper","Phantom Racer","Skeletons Men","Moon Monsters"]

a = scoobydoo("oyhxtdwnrjtx",villians)
print(a)


#!!!!!!!!!!!!!!!!!!!!!!!Another Code !!!!!!!!!!!!!!!!!!!!!!!!!!#
b = "ndcddzmiahsz"
#c = "zshaimzddcdn"
print(b[-6::-1]) # from 6th to last
print(b[::-1]) #reverse print
print(b[:-6:-1]) #from 0th to 5th position
print(b[:-1]) #only last one.
print(b[-6:]) #only last 6 characters
print(b[:-6]) #First 6 characters

fromm = ascii_lowercase + ascii_uppercase
print(fromm)
too = (ascii_lowercase[5:] + ascii_lowercase[:5]) * 2
print(too)
abl = str.maketrans(ascii_lowercase + ascii_uppercase, (ascii_lowercase[5:] + ascii_lowercase[:5]) * 2)
v = "a"
print(v.translate(abl)) # v will act as from and than it will translate it to .

maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ","fghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcde")