MAXCHAR  = 100

class URLify:
    
    def urlify(self, str):
        str = str.strip()
        i = len(str)-1
        if i>MAXCHAR:
            return -1 
        # Make a stripped format of list
        arrList = list(str)
        # print(arrList)
        spaceCount = 0
        for space in arrList : 
            if space == ' ':
                spaceCount+=1
        # print(spaceCount)
        newIndex = i + 2*spaceCount
        # print(newIndex)
        for item in range(i-2,newIndex-2):
            arrList.append('0')
        # print(arrList)
        for j in range(i-1,0,-1):
            if arrList[j] == ' ':
               arrList[newIndex] = '0'
               arrList[newIndex-1] = '2'
               arrList[newIndex-2] = '%'
               newIndex = newIndex-3
            else : 
                arrList[newIndex] = arrList[j]
                newIndex-=1
        return "".join(arrList)  
if __name__ == '__main__':
    obj = URLify()

    str = 'Mr John Smith  '
    print(obj.urlify(str))
