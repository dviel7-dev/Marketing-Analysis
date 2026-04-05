# Marketing-Campaign-Analysis
------------------------------

An analysis of a marketing campaign and its different transmission channels, as well as total sales and new users, to achieve greater efficiency when investing in advertising.

# The Campaign

In this project, our client, an online store, completed a week-long, multichannel marketing campaign designed to test messaging and customer response across a range of featured products.

The campaign included two versions of messages:

## Campaign A used a casual, conversational tone:

<img width="1277" height="715" alt="Campaign A" src="https://github.com/user-attachments/assets/ac2e7133-9e7c-4cda-b280-14b613945386" />

## Campaign B used a more promotional, sales-oriented tone:

<img width="1277" height="679" alt="Campaign B" src="https://github.com/user-attachments/assets/d020f971-bafd-4c8b-a545-27890394d643" />

The client used three marketing channels:

Email

Instagram

Website banner

## What the client wants to know:

“Which campaign and channel combination should we focus on to increase sales to new customers, and why?”

# The Data
The Marketing_Campaign_Data.csv file contains records of marketing interactions from the weekly campaign; these records will be used to analyze the effectiveness of different campaigns and channels.

Below is a detailed breakdown of the dataset's structure and contents:

## Column Overview
The dataset consists of 7 columns:

Interaction ID: A unique identifier for each customer interaction.

Campaign Type: Categorical variable with two groups, likely representing an A/B test.

Channel: The marketing platform used for the interaction.

Customer Type: Classification of the customer.

Converted (1=yes, 0=no): A binary indicator of whether the interaction led to a conversion.

Time on Site (seconds): The duration the user spent on the site.

Sales ($): The revenue generated from the interaction.

# Analysis and Dashboard
The CSV file was converted to XLSX, and a table was created with the data. Several pivot tables were then created to obtain the following metrics:

Sum of total sales.

User type.

Percentage of converted sales.

Total sales by channel and campaign.

Total sales by campaign.

Total sales by channel.

A dashboard was then created with the obtained metrics:

<img width="1019" height="717" alt="Marketing_excel_dashboard" src="https://github.com/user-attachments/assets/5fa69a5a-06bf-47c6-a01d-564f927e7fe5" />

# Results and Recommendations

The analysis performed on marketing campaigns A and B and their different transmission channels, with the objective of determining the best option when investing in advertising, concluded that campaign B via email is the best option when attracting new users, followed by campaign A via email, campaign B via Instagram, and campaign B via web banner.

The analysis revealed total sales from new users totaling $988,528.51 and a total of 42,597 new users with a purchase rate of 47.86%.

Campaign B via email acquired 9,700 new users and generated sales of $225,285.52, making it the most effective campaign in terms of acquiring new users and converting sales.

The reason for this may be the more formal and personalized communication provided by email, and the campaign's more sober and corporate tone, as seen in campaign B. This builds trust with consumers and a sense of status and exclusivity, encouraging them to visit the website and make purchases

<img width="1590" height="888" alt="MarketingInsights" src="https://github.com/user-attachments/assets/3d563f16-f50e-454f-b835-920ce320f06e" />
