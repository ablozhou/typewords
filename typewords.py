# coding=UTF-8
import random
import excel
import time
from colorama import init, Fore#, Style # Back

class TypeWords:
    help_cmds={"/help":"相关命令帮助", "/exit":"退出","/choose":"选类别,[99]为全部","/next":"下一个类别"}
    params = {"exit":False, "type":99}
    sheetnames={}

    def __init__(self):
        
        self.points = 0
        self.dicts={}
        # get words
        self.words = excel.ReadExcel('words.xlsx')
        self.cmds={"/help":self.help_print, "/choose":self.choose_types,"/exit":self.exit,
        "/next":self.next_type}

    def next_type(self):
        if self.params["type"]==99 or self.params["type"]>=len(self.sheetnames):
            self.params["type"] = 0
        else:
            self.params["type"] += 1
        
        self.dicts = self.words.read_data(self.params["type"])

    def choose_types(self):
        self.sheetnames=self.words.sheet_names()
        print()
        print("选择要练习的类别索引，[99] 为全部:\n")
        for key in self.sheetnames:
            print(key,self.sheetnames[key])
        i=input("选择要练习的类别索引，[99] 为全部:\n")
        if len(i) == 0 or not i.isdigit() or int(i)<0 or int(i)>=len(self.sheetnames):
            self.params["type"]=99
        else:
            self.params["type"]=int(i)
        
        self.dicts = self.words.read_data(self.params["type"])

    def help_print(self):
        print("打字练习，小学英语单词版. 输入[/exit]结束练习. 负分将结束. ") 
        print("Author: Andy zhou<ablozhou@gmail.com> 2021")
        print("命令列表：")
        print("-"*10)
        for key in self.help_cmds:
            print("%s: %s"%(key,self.help_cmds[key]))
        print("-"*10)

    def exit(self):
        print("End of practice, exit ...")
        self.params["exit"] = True

    # 选择练习类别
    def process_cmds(self,cmd):
        if cmd in self.cmds.keys():
            self.cmds[cmd]()
        else:
            print("Wrong cmds:",cmd)

    def practise(self):
        
        self.help_print()
        self.choose_types()

        while not self.params["exit"]:
            time.sleep(1)
            word = random.sample(list(self.dicts.keys()), 1)[0]  # 随机一个字典中的key，第二个参数为限制个数
            leng = len(word)
            print()
            print(Fore.CYAN+"---points: %d---" % (self.points, ))
            print(Fore.WHITE+self.dicts[word])
            print(Fore.GREEN)
            print(word)
            print(Fore.YELLOW, end="")
            ans = input()
            # print(Fore.RESET)
            if len(ans) >0 and ans[0]=="/":
                
                self.process_cmds(ans)
                continue
            
            if ans == word:
                self.points += leng
                #print(Fore.WHITE+"---%d---\n%s\n" % (self.points, self.dicts[ans]))
            else:
                self.points -= leng
                print("Try again... %d\n" % self.points)
                if self.points <= 0:
                    print(Fore.RED+"GAME OVER!!! Your have not enough points!")
                    input("Type any key to exit...")
                    print(Fore.RESET+"")
                    break


if __name__ == '__main__':
    init()
    t = TypeWords()
    t.practise()