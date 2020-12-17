from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(r'StudentSystemData.sqlite', table_name='StudentSystem')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS Account('
    'PersonnelNumber VARCHAR(20) PRIMARY KEY ,'
    'Password VARCHAR(20))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS PersonnelDetail('
    'PersonnelNumber VARCHAR(20) PRIMARY KEY ,'
    'PersonnelName VARCHAR(20),'
    'EnrollYear VARCHAR(10))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS LessonDetail('
    'LessonCode VARCHAR (10) PRIMARY KEY ,'
    'PersonnelNumber VARCHAR(20),'
    'LessonName VARCHAR (20),'
    'LessonCredit VARCHAR (5),'
    'LessonProfessor VARCHAR (20),'
    'LessonType VARCHAR (3),'
    'Semester VARCHAR (5))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS LessonContent('
    'LessonCode VARCHAR(20) PRIMARY KEY ,'
    'LessonName VARCHAR(20),'
    'LessonContent VARCHAR(3000),'
    'Semester VARCHAR (5))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS LessonGrade('
    'LessonCode VARCHAR(20) PRIMARY KEY ,'
    'PersonnelNumber VARCHAR(20),'
    'Grade VARCHAR(3000),'
    'Semester VARCHAR(5),'
    'LessonProfessor VARCHAR(20))')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS PersonnelAccess('
    'PersonnelNumber VARCHAR(20) PRIMARY KEY ,'
    'Access VARCHAR(10))')

SQL.close()
