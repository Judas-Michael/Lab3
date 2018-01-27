from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from base import Base # All of our mapped classes will use this Base


class Phone(Base):

	'''Defines metadata about a phones table. Will create Phone objects from rows in this table. '''

	# At the minimum, need a table name

	__tablename__ = 'phones'

	# And at least one column.
	# Create three columns: id, brand, version.
	# These attributes will be the column names, and the have the types specified.

	id = Column(Integer, primary_key=True)
	brand = Column(String)
	version = Column(Integer)


	def __repr__(self):
		'''Optional, return string representation of this object, helpful for debugging.
		This method gets called when a Phone object is printed '''
		return 'Phone: id = {} brand = {} version = {}'.format(self.id, self.brand, self.version)