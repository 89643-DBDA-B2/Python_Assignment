key_dic = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a',
'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P',
'D':'Q', 'E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 'P':'C',
'Q':'D','R':'E', 'S':'F', 'T':'G','U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

input = 'Pnrfne pvcure V zhpu cersre Pnrfne fnynq'
input.replace("!","")

newstr = ""
lst_ofchars = []

# for val in input :
#     if val == " " :
#         lst_ofchars.append(" ")
#     else:
#         lst_ofchars.append(key_dic[val])

for val in input :
    if val == " " :
        newstr = newstr + " "
    else :
        newstr = newstr + key_dic[val]


print(f"The list of encoded string is {newstr}")

