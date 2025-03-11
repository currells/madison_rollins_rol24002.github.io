"""Using AI to describe an image and trying to get it to describe flowers in detail"""

#part one meta thingy megigger
"""
1. Cereate a main.py and subfolders with files with functions in them and import those funcitons in the main.py
2. recursion: looping wihtout loops, create a function which iterates a file link by line wihtout using while or for loops
3. integrate with AI create a simple commandline chat box which interferes with an llm allow it to work with immages."""

#importing Ollama
import ollama

#using the llava formula code and edditing the message content heavily
res = ollama.chat(
	model="llava",
    settings={
        'temperature': 0.7
    },
	messages=[
		{
			'role': 'user',
			
            #Botanical books are used for their definitions of flowers, petals, stamen, etc.
            #dictionaries uesed: Davesgarden.com, Britannica.com, 
            'content': """
            Describe the flower petals in detail.

            Petal definition:  in flowering plants, a sterile floral part that usually functions as a visually conspicuous 
            element of a flower. Petals are modified leaves and are often brightly coloured to attract specific pollinators to 
            the flower. Petals often come in multiples of three in monocots or in multiples of four or five in eudicots. 
            Many horticultural flowers, such as roses and peonies, have been bred to have multiple layers of petals, resulting
            in showy textured blooms.  Petals are located on the inner whorls of a flower, typically surrounded by the reproductive
            organs of the plant.

            The description of the petals should be limited to the following and be concise:
                Describe the shape of the petals, round, pointed, long, short, etc.
                Describe the color of the petals, red, blue, yellow, etc.
                Describe the size of the petals, small, large, etc.
                Describe the texture of the petals, smooth, rough, etc.
                Describe the pattern of the petals, solid, striped, etc.
                Describe the number of petals, one, two, three, etc.
            """, 


			'images': ['./flower-2.jpg']
		}
	]
)

print(res['message']['content'])