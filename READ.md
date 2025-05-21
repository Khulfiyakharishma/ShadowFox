# ShadowFox Internship Tasks

This repository contains all the tasks completed during my Data Science Internship with ShadowFox.

## 📁 Contents:
- `datascience/`: Documentation for Matplotlib and Pandas (Task 1)
- `delhi_aqi_analysis/`: AQI Analysis Project using Python (Task 2)

## 🛠 Tools Used:
Python, Pandas, Matplotlib, Seaborn

ASSIGNMENT 1- Python Visualization Libraries Documentation
-----------------------------------------------

## Overview

This repository contains beginner-level documentation for two widely-used Python visualization libraries:

- **Matplotlib**
- **Seaborn**

The goal of this documentation is to introduce new learners to the basics of data visualization using Python. Each section includes an overview, key features, and practical code examples.

## Contents

1. 📚 Introduction to Matplotlib  
2. 📊 Common Graph Types with Matplotlib  
3. 🎨 Introduction to Seaborn  
4. 📈 Common Graph Types with Seaborn  
5. ⚖️ Comparison of Matplotlib vs Seaborn

## Key Features

- Clean and concise explanations for beginners
- Ready-to-run Python code examples
- Practical use cases for each graph type
- Markdown-based format for easy readability

## Technologies Used

- Python 3.x
- Jupyter Notebook / VS Code
- Libraries: `matplotlib`, `seaborn`, `pandas` (for sample data)


ASSIGNMENT 2-Delhi Air Quality Index (AQI) Analysis
--------------------------------------------------
## Project Overview

This project performs exploratory data analysis and visualization on Delhi's air quality data using Python. The goal is to understand pollution trends and visualize key insights using visual analytics.

## Dataset

- **File Name**: `delhiaqi.csv`
- **Contents**: Date-wise AQI values, pollutants (PM2.5, PM10, NO2, etc.), and location data

## Features

- 📈 Line plots to show AQI trends over time
- 📊 Bar charts for comparing pollutants
- 📌 Heatmaps to highlight pollutant concentration levels
- 📍 Location-based pollution analysis

## Technologies Used

- Python 3.x
- Visual Studio Code
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`

## ASSIGNMENT 3 – Cricket Fielding Performance Analysis Overview 
--------------------------------------------------

This advanced-level task focuses on quantifying and analyzing fielding performance in cricket. It involves recording detailed fielding events for each ball and calculating a Performance Score (PS) to evaluate individual fielders.

## Performance Metrics Formula 

To compute the Performance Score (PS) for a fielder:

PS = (CP × WCP) + (GT × WGT) + (C × WC) + (DC × WDC) + (ST × WST) + (RO × WRO) + (MRO × WMRO) + (DH × WDH) + RS 

Where:
PS: Performance Score
CP: Clean Picks
GT: Good Throws
C: Catches
DC: Dropped Catches
ST: Stumpings
RO: Run Outs
MRO: Missed Run Outs
DH: Direct Hits
RS: Runs Saved (positive for saved runs, negative for conceded runs)
W*: Assigned Weights for each action (to be defined based on coaching strategy)

## Task Instructions:

## Data Collection
Record each fielding action per ball in a match.
Include fields like Player Name, Over, Ball, Action Type, Outcome, Runs Saved/Conceded.

## Analysis Preparation
Use the collected data to identify top fielders and common errors.
Prepare for strategic fielding placements and training sessions.

## Deliverable
A clean, structured spreadsheet (Excel/CSV) or database containing all fielding actions.

Final output should include Performance Score per player.

## Tools: 
Excel, Google Sheets, or CSV-compatible editors

## Optional Analysis: 
Python + Pandas for automated score calculations

## Resources 

Sample Template & Formula Guide

Python Learning Roadmap

Author
Khulfiya Kharishma S
MCA Student, Crescent Institution,Chennai

