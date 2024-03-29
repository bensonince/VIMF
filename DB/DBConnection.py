#IMPORT modules section
import mysql.connector
from dictionaries import *
from classes import *
from mysql.connector import Error

#Establish DB connection with error checking and writes but doesn't commit or close
def db_add_tweet(tweet1):
    try:
        # tweet1.read_tweet()
        connection = mysql.connector.connect(**connection_config_dict)
        if connection.is_connected():
            c = connection.cursor()
        #SQL Connection and retrieval to variables here

    except Error as e :
        print ("Error while connecting to MySQL:", e)
    finally:
        #closing database connection.
        if(connection.is_connected()):
            c.close()
            connection.close()

#Establish DB connection with error checking and writes but doesn't commit or close
def db_add_tweet(tweet1):
    try:
        # tweet1.read_tweet()
        connection = mysql.connector.connect(**connection_config_dict)
        if connection.is_connected():
            c = connection.cursor()
            #Write information to file
            c.execute("INSERT INTO tweets (time, username, tweet) VALUES(%s, %s, %s)",
                (tweet1.time,tweet1.author,tweet1.tweet))
            connection.commit()
            return c.lastrowid

    except Error as e :
        print ("Error while connecting to MySQL:", e)
    finally:
        #closing database connection.
        if(connection.is_connected()):
            c.close()
            connection.close()

def db_read_tweet(ID = 0, author = "N/A", inTweet = "unimportant"):
    try:
        connection = mysql.connector.connect(**connection_config_dict)
        if connection.is_connected():
            c = connection.cursor()
            sql_select_statement = """SELECT * FROM tweets WHERE ID = %s OR username = %s OR tweet = %s"""
            c.execute(sql_select_statement, (ID, author, inTweet ))
            row = c.fetchone()
            if not row :
                return 0
            tweet1 = row[1], row[2], row[3]
            return tweet1 #row[1], row[2], row[3] # tweet1
    except Error as e :
        print ("Error while connecting to MySQL:", e)
    finally:
        #closing database connection.
        if(connection.is_connected()):
            c.close()
            connection.close()
