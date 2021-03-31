from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(db_name=r'Book.sqlite', table_name='Book')

'''
Hotel(hotelNo, hotelName, hotelType, hotelAddress, hotelCity, numRoom)
Room(roomNo, hotelNo, roomPrice)
Booking(bookingNo, hotelNo, guestNo, checkIn, checkOut, totalGuest, roomNo)
Guest(guestNo, firstName, lastName, guestAddress)
'''

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS Hotel(hotelNo integer(5),hotelName VARCHAR(10),hotelType VARCHAR(10),'
    'hotelAddress VARCHAR(20),hotelCity VARCHAR(10),numRoom integer(5),PRIMARY KEY(hotelNo))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS Room(roomNo integer(5),hotelNo integer(5),'
    'roomPrice integer(10),PRIMARY KEY(roomNo))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS Booking(bookingNo integer(5),hotelNo integer(5),'
    'guestNo integer(10),checkIn VARCHAR(10),checkOut VARCHAR(10),totalGuest integer(5),'
    'roomNo integer(5))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS Guest(guestNo integer(5),firstName VARCHAR(10),'
    'lastName VARCHAR(10),guestAddress VARCHAR(20))')

SQL.close()
