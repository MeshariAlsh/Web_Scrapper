from  playwright.sync_api import sync_playwright, Playwright
import  pandas as pd
import time


def run(playwright: Playwright):

    #For adding data to an existing CSV file
    #file_path = "UFC_Fighters_e.csv"
    #fightersData = pd.read_csv(file_path)

    # To store urls 
    start_url = []

    with open("urls.txt","r") as f:
        start_url = [i.strip() for i in f.readlines()]
    
    chromium= playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()

   #List to store fighter data
    myList = []
    
    for i in start_url:
        
            page.goto(i)
        
            #Scrape essential data
            record = page.locator("p.hero-profile__division-body").text_content()
            fighterName = page.locator("h1.hero-profile__name").text_content()

            #Scrape fighting style 
            styleFighting = page.locator("div.c-bio__row--2col  div.c-bio__text")

            #Scrape bio stats like age, height, weight, reach etc
            bioStatsValue = page.locator("div.c-bio__row--3col div.c-bio__text")
            sigStrikes = page.locator("div.c-stat-3bar__value")

            #Scrape average match stats like strike per min, submission, takendowns etc
            avgStatsPerMin_groupOne = page.locator("div.c-stat-compare__group-1 .c-stat-compare__number")
            avgStatsPerMin_groupTwo = page.locator("div.c-stat-compare__group-2 .c-stat-compare__number")

            #intilize a row for each fighter name
            fighterSecondName = fighterName.split()
            row = [fighterSecondName[1]]
        
            #Check if the locator has two values to avoid scraping 'Training at' instead of 'Fighting style'
            if styleFighting.count() == 2:
                styleValue = styleFighting.nth(1).text_content().strip()
                row.append(styleValue)
            else:
                styleValue = styleFighting.nth(0).text_content().strip()
                row.append(styleValue)

            for i in range(bioStatsValue.count()):
                bioValue = bioStatsValue.nth(i).text_content().strip()
                row.append(bioValue)
        
            for i in range(sigStrikes.count()):
                sigStrValue = sigStrikes.nth(i).text_content().strip()
                divide = sigStrValue.split()
                row.append(divide[0])

            for i in range(avgStatsPerMin_groupTwo.count()):
                avgValueTwo = avgStatsPerMin_groupTwo.nth(i).text_content().strip().replace("\n", "").replace("  ","")
                row.append(avgValueTwo)

            for i in range(avgStatsPerMin_groupOne.count()):
                avgValueOne = avgStatsPerMin_groupOne.nth(i).text_content().strip().replace("\n", "").replace("  ","")
                row.append(avgValueOne)

            #Reformat record from "0-0-0 W-L-D" to "W-L-D 0-0-0" and append to myList
            parts = record.split()
           

            wins_loss_draws = parts[0].split("-")

            for i in range(len(wins_loss_draws)):
                row.append(wins_loss_draws[i])

            #Append fighter data as a row to the list for DataFrame conversion
            myList.append(row)

            time.sleep(15) #15-second delay to adhere to robots.txt crawl-delay
        

    #Convert dictionary to dataframe
    df = pd.DataFrame(myList, columns=["Name", "Fighting style", "Age", 
                                       "Height", "Weight", "Octagon Debut", 
                                       "Reach", "Leg reach", "Standing Strikes", 
                                       "Clinch Strikes", "Ground Strikes","KO/TKO",
                                       "DEC","SUB","Sig Str Absorbed Per Min", 
                                       "Sub avg Per 15 Min","Takedown Def Per 15 Min","Avg Fight Time",
                                       "Sig Str Landed Per Min", "Takedown Avg","Sig Str Defense",
                                       "Knockdown Avg","Wins","Loss","Draws"])
    
    #To add data to existing CSV file 
    #updatedFighterData = pd.concat([fightersData, df], ignore_index=True)

    df.to_csv("UFC_Fighters_Final.csv", index=False)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)