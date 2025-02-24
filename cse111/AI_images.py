"""1Cereate a main.py and subfolders with files with functions in them and import those funcitons in the main.py
2. recursion: looping wihtout loops, create a function which iterates a file link by line wihtout using while or for loops
3. integrate with AI create a simple commandline chat box which interferes with an llm allow it to work with immages."""

import ollama

res = ollama.chat(
	model="llava",
	messages=[
		{
			'role': 'user',
			'content': """Describe this image specifically the shirt they are wearing and 
            tell me the hexcode of the shirts color""", 
			'images': ['./babymads.jpg']
		}
	]
)

print(res['message']['content'])