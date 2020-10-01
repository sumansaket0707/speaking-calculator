def speak(str):
    

   from win32com.client import Dispatch
   speak=Dispatch("SAPI.spvoice")
   speak.Speak(str)
if __name__ == '__main__' :
    speak("so how u are doing yuvika vatsa5")
    speak("this calculator is designed by Mr saket suman in python programming")
    print("enter first no")
    speak("enter first number")
    a=int(input())
    print("enter second number")
    speak("enter second number")
    b=int(input())
    print("what do you want to perform? ,+,-,*,/ ")
    speak("what do u want to perform, addition, substraction, multiplication, or  division")
    c=input()
    if c=="+":

        d=a+b
        print(d)
        speak("your answer is")
        speak(d)
    elif c=="-":
         d=a-b
         print(d)
         speak("your answer is")
         speak(d)
    elif c=="*":
        d=a*b
        print(d)
        speak("your answer is")
        speak(d)
    elif c=="/":
        d=a/b

        print(d)
        speak("your answer is")
        speak(d)





