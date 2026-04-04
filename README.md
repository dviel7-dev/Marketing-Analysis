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

# The base CSV file
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

# Excel Analysis and Dashboard
The CSV file was converted to XLSX, and a table was created with the data. Several pivot tables were then created to obtain the following metrics:

Sum of total sales.

User type.

Percentage of converted sales.

Total sales by channel and campaign.

Total sales by campaign.

Total sales by channel.

A dashboard was then created with the obtained metrics:

<img width="1021" height="717" alt="Marketing_excel_dashboard" src="https://github.com/user-attachments/assets/2fb9c5a3-e659-45b1-864a-27f18edf4b9b" />

