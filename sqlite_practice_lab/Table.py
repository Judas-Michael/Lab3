def main():

	import sqlite3

	sqlite_file = 'records_holders.sqlite'    # name of database file
	table_name1 = 'Records'  # name of the table to be created
	key_value = 'ID' 
	primary_key = 'primary_table' #table for primary key
	field_type1 = 'INT'  # column data type
	name_column1 = 'Chainsaw Juggling Record Holder' 
	field_type2 = 'TEXT'
	country_column1 = 'Country'
	amount_column1 = 'Number of catches'


	conn = sqlite3.connect(sqlite_file) #creates connection
	c = conn.cursor()

	# Creating a new SQLite table with 1 column
	c.execute('CREATE TABLE {tn} ({nf} {ft})'\
			.format(tn=table_name1, nf=key_value, ft=field_type1))

	# Creating a second table with 1 column and set it as PRIMARY KEY
	# note that PRIMARY KEY column must consist of unique values!
	c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
			.format(tn=primary_key, nf=key_value, ft=field_type1))
		
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\ #adds columns
			.format(tn=table_name1, cn=name_column1, ct=field_type2))
		
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
			.format(tn=table_name1, cn=country_column1, ct=field_type2))
		
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
			.format(tn=table_name1, cn=amount_column1, ct=field_type1))
	
	# Committing changes and closing the connection to the database file
	conn.commit()
	conn.close()



def insert_data():

	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	#add rows if needed
	
	key_insert = input("What key will you use?")
	name_insert = input("Catcher's name?")
	country_insert = input("Catcher's country?")
	catch_insert = input("What is their catch record?")

	try:
		c.execute("INSERT INTO {tn} ({idf}, {cn}, {cc}, {ac}) VALUES (key_insert, name_insert, country_insert, catch_insert)".\
			format(tn=table_name, idf=key_value, cn=name_column1, cc = country_column1, ac = amount_column1))
	except sqlite3.IntegrityError:
		print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
	
	conn.commit()
	conn.close()
	
def edit_data():
		conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	
	key_insert = input("What key will you edit?")
	name_insert = input("Catcher's name?")
	country_insert = input("Catcher's country?")
	catch_insert = input("What is their catch record?")
	
	c.execute("UPDATE {tn} SET {cn}=(name_insert), {cc} = (country_insert),{ac} = (catch_insert) WHERE {idf}=(key_insert)".\
        format(tn=table_name, cn=name_column1,cc = country_column1, ac = amount_column1, idf=key_value))
	
	conn.commit()
	conn.close()
	
def delete_data():
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	
	name_insert = input("What entry will you delete? (Name)")
	
	c.execute("UPDATE {tn} DELETE {cn}, {cc},{ac}, {idf}WHERE {cn}=(name_insert)".\
        format(tn=table_name, cn=name_column1,cc = country_column1, ac = amount_column1, idf=key_value))
	
	conn.commit()
	conn.close()
	
def search_data():
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	
	name_insert = input("What entry will you delete? (Name)")
	
	c.execute("UPDATE {tn} PRINT {cn}, {cc},{ac}, {idf}WHERE {cn}=(name_insert)".\
        format(tn=table_name, cn=name_column1,cc = country_column1, ac = amount_column1, idf=key_value))
	
	conn.commit()
	conn.close()

