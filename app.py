print("Title of program: CCA Matching Personality test")
print()
print("Welcome to DHS! Please answer the following questions truthfully and we'll suggest a CCA which might be suitable for you!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

tech1 = input("I enjoy building and fixing things.")

outdoor1 = input("I'll go crazy if I do not go out of the house for the whole day.")

music1 = input("I can see colours in my mind when i hear music.")

tech2 = input("I know how to build apps and websites.")

outdoor2 = input("I'm good with tying knots and ropes.")

music2 = input("I play a musical instrument well.")

tech3 = input("I enjoy creating artworks when I am free.")

outdoor3 = input("I have experiene in partcipating in art competitions.")

music3 = input("I can see shapes and colours everywhere I go.")

tech4 = input("I listen to chinese music often.")

outdoor4 = input("I feel calm and relaxed when I listen to an orchestra play music.")

music4 = input("I hope to be part of an orchestra.")

tech5 = input("I like watching plays and dramas.")

outdoor5 = input("I enjoy conversing with others in mandarin.")

music5 = input("I like working with props, music and lights backstage.")


tech_final = int(tech1) + int(tech2) + int(tech3)
outdoor_final = int(outdoor1) + int(outdoor2) + int(outdoor3)
music_final = int(music1) + int(music2) + int(music3)

print()

if tech_final > outdoor_final and tech_final > music_final:
  print("You might be suitable for Infocomm club!")
if outdoor_final > music_final:
  print("You might be stuiable for ODAC!")
if music_final > outdoor_final:
  print("You might be suitable for Band!")
if tech_final == outdoor_final :
  print("You might be suitable for Art Club!")
if outdoor_final == tech_final or outdoor_final == music_final: 
  print("You might be suitable for Chinese Orchestra!")
if music_final > tech_final and music_final > outdoor_final: 
  print("You might be suitable for Chinese Drama!")
