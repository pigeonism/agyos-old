# wayne w 2015
# 6 letters long & must include letters only in values below
#keyword = "nisram" # osacue, the o and y just reflect
keyword = "eucaso" #"osacue"
#keyword= "cccccc"
# values, not all the alphabet - primes, +c cdhpr no.
values = ["a2", "b2", "c3", "d5", "e14", "f2", "g6", "h5", "i14", "k15", "l20", "m22", "n14","o8","p13","q20","r11","s8","t8","u15","x15","y15","z2"]

# 'wheel', use letter value to move clockwise through the wheel,
def move(letter, mode, val):
    #print val
    if mode == "row":
        newletter = ""
        index = 0
        # values can just be the wheel too
        for pair in values:
            if letter in pair:
                index = values.index(pair) + int(pair[1:])
                if (index > len(values)):
                    index -= len(values)
                newletter = values[index]
                newletter = newletter[0]
        return newletter
    if mode == "wheel": 
        #first letter is wheel letter, second is value.
        start = 0
        index = 0
        newletter = ""
        for pair in values:
            if letter in pair:
                start = values.index(pair)
        for pair in values:
            if val in pair:
                index = start + int(pair[1:])
        if (index > len(values)-1):
            index -= len(values)-1
	#print "index: ", index , " val passed to move: ", val, " top letter: ", letter
        newletter = values[index]
        newletter = newletter[0]
        return newletter
#print "wheel test\n"
#x=move("s")
#print x

def rev(word):
    temp = ""
    for i in range(len(word), 0, -1):
        temp += word[i-1]
    return temp
revkeyword = rev(keyword)

# keyword column, 36 letters - for the left row
leftcolumn = keyword + revkeyword + keyword + revkeyword + keyword + revkeyword

# build table; add keyword and top row. numbers will be str, just place holders
def get_table():
    xtable = []
    row = []
 
    for i in range(36): # 0-35
        row.append("*")

    for i in range(len(leftcolumn)):  
        xtable.append([leftcolumn[i]] + row[1:]) #first letter of keyword first

	

    return xtable

table = get_table()

#build final table, but first row seperate
def build(tbl):
    #row 0
    #print tbl[0]
    for i in range(1,len(tbl[0])):
        tbl[0][i] = move(tbl[0][i-1], "row", "") # the leftmost will have a letter, so change it

    #print tbl[0]	

    # now for the full thing, the one letter above is index of value to start, left is now how far	

    #print "\n"
    #print tbl

    for i in range(1,len(tbl)): # 1 to ignore first row 
        ##def move(letter, mode, val):
        for x in range(1, len(tbl[i])):
            tbl[i][x] = move( tbl[i-1][x], "wheel",tbl[i][x-1] ) # final param is left value
                
        #print "\n"
    return table	
soyga = build(table)

for row in soyga:
    print(row)
