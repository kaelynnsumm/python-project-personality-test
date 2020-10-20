print("Title of programme: Y1 CCA Matching Personality test")
print()
print("Welcome to DHS! Please answer the following questions truthfully and we'll suggest a CCA which might be suitable for you!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

tech1 = input("I enjoy building and fixing things.")

outdoor1 = input("I'll feel frustrated if I do not go out of the house for the whole day.")

music1 = input("I can see colours in my mind when i hear music.")

tech2 = input("I know how to build apps and websites.")

outdoor2 = input("I'm good with tying knots and ropes.")

music2 = input("I know how to play a musical instrument and plays it well.")

tech3 = input("I enjoy attending computing workshops outside the school curriculum.")

outdoor3 = input("I have experiene in partcipating in sports competitions.")

music3 = input("I often go for music concerts.")

tech4 = input("I help my teachers and classmates fix technological problems in school.")

outdoor4 = input("I feel calm and relaxed when I participate in outdoor activities.")

music4 = input("I hope to be part of an orchestra.")

tech5 = input("I find working on technology fun and engaging.")

outdoor5 = input("I enjoy conversing with others in mandarin.")

music5 = input("I like performing music in front of a large audience and receive their applause after the performance.")


tech_final = int(tech1) + int(tech2) + int(tech3)
outdoor_final = int(outdoor1) + int(outdoor2) + int(outdoor3)
music_final = int(music1) + int(music2) + int(music3)

print()

if tech_final > outdoor_final and tech_final > music_final:
  print("You might be suitable for Infocomm club or Robotics Club!")
elif outdoor_final > music_final:
  print("You might be stuiable for sports CCA such as ODAC!")
else:
  print("You might be suitable for Performing Arts CCA such as Chinese Orchestra, Symphonic Band, String Ensemble and Guzheng Ensemble!")
