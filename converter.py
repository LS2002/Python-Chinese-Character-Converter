# -*- coding: utf-8 -*-

# maximized match
def conv(string,dic):
    i = 0
    while i < len(string):
        for j in range(len(string) - i, 0, -1):
            if string[i:][:j] in dic:
                t = dic[string[i:][:j]]
                string = string[:i] + t + string[i:][j:]
                i += len(t) - 1
                break
        i += 1
    return string
 
# generate dict
def mdic():    
    table = open('ZhConversion.php','r').readlines()
    dic = dict()
    name = []
    for line in table:
        if line[0] == '$':
            #print line.split()[0][1:]
            name.append(dic)
            dic = dict()
        if line[0] == "'":
            word = line.split("'")
            dic[word[1]] = word[3]
    name[3].update(name[1]) # SC to TC: zh2Hant + zh2TW
    name[4].update(name[1]) # SC to TC: zh2Hant + zh2HK
    name[5].update(name[2]) # TC to SC: zh2Hans + zh2CN
    return name[3],name[4],name[5]
 

def main():
    resultfile = open('ExtractedSimplifiedChineseCharacters.txt','wa')
    with open('TabDilimitedCSV.csv','r') as f:
        for line in f:
            simplifiedstr = line.split('\t')[4] #change this index to the one corresponding to CSV columns
            resultfile.write(conv(simplifiedstr,dic_CN)+'\n')
    newf.close

if __name__=="__main__":

    [dic_TW,dic_HK,dic_CN] = mdic()
    main()
