#!/usr/bin/env python3
"""
Script to seed the database with Disney World rides
"""
import requests
import json

API_URL = "http://localhost:8765/api"

DISNEY_RIDES = [
    # Magic Kingdom - Adventureland
    {
        "name": "Jungle Cruise",
        "location": "Adventureland",
        "description": "Embark on a guided tour through exotic jungle settings",
        "min_height": None,
        "queue_time": 45,
        "park_area": "Magic Kingdom - Adventureland"
    },
    {
        "name": "Pirates of the Caribbean",
        "location": "Adventureland",
        "description": "Experience the life and exploits of pirate crews throughout the ages",
        "min_height": None,
        "queue_time": 55,
        "park_area": "Magic Kingdom - Adventureland"
    },
    
    # Magic Kingdom - Frontierland
    {
        "name": "Big Thunder Mountain Railroad",
        "location": "Frontierland",
        "description": "A thrilling runaway mine train roller coaster",
        "min_height": 3.8,
        "queue_time": 60,
        "park_area": "Magic Kingdom - Frontierland"
    },
    {
        "name": "Splash Mountain",
        "location": "Frontierland",
        "description": "Splash down a thrilling five-story drop",
        "min_height": 3.6,
        "queue_time": 50,
        "park_area": "Magic Kingdom - Frontierland"
    },
    
    # Magic Kingdom - Tomorrowland
    {
        "name": "Space Mountain",
        "location": "Tomorrowland",
        "description": "Blast off on an outer space adventure",
        "min_height": 3.6,
        "queue_time": 65,
        "park_area": "Magic Kingdom - Tomorrowland"
    },
    {
        "name": "Buzz Lightyear of Star Command Astro Blasters",
        "location": "Tomorrowland",
        "description": "Battle the Evil Emperor Zurg with interactive laser cannons",
        "min_height": None,
        "queue_time": 35,
        "park_area": "Magic Kingdom - Tomorrowland"
    },
    
    # Magic Kingdom - Fantasyland
    {
        "name": "Cinderella's Royal Table",
        "location": "Fantasyland",
        "description": "Dine in Cinderella's Castle and meet Disney Princesses",
        "min_height": None,
        "queue_time": 120,
        "park_area": "Magic Kingdom - Fantasyland"
    },
    {
        "name": "It's a Small World",
        "location": "Fantasyland",
        "description": "Journey around the world celebrating world cultures",
        "min_height": None,
        "queue_time": 25,
        "park_area": "Magic Kingdom - Fantasyland"
    },
    {
        "name": "Haunted Mansion",
        "location": "Liberty Square",
        "description": "Tour a spooky mansion filled with 999 happy haunts",
        "min_height": None,
        "queue_time": 40,
        "park_area": "Magic Kingdom - Liberty Square"
    },
    
    # EPCOT
    {
        "name": "Test Track",
        "location": "EPCOT - Future World",
        "description": "Test innovative vehicles in a thrilling high-speed drive",
        "min_height": 3.8,
        "queue_time": 50,
        "park_area": "EPCOT"
    },
    {
        "name": "Soarin' Around the World",
        "location": "EPCOT - The Land",
        "description": "Glide over the world's most beautiful landmarks",
        "min_height": None,
        "queue_time": 45,
        "park_area": "EPCOT"
    },
    {
        "name": "The Seas with Nemo & Friends",
        "location": "EPCOT - Future World",
        "description": "Explore the ocean with Nemo and friends",
        "min_height": None,
        "queue_time": 30,
        "park_area": "EPCOT"
    },
    {
        "name": "Frozen Ever After",
        "location": "EPCOT - Norway",
        "description": "Join Anna and Elsa in a winter-themed musical journey",
        "min_height": None,
        "queue_time": 55,
        "park_area": "EPCOT"
    },
    
    # Hollywood Studios
    {
        "name": "Star Wars: Galaxy's Edge - Millennium Falcon Smugglers Run",
        "location": "Star Wars: Galaxy's Edge",
        "description": "Pilot the legendary Millennium Falcon on a cargo mission",
        "min_height": None,
        "queue_time": 90,
        "park_area": "Hollywood Studios"
    },
    {
        "name": "Tower of Terror",
        "location": "Twilight Zone Tower of Terror",
        "description": "Face the unknown in a haunted hotel tower",
        "min_height": 4.0,
        "queue_time": 65,
        "park_area": "Hollywood Studios"
    },
    {
        "name": "Rock 'n' Roller Coaster Starring Aerosmith",
        "location": "Hollywood Studios - Sunset Boulevard",
        "description": "Launch into a high-speed rock and roll adventure",
        "min_height": 3.8,
        "queue_time": 50,
        "park_area": "Hollywood Studios"
    },
    {
        "name": "Toy Story Land - Slinky Dog Dash",
        "location": "Toy Story Land",
        "description": "Ride along Slinky Dog's track in Andy's backyard",
        "min_height": 3.5,
        "queue_time": 75,
        "park_area": "Hollywood Studios"
    },
    
    # Animal Kingdom
    {
        "name": "Expedition Everest",
        "location": "Asia",
        "description": "Encounter the legendary Yeti on this thrilling coaster",
        "min_height": 3.6,
        "queue_time": 60,
        "park_area": "Animal Kingdom"
    },
    {
        "name": "Kilimanjaro Safaris",
        "location": "Africa",
        "description": "See real animals on an African safari adventure",
        "min_height": None,
        "queue_time": 40,
        "park_area": "Animal Kingdom"
    },
    {
        "name": "Avatar Flight of Passage",
        "location": "Pandora - The World of Avatar",
        "description": "Soar through the mystical world of Pandora on a banshee",
        "min_height": 3.6,
        "queue_time": 100,
        "park_area": "Animal Kingdom"
    },
    {
        "name": "Kali River Rapids",
        "location": "Asia",
        "description": "Navigate through a white-water river adventure",
        "min_height": 3.3,
        "queue_time": 45,
        "park_area": "Animal Kingdom"
    }
]

def add_rides():
    """Add all Disney World rides to the database"""
    print("🎢 Adding Disney World rides to the database...\n")
    
    success_count = 0
    error_count = 0
    
    for ride in DISNEY_RIDES:
        try:
            response = requests.post(
                f"{API_URL}/rides",
                json=ride,
                timeout=5
            )
            
            if response.status_code == 201:
                result = response.json()
                print(f"✅ Added: {ride['name']} (ID: {result['id']})")
                success_count += 1
            else:
                print(f"❌ Failed to add {ride['name']}: {response.status_code}")
                error_count += 1
                
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection Error: Unable to connect to API at {API_URL}")
            print("   Make sure the backend server is running on port 8765")
            return
        except Exception as e:
            print(f"❌ Error adding {ride['name']}: {str(e)}")
            error_count += 1
    
    print(f"\n{'='*50}")
    print(f"✨ Results: {success_count} rides added, {error_count} failed")
    print(f"{'='*50}")

if __name__ == "__main__":
    add_rides()
