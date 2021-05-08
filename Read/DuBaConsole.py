import pyttsx3

import datetime,time,os

import news_rmrb

engine = pyttsx3.init()

#news_rmrb.main()

dir_ = os.listdir(".\\Data\\%s"%time.strftime('%Y%m%d' , time.localtime()))

def Main():

    run = True

    while run:

        print("Loding News Titles\n\n")

        for i in range(0,len(dir_)):

            print(i,dir_[i])

        try:

            cmd = input("Choose an article (just input a number!) :: ")

            try:
                
                int(cmd)

            except:

                print("Unsupported Type.Please input an INT.")

                continue

        except KeyboardInterrupt:

            print("Ctrl+c have been pressed.You sure to quit the program ?? ")

            if input("[Y/n] ") == "Y":

                print("Exiting...")
            
                run = False

            else:

                pass
            

        try:

            file = open(".\\Data\\%s\\%s"%(time.strftime('%Y%m%d' , time.localtime()),dir_[int(cmd)]),"r",encoding='utf-8')
            
            text = file.readlines()

            try:

                for i in text:

                    print(i)
                    
                    engine.say(i)

                    try:

                        engine.runAndWait()

                    except RuntimeError:

                        print("[Error] An Error Happens With The App.\nWe Have No Way To Fix This Problem.\nRESTART THE PROGRAM May Help.\nError Code : RuntimeError")

                        #print("Python Gaves out RuntimeError.")

                        run = False

                        continue
                    
            except KeyboardInterrupt:

                print("Stop playing.")

                continue

        except IndexError:

            print("Sorry,Wrong command.")

            continue

Main()

input("Press Enter To Exit...")
