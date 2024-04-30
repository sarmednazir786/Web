## Title: The Shrewd thief
## Details:
* difficulty: Easy
* category: Web 
* author: Sarmed
* flags: flag{XSS Exploited Successfully}

## Description:
Cross site scripting is a fairly common and one of the most exploited vulnerabilities in the Application Security ecosystem.

## Hint:
Pay attention to where there are input fields.

## Intended Learning and outcome:

With the given challenge, I was able to learn about how severe the vulnerability of Cross-Site Scripting is, as it can be used to steal session cookies of the victim. I learnt that there are different types of XSS, Reflected, Dom-based, and Stored. In this challenge I explored the Reflected XSS in depth. 

## Solution: 

To start this challenge you need to download the files in the repo. Then using the command "python3 server.py" on the terminal, we will run the script. Finally, we will go inside the templates folder and open the index.js file. The application looks like a real-world simulation of a consultancy, we will find potential input fields and we can see that the subscribe text box is one. When we enter an email, it accepts it, and shows us Subscribed. As we know this is an XSS Lab, we will enter the basic payload, "<script>alert(1)</script>" and upon hitting the subscribe button, we see the alert box is triggered. In the terminal, we can see the flag is displayed.


........




