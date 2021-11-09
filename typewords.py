import random
import excel
import time


def type_words():
    print("打字练习，小学英语单词版. 输入[exit]结束练习.")
    count = 0
    # get words
    words = excel.ReadExcel('words.xlsx')
    dicts = words.read_data()
    while True:
        time.sleep(1)
        word = random.sample(dicts.keys(), 1)[0]  # 随机一个字典中的key，第二个参数为限制个数
        leng = len(word)
        word += "\n"
        ans = input(word)

        if ans == "exit":
            print("game exited!!!")
            break

        if ans == word[:-1]:
            count += leng
            print("---%d---\n%s\n" % (count, dicts[ans]))
        else:
            count -= leng
            print("do better. %d\n" % count)
            if count < 0:
                print("您已没分,game over!!!")
                break


if __name__ == '__main__':
    type_words()