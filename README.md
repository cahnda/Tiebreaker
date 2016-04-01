# TIEBREAKER: DEMOCRATIZING A/B Testing


## Overview

**Tiebreaker**, is an A/B testing platform that allows users to test alternative titles for books and articles, user interfaces for mobile applications, and logo/business ideas. In today's market place there exist large complex A/B testing platforms for the largest website development and Fortune 500 companies inlcuding Optimize.ly and Oracle's Maximizer. There also exist smaller platforms that target authors such as PickFu. All of these firms, however, charge monopoly prices and extract exorbinant profit margins. Our mission is to unleash the power of the crowd on the market research industry by serving the lower to middle segments of the market with end to end solution for brainstorming and testing titles, designs, and ideas, and charging **at cost**.
### Component 1: The Front End


#### Sub-Component 1: Auxilliary functionality


##### Part A: The Home Page

We believe that front-end web development is critical to the success of web applications. As such, we plan to invest signficant resources designing a home page, and, in doing so, a template for the rest of our web application. This will take half the time of the 

##### Part B: The Login Page

We'll design a LogIn page so that users can purchase A/B tests, leave the site, and come back to see the results of their hits. User accounts will maintain information about all past A/B tests and will be associated with usernames and passwords. Payment information will be processed for loggin users. 

#### Sub-Component 2: Primary functionality

##### Part A: A/B Testing Request Page

Users will submit their questions, choices, and the number of responses they request.

##### Part B: Payment Processing / Stripe API

Users will submit payments through the Stripe API to pay for their purchases.

##### Part C: A/B Testing Results Page

Users will see their results displayed on the Results page. The results will be displayed directly on the site, and an Excel sheet with the results will also be available for download.

### Component 2: The Back End: Mechanical Turk

#### Sub-Component 1: Aggregation Module 

The aggregation module (see the mturk_backend file in the respository) sends hits to Amazon Mechanical Turk and asks workers to pick a preference in the A/B test and explain why they made that choice.

#### Sub-Component 2: Quality Control Module

The Quality Control module involves a few checks to make sure the customers receive valid results. 

##### Part A: Mechanical Turk QC Hits

We send all explanations to MTurk workers through an additional quality control hit in which workers rate work as valid or invalid. These quality control hits contain gold standards and redundancy to make sure poor responses are properly identified.

##### Part B: Built-in Gold Standards

All A/B test contain a gold standard A/B test with an obviosely correct answer (e.g. This Title Sucks vs. This Title Rocks)

#### Sub-Component 3: EM Algorithm Module

The EM algorithm is used based on each workers responses to previous hits and responses to current hits to created a weighted score for the A/B test hit

#### Sub-Component 4: Results

Results are stored as an array of tuples where the first component of the tuple is the A or B response and the second component of the tuple is the explanation behind the response.


### Component 3: The Middle End: Mongo DB System

#### Sub-Component 1: User Storage

Stores user login information

#### Sub-Component 2: Results Storage

Stores responses to users' past and current A/B tests

### Component 4: Reach Goals

#### Sub-Component 1: BrainStormIt Implementation

Allows users to simply submit a question. Our backend aggregates potential responses and then A/B tests those responses to give the user back a ranking of the top five responses to the question

#### Sub-Component 2: Experimentation / Research

Experimentation to evaluate how effective the crowd is compared with experts




