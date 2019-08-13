class TxtStringify(object):

	def __init__(self):

		self.__special_characters = ['.',',',';',':','"','!','#','?','"',
		'@','_','-','[',']','{','}','%','©','+','-','=','*','&','/','º',
		'ª','”','“','(',')', "$", "—", '–', '…', "'", '¬', '°', '²', '³', '>', 
		'‘', '’']

		self.__numbers = [str(n) for n in range(0,10)]

	def special_char_ovewrite(character_list):

		"""

		Receives a list to overwrite the special character list used to clean the text

		"""

		if type(character_list) is list:
			self.__special_characters = character_list

		else:

			return False


	def __get_file_data(self, file_path, lines=False):

		try:

			file = open(file_path, 'r')

			if lines:

				text = file.readlines()

			else:

				text = file.read()

			file.close()

			return text

		except:

			return False

	def raw_lines(self, file_path):

		"""
		
		It returns the list of the lines of the file

		"""

		text = self.__get_file_data(file_path, lines=True)

		if text:

			return text

		else:

			return False

	def raw_text(self, file_path):

		"""

		It returns a string with the text of the file

		"""

		text = self.__get_file_data(file_path)

		if text:

			return text

		else:

			return False

	def text(self, file_path):

		"""

		It returns a string with the text of the file without
		linebreaks

		"""

		if self.raw_lines(file_path):

			lines = self.raw_lines(file_path)
			newlines = [l.rstrip('\n') for l in lines]
			nospacelines = [l for l in newlines if l != '']
			text = ' '.join(nospacelines)

			return text

		else:

			return False

	def clean_text(self, file_path, 
		nospecial=False, nonumbers=False, nospaces=False, lower=False, upper=False):

		"""
		It returnes the text with treatement according to the parameters
		bellow:

		(remove special characters and ponctuation)
		nospecial = True

		(remove numbers)
		nonumbers = True

		(remove spaces)
		nospaces = True

		(make lower case)
		lower = True

		(make uppercase)
		upper = True

		If no parameter is assigned, it returns the same as text()

		"""

		if self.text(file_path):

			text = self.text(file_path)
			cleantxt = text

			if nospecial:
				
				cleantxt = [t for t in text if t not in self.__special_characters]
				cleantxt = ''.join(cleantxt)
				text = cleantxt				

			if nonumbers:
				
				temp = ""
				for s in text:
					if s not in self.__numbers:
						temp += s

				cleantxt = text = temp 

			if nospaces:
			
				cleantxt = cleantxt.replace(" ","")


			if lower:

				cleantxt = cleantxt.lower()

			if upper:
				
				cleantxt = cleantxt.upper()

			return cleantxt

		else:

			return False

txtstringify = TxtStringify()