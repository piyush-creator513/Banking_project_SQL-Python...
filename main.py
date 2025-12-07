from connection import get_connection
def super_admin():
    conn=get_connection()
    obj=conn.cursor()

    id=input("enter ID")
    user_pwd=input("Enter password:")

    correct_data=obj.execute("select * from superadmin where sid=?",(id))
    s=correct_data.fetchone()

    
    if s.spwd==user_pwd:
        print("you are correct")
        print("1. create admin 2. change password")
        ch=int(input("enter your choice"))
        if ch==1:
           aid=(input("enter admin id"))
           apwd=(input("enter admin pasword"))
           obj.execute("INSERT INTO admin (aid, apwd, sid) VALUES (?, ?, ?)", (aid, apwd, "super1"))
           obj.commit()

        # obj.execute("insert into admin values aid=?,apwd=?,sid=?",(aid,apwd,"super1"))
        conn.commit()
        if ch==2:
           new_pwd=input("enter new password")
           obj.execute("update superadmin set spwd=? where sid=?",(new_pwd,id))
           obj.commit()


    else:
        print("Wrong id or password")





    
    
def admin():
     conn=get_connection()
     obj=conn.cursor()

     id=input("enter ID")
     user_pwd=input("Enter password:")

     correct_data=obj.execute("select * from admin where aid=?",(id))
     s=correct_data.fetchone()

    
     if s.apwd==user_pwd:
    
        print("you are welcome")

        print("1.create a branch  2.create a employee  3.transfer employee  4.change password")

        ch=int(input("enter your choice"))

        if ch==1:
            bid=input("enter your branch id: ")
            name=input("enter your branch name:")
            city=input("enter your branch city: ")

            bcontact=input("enter your branch contact: ")

            bmail=input("enter your branch email: ")

            obj.execute("insert into branches values(?,?,?,?,?)", (bid,name,city,bcontact,bmail))

            obj.commit()

        elif ch==2:
            eid=input("Enter employee id ")
            ename=input("Enter employee name ")
            mob=input("Enter employee mobile")
            mail=input("Enter employee mail")
            sal=input("Enter employee sal")
            post=input("Enter employee post")
            bid=input("Enter employee bid")
            add=input("Enter employee add")

            obj.execute("insert into employee values (?,?,?,?,?,?,?,?)",(eid,ename,mob,mail,add,sal,post,bid))
            obj.commit()

        elif ch==3:
            eid = input("Enter employee ID to transfer: ")
            new_bid = input("Enter new branch ID: ")

            # Check if employee exists
            obj.execute("SELECT * FROM employee WHERE eid = ?", (eid,))
            emp = obj.fetchone()

        
        
            # Update branch
            obj.execute("UPDATE employee SET bid = ? WHERE eid = ?", (new_bid, eid))
            conn.commit()
            print("✔ Employee transferred successfully!")
            

        elif ch==4:
            conn.commit()
            new_pwd=input("enter new password")
            obj.execute("update admin set apwd=? where aid=?",(new_pwd,id))
            obj.commit()
            print("✔ Password changed successfully!")
             

            

        else:
           print("Wrong id or password")
         
            
             
             
            

    
    
    
    
def employee():
     conn=get_connection()
     obj=conn.cursor()

     id=input("enter ID")
     user_pwd=input("Enter password:")



     
     print("1. create account")
     print("2. change password")
     ch=int(input("Enter your choice"))
     if ch==1:
         acno=input("enter account no")
         actype=input("enter account type")
         cid=input("enter customer id")
         bid=input("enter branch id")
         balance=0

         obj.execute("insert into account values (?,?,?,?,?)", (acno,actype,cid,bid,balance))
         obj.commit()

     
         
        
    
def customer():
    conn=get_connection()
    obj=conn.cursor()

    id=input("enter ID")
    user_pwd=input("Enter password:")

    
    print("1. Enter details to create account")
    print("2. deposite")
    print("3. withdraw")
    print("4. balance check")
    print("5. passbook print")


    ch=int(input("Enter your choice"))
    if ch==1:
        name=input("enter your name")
        mobile=input("Enter your mobile")
        mail=input("Enter your mail")
        address=input("Enter your address")
        aadhar=input("Enter your aadhar no")
        bid=input("Enter branch id")

        obj.execute("insert into Customer values (?,?,?,?,?,?)", (name, mobile, mail, address, aadhar,bid))
        obj.commit()

    elif ch == 2:
        acc_no=input("Enter account no ")
        amt=int(input("Enter amount "))


        obj.execute("insert into acc_transaction values (?,?,?)",(amt, 'credit',acc_no))

        correct_data = obj.execute("select * from account where acc_no=?", (acc_no))
        # print(correct_data)
        s = correct_data.fetchone()
        #print(s.balance)
        new_balance=s.balance+amt
        obj.execute("update account set balance=? where acc_no=?", (new_balance, acc_no))

        obj.commit()

    elif ch == 3:
        acc_no=input("Enter account no ")
        amt=int(input("Enter amount "))


        obj.execute("insert into acc_transaction values (?,?,?)",(amt, 'debit',acc_no))

        correct_data = obj.execute("select * from account where acc_no=?", (acc_no))
        # print(correct_data)
        s = correct_data.fetchone()
        #print(s.balance)
        new_balance=s.balance-amt
        obj.execute("update account set balance=? where acc_no=?", (new_balance, acc_no))

        obj.commit()

    elif ch == 4:
        acno = input("enter account no: ")

        correct_data = obj.execute("select balance from account where acc_no=?", (acno))
        s = correct_data.fetchone()

        print("your current balance is:",s.balance)

    elif ch == 5:
        acno = input("enter account no: ")

        print("\n------ PASSBOOK ------")

        # Fetch customer name and current balance
        acc = obj.execute("""
            select c.cname, a.balance
            from account a
            join customer c on a.cid = c.cid
            where a.acc_no = ?
         """, (acno,)).fetchone()

        if not acc:
            print("Account not found!")
            return

        print(f"Account No   : {acno}")
        print(f"Customer Name: {acc.cname}")
        print(f"Current Balance: ₹{acc.balance}\n")

        # Fetch all transactions
        trans = obj.execute("""
                            select tid, amount, amount_type
                            from transactions
                            where acc_no = ?
                            order by tid
                            """, (acno,)).fetchall()

        if not trans:
            print("No transactions found.")
            return

        print("TID   |   TYPE     |   AMOUNT")
        print("----------------------------------")
        for t in trans:
            print(f"{t.tid:<5} | {t.amount_type:<9} | ₹{t.amount}")

        print("----------------------------------")
    


while True:
   print(" 1. superadmin\n 2. admin\n 3. employe\n 4customer. ")
   choice= int(input("Enter your choice"))
    
    
   if choice==1:
        super_admin()
        
   elif choice==2:
        admin()
        
   elif choice==3:
        employee()
        
   elif choice==4:
        customer()
        
   else:
        print("enter a valid choice!")
