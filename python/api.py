from tkinter import *
from tkinter import font
import requests
from PIL import Image , ImageTk
import random

countryInfo = []
options = []
options_capital = []
options_population = []
options_area = []
flagImage = None

# Global variables to store country information
countryName = ""
capital = ""
population = ""
area = ""
continent = ""



def ApiCall():
     url="https://restcountries.com/v3.1/all"
     response = requests.get(url)
     data = response.json()
     return data

def showCountryInfo():
    try:
         global countryInfoData,options,options_capital
         countryData =ApiCall()                            
         randomNo=random.randint(0,len(countryData)+1)
         country=countryData[randomNo]
         countryName=country.get("name",{}).get("common","N/A")
         #Randomly select three country 
         incorrect_answers = random.sample(countryData,3)
         incorrect_names=[country.get("name",{}).get("common","N/A") for country in incorrect_answers]

         #combine the correct and incorrect answer
            
         options = [countryName] + incorrect_names
         
         random.shuffle(options)

         # Update the labels with the shuffled options

         for i in range(4):
             option_labels[i].config(text=options[i])
          
         countryInfo.append(countryName)

         capital=country.get("capital","N/A")[0] if "capital" in country else "N/A"
         countryInfo.append(capital)

          # Randomly select three incorrect capitals
         incorrect_answers_capital = random.sample(countryData, 3)
         incorrect_capitals = [country.get("capital", ["N/A"])[0] for country in incorrect_answers_capital]

         # Combine the correct and incorrect answers
         options_capital = [capital] + incorrect_capitals
         
         random.shuffle(options_capital)

         # Update the labels with the shuffled options
         for i in range(4):
             option_labels_capital[i].config(text=options[i])

         population=country.get("population","N/A")
         countryInfo.append(population)
         
         # Randomly select three incorrect populations
         incorrect_answers_population = random.sample(countryData, 3)
         incorrect_populations = [country.get("population", "N/A") for country in incorrect_answers_population]

        # Combine the correct and incorrect answers
         options_population = [population] + incorrect_populations

         random.shuffle(options_population)

        # Update the labels with the shuffled options
         for i in range(4):
            option_labels_population[i].config(text=options_population[i])

         area=country.get("area","N/A")
         countryInfo.append(area)

          # Randomly select three incorrect areas
         incorrect_answers_area = random.sample(countryData, 3)
         incorrect_areas = [country.get("area", "N/A") for country in incorrect_answers_area]

        #Combine the correct and incorrect answers
         options_area = [area] + incorrect_areas

         random.shuffle(options_area)

        #Update the labels with the shuffled options
         for i in range(4):
            option_labels_area[i].config(text=options_area[i])

         continent=country.get("region","N/A")
         countryInfo.append(continent)

         #Randomly select three incorrect continents
         incorrect_answers_continent = random.sample(countryData, 3)
         incorrect_continents = [country.get("region", "N/A") for country in incorrect_answers_continent]

         while continent in incorrect_continents:
               incorrect_answers_continent = random.sample(countryData, 3)
               incorrect_continents = [country.get("region", "N/A") for country in incorrect_answers_continent]

        #Combine the correct and incorrect answers
         options_continent = [continent] + incorrect_continents

         random.shuffle(options_continent)

        # Update the labels with the shuffled options
         for i in range(4):
            option_labels_continent[i].config(text=options_continent[i])

         splitList=[str(item).split(" , ") for item in map(str,countryInfo)]
         flattenedList =[item for sublist in splitList for item in sublist]
     
         flagUrl=country.get("flags",{}).get("png","N/A")
         if flagUrl !="N/A":
          flagImage=Image.open(requests.get(flagUrl , stream=True).raw)
          flagImage=ImageTk.PhotoImage(flagImage)
          flag_label.config(image=flagImage)
          flag_label.image = flagImage  



          label5.grid(row=7,column=0)
          label6.grid(row=8,column=0)
          label7.grid(row=9,column=0)
          label12.grid(row=12,column=0)
          label13.grid(row=13,column=0)
          label14.grid(row=14,column=0)
          label19.grid(row=0,column=6)
          label20.grid(row=0,column=8)
          label21.grid(row=1,column=6)
          label26.grid(row=4,column=6,padx=20)
          label27.grid(row=4,column=8,padx=20)
          label28.grid(row=6,column=6,padx=20)
          label33.grid(row=9,column=6)
          label34.grid(row=9,column=8)
          check_answers_button.grid(row=11, column=7)
      
    except Exception as e:
        print(f"An Error occurred : {e}")


def checkAnswers():
    try:
        # Check answers
        country_answer = label6.get()
        capital_answer = label13.get()
        population_answer = label20.get()
        area_answer = label27.get()
        continent_answer = label34.get()

         # Get correct names from the countryInfo list
        country_correct_name = countryInfo[0]
        capital_correct = countryInfo[1]
        population_correct = str(countryInfo[2])
        area_correct = str(countryInfo[3])
        continent_correct = countryInfo[4]

        # Create a new window for feedback
        feedback_window = Toplevel(root)
        feedback_window.title("GUI For Feedback")

        # Create labels and pack them into the feedback window
        feedback_label_country = Label(feedback_window, text=f"Country Name: {'Correct!' if country_answer.lower() == country_correct_name.lower() else f'Incorrect! Correct answer: {country_correct_name}'}", font=customFont)
        feedback_label_country.pack()

        feedback_label_capital = Label(feedback_window, text=f"Capital: {'Correct!' if capital_answer.lower() == capital_correct.lower() else f'Incorrect! Correct answer: {capital_correct}'}", font=customFont)
        feedback_label_capital.pack()

        feedback_label_population = Label(feedback_window, text=f"Population: {'Correct!' if str(population_answer).lower() == population_correct.lower() else f'Incorrect! Correct answer: {population_correct}'}", font=customFont)
        feedback_label_population.pack()

        feedback_label_area = Label(feedback_window, text=f"Area: {'Correct!' if area_answer.lower() == area_correct.lower() else f'Incorrect! Correct answer: {area_correct}'}", font=customFont)
        feedback_label_area.pack()

        feedback_label_continent = Label(feedback_window, text=f"Continent: {'Correct!' if continent_answer.lower() == continent_correct.lower() else f'Incorrect! Correct answer: {continent_correct}'}", font=customFont)
        feedback_label_continent.pack()
    except Exception as e:
         print(f"An Error occurred: {e}")

#This function is for to increase the size of the font
def increaseFontSize():
    currentSize=customFont.cget("size")
    newSize=currentSize+2
    customFont.config(size=newSize)


root = Tk()

#GUI logic here 
root.title("GAME FOR CHILDREN")
customFont=font.Font(family="Calibri",size=12)

country_info_label=Label(root,text="CLICK THE BUTTON FOR COUNTRY INFORMATION ")
country_info_label.grid(row=1,column=0)
country_info_label.config(font=customFont)

flag_label=Label(root)
flag_label.grid(row=0,column=0)

get_info_button=Button(root,text=" Get Country Flag ",command=showCountryInfo,font=customFont)
get_info_button.grid(row=2,column=0)

#labels to user to choose option of country names

label1 = Label(root, text="", font=customFont)
label1.grid(row=5, column=0, padx=0)

label2 = Label(root, text="", font=customFont)
label2.grid(row=5, column=1, padx=5)

label3 = Label(root, text="", font=customFont)
label3.grid(row=6, column=0, padx=0)

label4 = Label(root, text="", font=customFont)
label4.grid(row=6, column=1, padx=5)

option_labels = [label1, label2, label3, label4]

label5=Label(root,text="Guess the Country name and Then Enter Your Answer  : ",font=customFont)

label6=Entry(root,font=customFont)

#labels for capital options
option_labels_capital=[]
label7=Label(root,text="Below given the Country Capital name :",font=customFont)

label8=Label(root,text="",font=customFont)
label8.grid(row=10,column=0,padx=0)

label9=Label(root,text="",font=customFont)
label9.grid(row=10,column=1,padx=5)

label10=Label(root,text="",font=customFont)
label10.grid(row=11,column=0,padx=0)

label11=Label(root,text="",font=customFont)
label11.grid(row=11,column=1,padx=5)

option_labels_capital=[label8,label9,label10,label11]

label12=Label(root,text="Guess the Country Capital name and Then Enter Your Answer  : ",font=customFont)

label13=Entry(root,text="",font=customFont)

#labels for population options
label14=Label(root,text="Below given the Country Population Information :",font=customFont)

label15=Label(root,text="",font=customFont)
label15.grid(row=15,column=0,padx=0)

label16=Label(root,text="",font=customFont)
label16.grid(row=15,column=1,padx=5)

label17=Label(root,text="",font=customFont)
label17.grid(row=16,column=0,padx=0)

label18=Label(root,text="",font=customFont)
label18.grid(row=16,column=1,padx=5)

option_labels_population=[label15,label16,label17,label18]

label19=Label(root,text="Guess the Country Population and Then Enter Your Answer  :",font=customFont)

label20=Entry(root,text="",font=customFont)

#labels for area options

label21=Label(root,text="Below given the Country Area Information : ",font=customFont)

label22=Label(root,text="",font=customFont)
label22.grid(row=2,column=6,padx=0,pady=10)

label23=Label(root,text="",font=customFont)
label23.grid(row=2,column=8,padx=5,pady=10)

label24=Label(root,text="",font=customFont)
label24.grid(row=3,column=6,padx=0)

label25=Label(root,text="",font=customFont)
label25.grid(row=3,column=8,padx=5)

option_labels_area=[label22,label23,label24,label25]

label26=Label(root,text="Guess the Country Area and Then Enter Your Answer  :",font=customFont)

label27=Entry(root,text="",font=customFont)

#labels for Continent options

label28=Label(root,text="Below given the Continent  Information : ",font=customFont)

label29=Label(root,text="",font=customFont)
label29.grid(row=7,column=6)

label30=Label(root,text="",font=customFont)
label30.grid(row=7,column=8)

label31=Label(root,text="",font=customFont)
label31.grid(row=8,column=6)

label32=Label(root,text="",font=customFont)
label32.grid(row=8,column=8)

option_labels_continent=[label29,label30,label31,label32]

label33=Label(root,text="Guess the Country Continent and Then Enter Your Answer  :",font=customFont)

label34=Entry(root,text="")

check_answers_button = Button(root, text="Check Answers", command=checkAnswers, font=customFont)

root.mainloop()