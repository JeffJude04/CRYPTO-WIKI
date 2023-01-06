from PIL import Image
import sys
import mysql.connector as mys
from getpass import getpass
from tabulate import tabulate   


def m_menu():
    while(True):
        print("-----------------WELCOME TO THE WEBSITE--------------")
        print("----PLEASE CONFIRM AUTHENTICATION TO GAIN FULL ACCESS TO THE APP-----")
        first()

def menu():
    while(True):
        print("welcome to the ledger!!!!")
        print("----new to crypto and trading?? check out or new begginers profile below----")
        print("1.access ledger?")
        print("2.View Portfolio")
        print("3.Head to Main Page")
        ch=int(input("Enter your choice"))
        if ch==1:
            ledger()
        elif ch==2:
            portfolio()
        elif ch==3:
            main_page()
        else:
            print("Wrong input")
def first():
    try:
        print("---------------------------------------------------------------------")
        print("------------welcome to user authentication-------------")
        print("----Enter valid details for successfull authentication----")
        con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
        mycursor=con.cursor()
        EMAIL=input("enter your Email id")
        NAME=input("enter your full name")
        PASSWD=int(input("enter your password"))

        a="insert into first values('{}','{}','{}')".format(EMAIL,NAME,PASSWD)

        mycursor.execute(a)
        con.commit()
        print(" LOGIN SUCCESSFULL ")
        print(" READY TO ACCESS LEDGER")
        
    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close()
        dashboard()    
def ledger():
    while(True):
        print("1.start transactions")
        print("2.view transactions")
        print("3.check current databases")
        ch=int(input("enter your choice"))
        if ch==1:
            st_transactions()
        elif ch==2:
            vi_transactions()
        elif ch==3:
            databases()
        else:
            print("Wrong options,choose again")
def st_transactions():
    while (True):
        print("1.buy")
        print("2.sell")
        ch=int(input("enter your choice"))
        if ch==1:
            buy()
        elif ch==2:
            sell()
        else:
            print("wrong choice")
            transactions()
def buy():
    while(True):
        print("1.do you want to check crypto trends")
        print("2.move to buy phase")
        ch=input("yes or no")
        if ch=="yes":
            crypto_db()
        elif ch=="no":
            buy_phase()
        else:
            print("choose again")
            buy()
def crypto_db():
    try:
        con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
        mycursor=con.cursor()

        
        sql="select * from cryptodb"
        mycursor.execute(sql)
        data=mycursor.fetchall()
        print(tabulate(data,headers=['NAME','PRICE','SELLPRICE','UNITSSOLD'],tablefmt='fancy_grid'))


    except Exception as e:
            print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close() 

def buy_phase():
    print("what type of crypto would you like to buy")
    int(input("enter the id of a crypto you would like to buy"))
    con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
    mycursor=con.cursor()
    NO=int(input("enter the unique number"))
    q="select * from cryp_buy where NO={}".format(NO)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    print("would you like to buy??")
    ch=input("yes or no?")
    if ch== "yes":
        print("purchase successful")
    elif ch==no:
        print("purchase unsuccessful")
    else:
        print("check your dashboard and collection for the updated list")
    if con.is_connected():
        mycursor.close()
        con.close()

def sell():
    print("do you want to open your personal collection?")
    ch=input("enter yes or no")
    if ch==yes:
        collection1()
    elif ch==no:
        crypto_db()

def collection1():
    try:
        con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
        mycursor=con.cursor()
        USERIDNO=int(input("enter the specific number"))
        q="select * from ppage where USERIDNO={}".format(USERIDNO)
        mycursor.execute(q)
        rows=mycursor.fetchall()

        
    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close() 
    sell_ad()
        
def sell_ad():
    ch=int(input("enter the unique id of your crypto chain"))
    mycon=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
    mycursor=mycon.cursor()
    USERID=int(input("enter the employee  number"))
    sql="delete from ppage where UIDNO={}".format(USERID)
    mycursor.execute(sql)
    mycon.commit()
    print("all sold items have been sold at market rates please check dashboard for further confirmation")
    print("              The chain has been sold            ")
    print("          Thank you for using our platform       ")
    if con.is_connected():
        mycursor.close()
        con.close()
    

    
        
def vi_transactions():
   try:
        con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
        mycursor=con.cursor()
        NO=int(input("enter the transaction_number"))
        q="select * from transaction where NO={}".format(NO)
        mycursor.execute(q)
        rows=mycursor.fetchall()
   except Exception as e:
            print(e)
   finally:
       if con.is_connected():
           mycursor.close()
           con.close()      

def worktodo():
    print("Would you like to login:")
    print("Enter your email (@gmail)")
    con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
    mycursor=con.cursor()
    EMAIL=input("enter your name")
    PHNO=int(input("enter your phone number"))
    OTHERS=input("enter any miscellanious data")

    a="insert into ledger values('{}','{}','{}')".format(EMAIL,PHNO,OTHERS)

    mycursor.execute(a)
    con.commit()
    print("  ")
    print(" you have been successfully logged in")
    print("thank you for logging in")
    main()


def toolkit():
    print("This is a popular crypto toolkit used for begginers")
    print("all credits to github @(svrenkata9)")
    print("https://github.com/intel/crypto-api-toolkit")



def main_page():
    print("--- welcome to the main page---")
    while(True):
        print("1.access your personal page")
        print("2.explore the trends")
        print("3.biggest losses and wins of the day")
        print("4.access begginers toolkit")
        print("5.back to dashboard")
        print("6.customer service")
        ch=int(input("enter your choice:"))
        if ch==1:
            perso_page()
        elif ch==2:
            trends()
        elif ch==3:
            lo_wins()
        elif ch==4:
            begginerssection()
        elif ch==5:
            dashboard()
        elif ch==6:
            customer_service()
        else:
            print("wrong option")

def customer_service():
    try:
        print("welcome to immediate access customer service")
        print("since the website deals with sensitive topics you will be responded to quickly")
        print("dial the immeddiate customer service helpline @78999021112")
        mycursor.execute(q)
        rows=mycursor.fetchall()

    except Exception as e:
            print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close() 
def databases():
    print("These are the current Trends")
    print("TOP 10 TRENDS FOR TODAY")
    con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
    mycursor=con.cursor()
    NO=int(input("enter the page number"))
    q="select * from trends where TNO={}".format(TNO)
    mycursor.execute(q)
    rows=mycursor.fetchall()
    if con.is_connected():
        mycursor.close()
        con.close()


def begginerssection():
    while(True):
        print("welcome to the begginers guide")
        print("1.FAQ's")
        print("2.Begginers toolkit")
        print("3.Blog report")
        ch=int(input("enter your choice"))
        if ch==1:
            faq()
        elif ch==2:
            toolkit()
        elif ch==3:
            report()
        else:
            print("wrong option")
            begginerssection()
def faq():
    print("What are cryptocurrencies?")
    print("This is a seemingly simple question, but since most people answer about what they think, hope, or want cryptocurrencies to be, it is a confusing one. Cryptocurrencies are a digital asset that started as a medium of exchange for people to buy goods and services. Over time, their functionality has expanded")
    print("_______________") 
    print("This is a seemingly simple question, but since most people answer about what they think, hope, or want cryptocurrencies to be, it is a confusing one. Cryptocurrencies are a digital asset that started as a medium of exchange for people to buy goods and services. Over time, their functionality has expanded")
    print("Cryptocurrency value can be pegged to underlying asset such as U.S. dollar, central bank digital currencies, privacy coins (senders and receivers are anonymous), governance tokens (gives owners the right to vote in decisions regarding blockchain’s future development), utility tokens, and non-fungible tokens (distinct characteristics from all others). This is from a developer/development side. Of course, there are also investors and speculators who are hoping for appreciation. It is very important you know the intent and functionality of cryptocurrency you own or are considering owning.")
    print("_______________")
    print(" How are cryptocurrency transactions recorded?")  
    print("Cryptocurrency transactions are recorded on a shared, digital ledger called a blockchain. This is decentralized technology, spread across many computers, that records every transaction")
    print("_______________")
    print("Are blockchain and cryptocurrencies the same?")
    print("No. Blockchain is the technology that allows for cryptocurrencies to work. It is a decentralized and digital ledger of transactions used for cryptocurrencies and other assets/functions. It is important to separate the technology behind cryptocurrencies from the actual cryptocurrencies.")
    print("_______________")
    print(" What are the top cryptocurrencies? ")
    print("The most popular and widely heard of cryptocurrency is Bitcoin. As of early January 2021, the total cryptocurrency market is over $1 trillion, and Bitcoin is around $700 billion. Believe it or not, there are over 7,800 cryptocurrencies in existence and growing. The top five, with over 80 percent of the market value, are Bitcoin, Ethereum, XRP, Tether, and Litecoin.")
    print("_______________")
    print("Why are there so many cryptocurrencies? ")
    print("People saw the success of Bitcoin and tried to improve existing functionality and provide new functionality with new cryptocurrencies. Additionally, investors and developers were certainly trying to make money")
    print("_______________")
    print(" I hear cryptocurrencies are used for illicit/illegal activities; is this true?")
    print("Since cryptocurrency operates on a decentralized network that lacks a central authority, it is possible to exchange cryptocurrency without registering an identity. Yes, since the start there have been criminal activities with cryptocurrencies. However, the blockchain publicly records every transaction, and while names are not assigned to addresses, you can trace activity back to a crypto exchange, which knows the end user. The estimates vary for how many transactions are for illegal activities and proponents of cryptocurrency point to illegal activity with traditional currencies")
    

def blogreport():
    print("Blog report for the day")
    print("---thr rise of crypto currency in buisness")
    print("More than 2,300 US businesses accept bitcoin, according to one estimate from late 2020, and that doesn’t include bitcoin ATMs. An increasing number of companies worldwide are using bitcoin and other digital assets for a host of investment, operational, and transactional purposes.")
    print("The use of crypto for conducting business presents a host of opportunities and challenges. As with any frontier, there are both unknown dangers and strong incentives. That’s why companies venturing to use crypto in their businesses should have two things:")
    print("a clear understanding of why they are undertaking that action and a list of the many questions they should consider.")
    print("This paper endeavors to provide you and your company with an overview of the kinds of questions and insights enterprises should consider as they determine whether and how to use crypto. So, if your company plans to participate in crypto, it’s important to think ahead,")
    print("Crypto may provide access to new demographic groups. Users often represent a more cutting-edge clientele that values transparency in their transactions. One recent study found that up to 40% of customers who pay with crypto are new customers of the company, and their purchase amounts are twice those of credit card users.")
    print("introducing crypto now may help spur internal awareness in your company about this new technology. It also may help position the company in this important emerging space for a future that could include central bank digital currencies.")
    print("Crypto could enable access to new capital and liquidity pools through traditional investments that have been tokenized, as well as to new asset classes.")      
    print("Crypto furnishes certain options that are simply not available with fiat currency. For example, programmable money can enable real-time and accurate revenue-sharing while enhancing transparency to facilitate back-office reconciliation.")
    print("More companies are finding that important clients and vendors want to engage by using crypto. Consequently, your business may need to be positioned to receive and disburse crypto to assure smooth exchanges with key stakeholders.")
    print("Crypto may serve as an effective alternative or balancing asset to cash, which may depreciate over time due to inflation. Crypto is an investable asset, and some, such as bitcoin, have performed exceedingly well over the past five years. There are, of course, clear volatility risks that need to be thoughtfully considered.")
    print("hence we can conclude by saying crypto plays an important role in the finance of may companies in the present and possible future")
    
def toolkit():
    print("This is a popular crypto toolkit used for begginers")
    print("all credits to github @(svrenkata9)")
    print("https://github.com/intel/crypto-api-toolkit")
    


def main_page():
    print("--- welcome to the main page---")
    while(True):
        print("1.access your personal page")
        print("2.explore the trends")
        print("3.biggest losses and wins of the day")
        print("4.access begginers toolkit")
        print("5.back to dashboard")
        print("6.customer service")
        ch=int(input("enter your choice:"))
        if ch==1:
            perso_page()
        elif ch==2:
            trends()
        elif ch==3:
            lo_wins()
        elif ch==4:
            begginerssection()
        elif ch==5:
            dashboard()
        elif ch==6:
            customer_service()
        else:
            print("wrong option")
            
def perso_page():
    try:
        con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
        mycursor=con.cursor()
        EMPNO=int(input("enter the USERID"))
        q="select * from ppage where USERID={}".format(USERID)
        mycursor.execute(q)
        rows=mycursor.fetchall()

        
    except Exception as e:
        print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close()   

def trends():
    print("crypto trends for the day")
    try:
        img  = Image.open(path) 
    except IOError:
        pass
    
    
    
def customer_service():
    print("welcome to immediate access customer service")
    print("since the website deals with sensitive topics you will be responded to quickly")
    print("dial the immeddiate customer service helpline @78999021112")
    

def dashboard():
    print("welcome to  your dashboard")
    print("1.access ledger?")
    print("2.view markets")
    print("3.view field")
    print("4.view derivatives")
    ch=int(input("enter an option"))
    if ch==1:
        ledger()
    elif ch==2:
        markets()
    elif ch==3:
        field()
    elif ch==4:
        derivatives()
    else:
        print("wrong input")


def markets():
    print("market status as of this minute")
    try:
        con=mys.connect(host="localhost",user="root",passwd="jeffjude",database="crypto")
        mycursor=con.cursor()

        
        sql="select * from markets"
        mycursor.execute(sql)
        data=mycursor.fetchall()
        print(tabulate(data,headers=[''],tablefmt='fancy_grid'))


    except Exception as e:
            print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close()
def fields():
    while (True):
        print("1.take out loans in cash format")
        print("2.access digital card")
        print("3.Gift cards")
        ch=int(input("enter your loan amount"))
        if ch==1:
            loan()
        elif ch==2:
            card()
        elif ch==3:
            gift()
        else:
            print("wrong input")
def loan():
    print("enter your bank details")
    NUM=int(input("enter your loan amount:"))
    phno=int(input("enter your phone number"))
    print("details will be validated and our employee will be in contact soon")
    
def gift():
    print("press here to download instant gift card")
    

def card():
    print("use E card instant payments??")
    print("tap your phone on the device to complete transaction")


def derivatives():
    print("welcome to the deriivatives page")
    while (True):
        print("1.future_overview")
        print("2.view leaderboard")
        ch=int(input("enter the option"))
        if ch==1:
            overview()
        elif ch==2:
            leaderboard()
        else:
            print("wrong option")

def future_overview():
    print("bitcoin and crypto have fallen off a cliff in recent times but there remains hope that more can be done in the future to fully digitalise the system we as a company hope to asssist with that process in our never ending journey to make online transactions intereting, affordable and safe")

def leaderboard():
    try:
        con=mys.connect(host="localhost",user="root",passwd="jeffjudev",database="crypto")
        mycursor=con.cursor()

        
        sql="select * from leaderboard"
        mycursor.execute(sql)
        data=mycursor.fetchall()
        print(tabulate(data,headers=['NAME','TREND','PROFIT'],tablefmt='fancy_grid'))


    except Exception as e:
            print(e)
    finally:
        if con.is_connected():
            mycursor.close()
            con.close()
    
m_menu()    
