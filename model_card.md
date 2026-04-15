# 🎧 Model Card: Music Recommender Simulation

## Model Overview
This is a simple music recommender that suggests songs based on user preferences like genre, mood, and energy.

## Intended Use
This is for learning how recommendation systems work. It’s not meant for real-world use.

## Input Data
- Song data: genre, mood, energy, acousticness  
- User preferences: favorite genre, mood, energy level, acoustic preference  

## Output
A list of songs ranked by how well they match the user, with a short explanation.

## How It Works
Each song gets a score based on:
- genre match  
- mood match  
- how close the energy level is  
- acoustic preference  

Then songs are sorted from best match to worst.

## Limitations
- Very simple scoring  
- Small dataset  
- Doesn’t learn or update over time  

## Bias and Risks
- Can recommend the same types of songs repeatedly  
- Not very diverse  
- Depends heavily on user input  

## Future Improvements
- Add more song features  
- Improve the ranking logic  
- Make it adapt based on user behavior  