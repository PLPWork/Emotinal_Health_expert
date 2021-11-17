import socket
import pandas as pd
import bert_question_copy

def main():
    print("Starting server on the port 6001...")
    #load context data
    df=pd.read_csv("C:/Users/verma/Documents/GitHub/Sem4PLPPrj/Main_code/TelegramBot-PizzaOrderBot-master/Depression.txt",sep="\t")
    text=df
    s = socket.socket()
    host = socket.gethostname()
    port = 6001
    s.bind((host,port))
    s.listen(5)
    while True:
        print("waiting for connection accepted")
        c, addr = s.accept()
        print("Connection accepted from " + repr(addr[1]))
        while True:
            try:
                qb=c.recv(1026)
                que = qb.decode("utf-8", "ignore") 
                print("que from the user:", que)
                #invoke BERT for ans
                ans = bert_question_copy.question_answer(que, text)
                print("sending ans from BERT", ans)
                c.send(ans)
            except:
                print("connection is closed.")
                c.close()
                break 

main()