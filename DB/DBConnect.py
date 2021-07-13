#IMPORT modules section
from mysql.connector import MySQLConnection, Error
from dictionaries import connection_config_dict
from classes import *

#Establish DB connection with error checking and run StoredProcedure to retrieve list of...
def db_list_vollys():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        cursor.callproc('sp_find_all_vollys') # need to get the Proc setup

        # print out the list of results
        for result in cursor.stored_results():
            print(result.fetchall())

            #Read example to class
            # c.execute(sql_select_statement, (ID, author, inTweet ))
            # row = c.fetchone()
            # if not row :
            #     return 0
            # tweet1 = row[1], row[2], row[3]

    except Error as e:
        print("An error has occured while connecting to your DB: ", e)

    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            conn.close()

#Establish DB connection with error checking and run StoredProcedure to retrieve list of...
def db_list_shift_vollys(shift_ID):
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        shift_vollys = cursor.callproc('sp_find_all_vollys_for_shift', shift_ID) # need to get the Proc setup

        #print(shift_vollys[1])

        # print out the list of results
        for result in shift_vollys
            print(result.fetchall())

    except Error as e:
        print("An error has occured while connecting to your DB: ", e)

    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            conn.close()

#Establish DB connection with error checking and run StoredProcedure to retrieve list of...
def db_read_volly(volly_ID):
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        volly = cursor.callproc('sp_find_volly', volly_ID) # need to get the Proc setup

        #print(shift_vollys[1])

    except Error as e:
        print("An error has occured while connecting to your DB: ", e)

    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            conn.close()

#Establish DB connection with error checking and run StoredProcedure to retrieve list of...
def db_list_shifts():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        cursor.callproc('sp_find_all_shifs') # need to get the Proc setup

        # print out the list of results
        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print("An error has occured while connecting to your DB: ", e)

    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            conn.close()

#Establish DB connection with error checking and run StoredProcedure to retrieve list of...
def db_list_volly_shifts(volly_ID):
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        shift_vollys = cursor.callproc('sp_find_all_shifts_for_volly', volly_ID) # need to get the Proc setup

        #print(shift_vollys[1])

        # print out the list of results
        for result in shift_vollys
            print(result.fetchall())

    except Error as e:
        print("An error has occured while connecting to your DB: ", e)

    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            conn.close()

#Establish DB connection with error checking and run StoredProcedure to retrieve list of...
def db_read_shift(shift_ID):
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        volly = cursor.callproc('sp_find_shift', shift_ID) # need to get the Proc setup

        #print(shift_vollys[1])

    except Error as e:
        print("An error has occured while connecting to your DB: ", e)

    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            conn.close()

#Establish DB connection with error checking and writes but doesn't commit or close
def db_add_volly(volly):
    try:
        # tweet1.read_tweet()
        connection = mysql.connector.connect(**connection_config_dict)
        if connection.is_connected():
            c = connection.cursor()
            #Write information to file
            c.execute("INSERT INTO tweets (time, username, tweet) VALUES(%s, %s, %s)",
            #this bit is the class variable of data passed to the Storepocedure when ready    (tweet1.time,tweet1.author,tweet1.tweet))
            connection.commit()
            return c.lastrowid

    except Error as e :
        print ("Error while connecting to MySQL:", e)
    finally:
        #closing database connection.
        if(connection.is_connected()):
            c.close()
            connection.close()
