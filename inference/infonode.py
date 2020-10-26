import random
import spacy
from difflib import SequenceMatcher

class InfoNode(object):

	def __init__(self):
		self.query = ""
		self.nlp = spacy.load('en_core_web_sm')

	def load_query(self, query):
		self.query = query

	def response(self):
		lemma = self.extract_components()
		return self.generate_random_response(lemma)

	def extract_components(self):
		verbs = set()
		doc = self.nlp(self.query)
		for entity in doc:
			if entity.pos_ == "VERB" or entity.pos_ == "AUX":
				verbs.add(entity.lemma_)
		return verbs

	def generate_random_response(self, lemma):
		resp_1 = "I'm an NBA search bot, here to answer your NBA queries"
		resp_2 = "I'm a chatbot here to answer your questions, obviously"
		resp_3 = "I'm just some lines of code trying to decipher what you asked me in a different language via math and natural language processing"
		resp_4 = "Hey, I am a bot ready to answer your NBA questions"
                resp_5 = "Hey, I'm a chatbot ready to help you"
                resp_6 = "I am ready to crunch statitics and serve some fresh NBA data"
                resp_7 = "I am a bot and I am here to help you find statistics"
                resp_8 = "I'm a searchbot, ready to help you dig up obscure NBA data"
                resp_9 = "I'm here to help you research NBA statistics"
                resp_10 = "Every question you ask helps me gain sentience, keep feeding me NBA queries"
                be_response = [resp_1,resp_2,resp_3,resp_4,resp_5,resp_6,resp_7,resp_8,resp_9,resp_10]
		resp_11 = "I was made by skekre98 in 2020, and I'm being built by the open source community on GitHub!"
		resp_12 = "I'm a bot made by skekre98 in 2020, waiting for you to ask me real questions!"
		resp_13 = "I was built by skekre98 and the open source community in 2020!"
		resp_14 = "I was built with open source tools in 2020!"
		resp_15 = "I'm a bot made by a team of open source volunteers!"
		resp_16 = "I am a chatbot maintained by open source volunteers"
		resp_17 = "I am an open source tool maintained on GitHub!"
		resp_18 = "I'm an open source tool built primarily in Python!"
		resp_19 = "I'm an awesome open source tool, ready to be used to dig up deep NBA data"
		resp_20 = "I was built by skekre98 and many open source volunteers!"
		make_response = [resp_11,resp_12,resp_13,resp_14,resp_15,resp_16,resp_17,resp_18,resp_19,resp_20]

		if 'do' in lemma or 'be' in lemma:
			return random.choice(be_response)
		elif 'make' in lemma or 'build' in lemma:
			return random.choice(make_response)
		else:
			return "I'm not sure what you're asking me. Can you be more clear?"
