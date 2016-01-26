import copy
import sys
class Queen8:
	tableSize=8
	alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#queue contendra tuplas, una tabla que representa el estado y un indice que representa
#el nivel, este va de 0 a 7
	queue=[]
	stack=[]
	contador=0

	def __init__(self):
		table=self.blankTable()
		self.display(table)
		self.generate(table,self.contador)
		while len(self.queue)!=0:
			tablat=self.queue[0][0]
			indice=self.queue[0][1]
			self.queue.remove(self.queue[0])
			if indice+1 <8:
				self.generate(tablat,indice+1)

	#Create an empty table
	def blankTable(self):
		table = []
		for row in xrange(self.tableSize):
			new = []
			for col in xrange(self.tableSize):
				new.append(0);
			table.append(new)
		return table

	def display(self, table):
		cad=""
		for x in range(self.tableSize):
			cad = cad + self.alphabet[x]
		print cad

		for x in range(self.tableSize):
			print table[x]
		print ""

	def generate(self, table, contador):
		actualRow=table[contador]
		for x in range(self.tableSize):
			if actualRow[x]==0:
				#copiamos la tabla
				#asignamos en la posicion disponible un 1 e invalidamos las necesarias
				tableTemp=copy.deepcopy(table)
				tableTemp=self.invalidarPosiciones(tableTemp,contador,x)
				#self.showTable(tableTemp)
				#print ""
				self.queue.append((tableTemp,contador))
				if contador == 7:
					self.showTable(tableTemp)
					sys.exit()
		#print self.queue[0]

	def showTable(self, table):
		for x in range (self.tableSize):
			print table[x]

	def invalidarPosiciones(self, table, row, column):
		#primero invalidamos las posiciones de las columnas y renglones donde fue colocada la reyna
		for x in range(self.tableSize):
			table[row][x]=2
			table[x][column]=2
		#aumentar i y j mientras ambos sean menor a 8
		row2= row
		column2= column
		while (row2 < 7 and column2 < 7) :
			column2 = column2+1
			row2 = row2+1
			table[row2][column2]=2

		#decrementar i y j mientras ambos sean mayor a 0
		row2= row
		column2= column
		while (row2 > 0 and column2 > 0) :
			column2 = column2-1
			row2 = row2-1
			table[row2][column2]=2
		
		#aumentar j y decrementar i mientras j<8 e i>0
		row2= row
		column2= column
		while (row2 > 0 and column2 < 7) :
			column2 = column2+1
			row2 = row2-1
			table[row2][column2]=2
		
		#aumentar i y decrementar j mientras j>0 e i<7
		row2= row
		column2= column
		while (row2 < 7 and column2 > 0) :
			column2 = column2-1
			row2 = row2+1
			table[row2][column2]=2

		table[row][column]=1	
		return table

def execute():
	q8 = Queen8()

execute()