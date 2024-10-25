import sys
import time
# run this on your cmd . when you call it , give it parameters
def main():
    if len(sys.argv)==1:
        print("you have to enter a parameter")
    elif len(sys.argv)==2:

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        user_input = sys.argv[1]
        string_current = ""
        count :int =0
        while not string_current==user_input:
            for i in range(32,124):
                if count<len(user_input) and chr(i) == user_input[count]:
                    string_current = string_current+chr(i)
                    count=count+1
                    print(string_current)
                    break
                else:
                    print(string_current+chr(i))
                time.sleep(0.007)
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        inputs:str =""
        for user_input in sys.argv:
            if user_input=="main.py":
                continue
            else:
                string_current = ""
                count :int =0
                while not string_current==user_input:
                    for i in range(32,124):
                        if count<len(user_input) and chr(i) == user_input[count]:
                            string_current = string_current+chr(i)
                            count=count+1
                            print(inputs+" "+string_current)
                            break
                        else:
                            print(inputs+" "+string_current+chr(i))
                        time.sleep(0.007)
                inputs = inputs +" "+string_current




if __name__=="__main__":
    main()