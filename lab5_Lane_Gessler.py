# Lane Gessler Lab 5
# couldn't figure out bonus


def decode():
    
    text = str(input("text: "))
    string1 = ""
    sb2 = ""
    length = len(text)

    for substring in range(0,length):
        sb = text[substring : substring+1]
        #sb3 = text[substring : substring+2]

        #if sb3 == "uu" :
        #    sb2 = sb3.replace(sb3,"w ")
        #    string1 = string1 + sb2

        if sb == "l" :
            sb2 = sb.replace(sb,"t")
            string1 = string1 + sb2

        elif sb == "t" :
            sb2 = sb.replace(sb,"l")
            string1 = string1 + sb2

        elif sb == "8":
            sb2 = sb.replace(sb,"a")
            string1 = string1 + sb2
    
        elif sb == "b":
            sb2 = sb.replace(sb,"a")
            string1 = string1 + sb2
    
        elif sb == "a":
            sb2 = sb.replace(sb,"e")
            string1 = string1 + sb2   

        elif sb == "e":
            sb2 = sb.replace(sb,"b")
            string1 = string1 + sb2 

        else:
            string1 = string1 + sb
        
    return string1
    

string1 = decode()
print (string1)


