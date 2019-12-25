class TxtStringify(object):

	def __init__(self):

		self.__special_characters = ['.',',',';',':','"','!','#','?','"',
		'@','_','-','[',']','{','}','%','©','+','-','=','*','&','/','º',
		'ª','”','“','(',')', "$", "—", '–', '…', "'", '¬', '°', '²', '³', '>', 
		'‘', '’']
		self.__numbers = [str(n) for n in range(0,10)]
		self.__english_stopwords = list()
		self.__portuguese_stopwords = list()
		self.__load_english_stopwords()
		self.__load_portuguese_stopwords()


	def special_char_overwrite(character_list):

		"""

		Receives a list defining the special characters list used for cleaning the text
		used on some functions of this class

		If no list is provided, it is used a default list

		"""

		if type(character_list) is list:

			self.__special_characters = character_list

		return


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

			return


	def __load_english_stopwords(self):


		english_file = open("./TxtStringify/english_stopwords.txt", "r")
		english_lines = english_file.readlines()

		for line in english_lines:

			self.__english_stopwords.append(line.rstrip('\n'))

		english_file.close()


	def __load_portuguese_stopwords(self):

		portuguese_file = open("./TxtStringify/portuguese_stopwords.txt", "r")
		portuguese_lines = portuguese_file.readlines()

		for line in portuguese_lines:

			self.__portuguese_stopwords.append(line.rstrip('\n'))

		portuguese_file.close()


	def __remove_english_stopwords(self, text):
		
		words = text.split()
		new_words = [word for word in words if word not in self.__english_stopwords]
		new_text = ' '.join(new_words)

		return new_text



	def __remove_portuguese_stopwords(self, text):
		
		words = text.split()
		new_words = list()
		new_words = [word for word in words if word not in self.__portuguese_stopwords]
		new_text = ' '.join(new_words)

		return new_text



	def raw_lines(self, file_path, linebreaks=True):

		"""
		
		It returns the list of the lines of the file

		Set linebreaks=False to remove the linebreaks from the lines

		"""
		lines = self.__get_file_data(file_path, lines=True)

		if linebreaks:

			if lines:

				return lines

		else:

			cleaned_lines = [l.rstrip('\n') for l in lines]

			if cleaned_lines:

				return cleaned_lines

		return


	def raw_text(self, file_path):

		"""

		It returns a string with the text of the file

		"""

		text = self.__get_file_data(file_path)

		if text:

			return text

		return


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

		return 


	def clean_text(self, file_path, 
		nospecial=False, nonumbers=False, nospaces=False, lower=False, upper=False, nostopwords=False):

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

		(remove stopwords)
		nostopwords = "english"

		or 

		nostopwords = "portuguese"

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

			if nostopwords == "portuguese":

				cleantxt = self.__remove_portuguese_stopwords(cleantxt)

			if nostopwords == "english":

				cleantxt = self.__remove_english_stopwords(cleantxt)

			return cleantxt

		return

txtstringify = TxtStringify()