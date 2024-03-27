TCP Protocol : 

How to Progrqmming a Basic TCP protocol For Server and Client 

    Basic File Contain The Code of the Basic TCP  Client and Server  

Sending Large Data 

      How To send a large Data Over TCP protocol with more reliable sending 

            By Using :
                1- sendall()  { Bulid in } method in python and recvall() method that bulid by the user 
                2- Defind a new Function that split the data into a small pacies and sending it by implement for loop to send
                    all data 

Deadlook 

        sometimes there is an Deadlock occurs when u send a Big Data :  
        In the modified codes, the client sends a chunk of data and then waits
        for the server to send a confirmation back (in this case, ACK) before 
        continuing. The server, upon receiving data, sends back this confirmation 
        immediately. 
        This confirmation can also be used by the client to check if the server has
        received the data and is ready for more. The client then shuts down its side
        of the socket for writing (SHUT_WR) to signal the end of data transmission.


OSAMA ALHROUB 
