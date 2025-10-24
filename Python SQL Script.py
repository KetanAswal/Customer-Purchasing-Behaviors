import mysql.connector as mysql # for used mysql code in python
import  pandas as pd # for access xlsx or csv format and send in to database

mydb=mysql.connect(host="localhost",
                   user="root",
                   password="123456789",
                 #  database="myproject4"
                   )

mycode=mydb.cursor() # this line because i dont need for write mydb.cursor() too many time

#for create our database in sql
mycode.execute("create database MyDatabase") 

#for use or access the databse
mycode.execute("use MyDatabase")

#for create table. remember table name is ditto exact in which data you take
mycode.execute("create table MyData(" \
"CustomerID int Primary Key,"
"Age int," \
"Gender char(1)," \
"ItemPurchased varchar(20)," \
"Category varchar(20)," \
"Location varchar(20)," \
"Purchase_Amount_In_USD int," \
"Size varchar(2)," \
"Color varchar(20)," \
"Season varchar(20)," \
"ReviewRating decimal(2,1)," \
"SubscriptionStatus varchar(3)," \
"ShippingType varchar(20)," \
"DiscountApplied varchar(3)," \
"PromoCodeUsed varchar(3)," \
"PreviousPurchases int," \
"PaymentMethod varchar(20)," \
"FrequencyOfPurchases varchar(20))")

#here we used pandase for read the data and store in df variable
df=pd.read_csv("shopping_behavior_updated.csv")

#here we runs the loop for inserted the data one by one 
for _, row in df.iterrows():
    sql="insert into MyData(" \
    "CustomerID,Age,Gender,ItemPurchased,Category,Location,Purchase_Amount_In_USD,Size," \
    "Color,Season,ReviewRating,SubscriptionStatus,ShippingType,DiscountApplied," \
    "PromoCodeUsed,PreviousPurchases,PaymentMethod,FrequencyOfPurchases" \
    ") values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    values=(row['CustomerID'],
            row['Age'],
            row['Gender'],
            row['ItemPurchased'],
            row['Category'],
            row['Location'],
            row['Purchase_Amount_In_USD'],
            row['Size'],
            row['Color'],
            row['Season'],
            row['ReviewRating'],
            row['SubscriptionStatus'],
            row['ShippingType'],
            row['DiscountApplied'],
            row['PromoCodeUsed'],
            row['PreviousPurchases'],
            row['PaymentMethod'],
            row['FrequencyOfPurchases']
            )
    
    #for exectute the data
    mycode.execute(sql,values)

#commint used as a confirmation for the above process
mydb.commit()

#here our codes is end
mycode.close()

#here our database is closed
mydb.close()

print("Data inserted sucessfully")


'''
for insert the new data create the new csv file and store there new data with same exact old files heading
now 
df=pd.read_csv("shopping_behavior_updated.csv")
in this line
df=pd.read_csv("new_csv_data.csv")
and then same runs the code

note:- create database  and create table runs first time when you want to create
but if they already created so just comment out them  

'''