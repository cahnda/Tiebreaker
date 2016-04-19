# TIEBREAKER: DEMOCRATIZING A/B TESTING

## Instuctions for NETS 213 Teaching Team
Our "working prototype" is a fully-functional finished product of the Tiebreaker website. Due to the complexity of the web application, we are currently running Tiebreaker off of our local machines. As we proceed to the final step in the project, we will work toward hosting the website at a publicly accessible URL. In the meantime, we have included instructions for running Tiebreaker on your local machine below: 

**Step 1: Loading the App**

1. **Import system Requirments:** Pip install the requirements in requirements.txt. Make sure that you have the most recent version of Java (this is critical).
2. **Get the Secret Key:** Email cahnja@wharton.upenn.edu and request the most recent API Secret Key. We cannot post this key on Github due to security concerns. Once you have the secret key, go into the folder mturk_backend/bin and open the file mturk.properties. Copy and paste (no quotes needed, just directly copy and paste) the secret key and access key into the indicated spots. Now the AWS connection should work for you.
3. **Run the App:** Go into your terminal to the cloned repository. Run "python app.py". Load: http://127.0.0.1:5000/ in your URL bar. 

**Step 2: Using the App**

1. **Login:** Use the login button. 
2. **Create a Hit:** Click Get Started. Type in your Question and 2 choices. For now use the question "Which title do you like better?" which we've hard coded in for the time being. Make up two titles of your choosing.
3. **Pay for the Hit:** Use 4242 4242 4242 4242 as the credit card number for now (we don't want to make you pay). You can make up the expiration date and pin number.
4. **Complete the Hit:** Complete ALL of the hits at link: "https://workersandbox.mturk.com/mturk/preview?groupId=3UY3BQX0VVC59LPG46Y13TOMDQG02Z" to get the results back (there should not be many). Refresh the results page and you'll see your results. 
5. **Load the Results:** The results should load on the results page.

We have robustly tested the app on the production site. There, we get 50 results instead of just 1 result and use the responses to the gold standard question (which are now just "this title rocks" and "this title sucks") to do initial quality control. Full details on the app are below.

If you have any problems, we are happy to answer any questions at cahnja@wharton.upenn.edu. If you have any issues downloading the system requirments, we are happy to demo the prototype on our local machines. By the final step of this assignment, we should have the site hosted online, so downloading system requirements will not be an issue.


## Overview

**Tiebreaker**, is an A/B testing platform that allows users to test alternative titles for books and articles, user interfaces for mobile applications, and business names and logos by crowdsourcing the consumer preferences of crowd-workers on Amazon's Mechanical Turk platform. Our mission is democratize and disrupt the A/B testing industry by charging customers **at cost** and pricing out the existing players who currently extract monopoly prices. The app was created because the founders were tired of burning money by purchasing A/B tests on expensive platforms and wanted to design a solution that cut out the 90% profit margins charged by existing players. Tiebreaker's primary target audience is journalists and authors who need to test title choices and cover designs. 

1. **Deliverable 1:** The diagrams and flow charts for Deliverable 1 can be found in the Class Deliverables folder in the sub-directories "Flow Diagrams" and "Screenshots/Mockups."
2. **Deliverable 2:** See the Class Deliverables folder. 
	* The sub-directory "QC Module" contains a python script that implements the gold standard procedure, a csv file with gold standard titles where the left column is the correct answer and the right column is the incorrect answer, and folders with sample inputs and sample outputs. The sample inputs folder contains the results of MTurk searches and the Sample Outputs folders contains tags based on whether validating MTurk workers labeled the response valid or invalid. The GoldStandard implementation is baked into the aggregation module. 
	* The sub-directory "Aggregation Module" contains the core python scripts for this project. loadResults.py is a script that loads user inputs into a MTurk Hit. returnResults.py is a script that is run every five minutes on the server to aggregate the results from MTurk and returns a matrix with worker responses to given queries. The "Aggregation Module" sub-directory also contains Sample Inputs and Sample Outputs folders. The Sample Inputs folder contain inputs for each MTurk call. These files are written by the loadResults.py script and includes the user inputs "Choice 1" "Choice 2" and "N". The Sample Outputs folders contains the results of calls to returnResults.py, which are spreadsheets with worker responses.
	* The sub-directory "Raw Data" contains that actual data generated by the crowd on sample queries. Each sub-directory corresponds to a seperate query.


### Component 1: The Front End


#### Sub-Component 1: Auxilliary functionality


##### Part A: The Home Page (2)

Front-end development is critical to the success of web applications, particularly user-centric products like Tiebreaker. In order to help Tiebreaker stand out from the plethora of existing, but highly expensive, solutions in the marketplace, we made front-end design a key point of emphasis for our team. Front-end tools include Bootstrap, as well as basic HTML, CSS and Javascript programs. Particular emphasis in the front-end design process was placed on the home page given its critical signficance in winning the attention of potential users. Statistical analyses show that users tend to form their impressions of websites with .05 seconds, making the home page the virtual "gateway" to a successful web application. Furthermore, because close to 85% of users search the web before making a purchase decision and 94% say that first impressions are based on design, an elegant front page design is one of the best sales tools for new and growing web applications. This is especially true for young entrepreneurs because 74% of users make credibility judgements based on web design. 

##### Part B: The Login Page

A system for users to register and login is key to both Tiebreaker's functionality and user retention strategy. For functionality purposes, it makes sense for user's to create unique accounts associated with their previous questions in case they want to rephrase or reuse old A/B tests and with their payment information. For retention purchases, it is helpful for user's to be able to be reminded of the value we've created for them in the past upon login. The login design is simple and is linked with a simple MongoDB database system which securely stores usernames, passwords, and previous A/B tests. 

#### Sub-Component 2: Primary functionality

##### Part A: A/B Testing Request Page (2)

The core revenue-generating segment of the web application is the A/B testing request page where users can type in their questions of interest as well as the two choices they are currently considering. In its present form, the A/B testing request page only takes text inputs. The next iteration of the Tiebreaker site will also include the ability to upload pictures that can be A/B tested and compared by crowd-workers. In its present form, request functionality is limited to two choices on the core page. The next iteration will include functionality that allows users to compare multiple choices if they so choose, although this option will be more expensive because it requires an increasing number of A/B split tests. The request page itself will store the user's three inputs, which will be delivered to the Python script on the backend that connects to the Amazon Mechanical Turk API, and redirect to the payment processing page.

##### Part B: Payment Processing / Stripe API (2)

Users will be redirected to the payment processing page from the A/B testing page. The first step for users will be to choose how many responses they'd like to get from crowd-workers, with the default number set at 50 responses. In its current iteration, we pay workers four cents per hit and charge users a fixed 1 percent commission all on orders to cover our fixed costs. The payment processing itself occurs through the Stripe API, which is integrated into our application.

##### Part C: A/B Testing Results Page (4)

Every five minutes, the results pages that do not have finished results yet are updated based on the progress of crowd-workers on Amazon's Mechanical Turk. Those pages where the Amazon Mechanical Turk hits are completed retrieve the finished information from the MongoDB dabatase where the results of all completed A/B tests are stored. The Results page is the most difficult of the core functionality pages in terms of design complexity because the page must be ready to update based on incoming information. Second, we implemented the page so that users can hover over results and view the demographic backgrounds of users. 

### Component 2: The Back End: Mechanical Turk

#### Sub-Component 1: Aggregation Module (see: MTurk_Backend) (4)

The aggregation module is a complex set of programs that constantly interact to send data back and forth between the Tiebreaker application and the Amazon Mechanical Turk platform. The first component of the aggregation module in the functionality that distributes user inputs to a XML file generator. The XML file generator takes a user's inputs and a basic MTurk Hit template and merged them to create a ready for production MTurk Hit. The second component sends this Hit to the mechanical turk platform, where MTurk crowd-workers are asked to fill out a demographic survey, respond to the A/B test of interest, explain their choice, and fill out "Gold Standard" questions that evalute whether or not they are credible workers. The third component intermiddentely walks through all unfinished A/B tests and sends the updated results to the Tiebreaker front end for display to the users. If an A/B test finishes during this check, the program makes a change to the test to indicate that it is finished (so that it is not checked in future iterations) and transfers this finished information to the MongoDB database. 

#### Sub-Component 2: Quality Control Module (4)

The Quality Control module includes 3 different checks to make sure that crowd-workers are returning high-quality results. First, when crowd-workers finish choosing the preferences in the A/B test and describing their preferences, we run a second Quality Control Hit in which a new set of workers reviews the answers to the first hit to notify us if the answers are either not written in English or do not make sense to a reasonable observer. Second, in the first Hit, we include "Gold Standard" questions with obviousely correct answers so that we can remove the results of workers who do not give the question sufficient attention. Third, we use the Expectation-Maximization (EM) algorithm to weight workers responses based on the quality of past work.

#### Sub-Component 3: EM Algorithm Module (2)

A weighted analsysis algorithm is employed as a quality control mechanism. We store in a MongoDB datased a 2 by 2 matrix with all A/B tests ever completed on our platform on one axis and all workers on the other axis. If a worker is in the majority opinion on a hit, the intersection of the worker and hit is a 1. If a worker in in the minoirty opinion, the intersection is a 0, and if the worker did not participate in the hit, the intersection is a -1. This way we can give workers weights based on the percent of times in which the workers chose the "correct" answer. Based on the weights of other workers, the "correct" answer may change. Changes to weights do not affect past analyses of those workers, but do affect future analyses, in which we report to the user the weighted vote count as well as the raw weight count. 

#### Sub-Component 4: Results

Results are stored as an array of tuples, where the first element of the tuple is the worker's response to the A/B test and the second element of the tuple is the worker's explanation. The results are sent from the Mechanical Turk platform to the web application, where they are stored and hosted for users to access at any point i the future. 

### Component 3: The Middle End: Mongo DB System (2)

#### Sub-Component 1: User Storage

The user storage is the less complex sub-component of the middle end. Usernames, passwords, and any other relevant user-centric information is stored in a MongoDB databse. 

#### Sub-Component 2: Results Storage

The results storage component is complex because it required the database to be flexible and store a wide variety of different inputs including non-text responses.

### Component 4: Reach Goals
 
#### Sub-Component 1: BrainStormIt Implementation (2)

The BrainStormIt component is a reach goal which we are currently implementing. BrainStormIt will allow users to ask a question without choices. The Tiebreaker back end will call on Mechanical Turk workers to generate responses to this question and will gather the responses of workers. In a second pass, it will have workers narrow down the list of options with built-in redundancy. Finally, it will take the top 10 answers and use A/B tests to rank the various answers so that a ranked list of answers can be returned to the users. 

#### Sub-Component 2: Experimentation / Research (2)

The Experimentation portion involves a battery of tests we will run to evaluate how effective crowd-workers are compared with an expert control group.

