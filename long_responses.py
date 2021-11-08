import random

R_EATING = "I don't like eating anything because I am a bot obviously."

def unknown():
	response = ['Could you please re-phrase that?',
				"...",
				"Sound about right",
				"what does that mean?"][random.randrange(4)]
	return response

