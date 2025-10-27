from faker import Faker
import random 

def generate_random_paragraphs(max_sentence_length=50):
    fake = Faker()
    Faker.seed()  # You can set a seed for reproducibility

    paragraphs = ""

    while True:
	    paragraph = fake.paragraph(nb_sentences=random.randint(3, 6), variable_nb_sentences=True)
	    paragraph = str(paragraph)

	    if len(paragraphs) < target_length:
	        paragraphs = paragraphs + paragraph
	    elif len(paragraphs) > target_length:
	    	paragraphs = paragraphs[:-2]
	    elif len(paragraphs) == target_length:
		    return paragraphs

target_length = 10000
random_paragraph = generate_random_paragraphs(1)
print(random_paragraph)
