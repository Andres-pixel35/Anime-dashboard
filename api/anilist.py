import requests
import pandas as pd
import time

def fetch_anime_info(name, work_type):     
    # GraphQL query
    query = '''
    query ($search: String) {
        Media (search: $search, type: ANIME) {
            title {
                romaji
                english
            }
            format
            episodes
            duration
            source
            season
            seasonYear
            genres
            tags {
                name
            }
            startDate {
                year
                month
                day
            }
            countryOfOrigin
            averageScore
            nextAiringEpisode {
                episode
            }
        }
    }
    '''
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Referer': 'https://anilist.co/',
        'Origin': 'https://anilist.co',
    }
    variables = {'search': name}
    url = 'https://graphql.anilist.co'
    
    try:
        response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
        data = response.json()

        errors = data.get('errors') or []
        error_msg = '; '.join(e.get('message', '') for e in errors) or response.text

        if not response.ok:
            print(f"Error: AniList API returned {response.status_code}: {error_msg}")
            time.sleep(1)
            return ""

        if errors:
            print(f"Error: AniList API error: {error_msg}")
            time.sleep(1)
            return ""

        if (data.get('data') or {}).get('Media') is None:
            print(f"Error: No match found for '{name}'")
            time.sleep(1)
            return ""
        
        media = data['data']['Media']
        
        # Check if format matches the type
        media_format = media.get('format', '').lower()
        if media_format != work_type:
            print(f"Error: No match found for '{name}' with type '{work_type}'")
            time.sleep(1)
            return ""
        
        # Format start_date
        start_date = None
        if media.get('startDate'):
            sd = media['startDate']
            if sd.get('year') and sd.get('month') and sd.get('day'):
                start_date = f"{sd['year']}-{sd['month']}-{sd['day']}"
        
        # Extract and format genres
        genres = ';'.join(media.get('genres', [])) if media.get('genres') else None
        
        # Extract and format tags
        tags = ';'.join([tag['name'] for tag in media.get('tags', [])]) if media.get('tags') else None
        
        # Extract next episode number
        next_episode = None
        if media.get('nextAiringEpisode'):
            next_episode = media['nextAiringEpisode'].get('episode')
        
        # Create dataframe
        df = pd.DataFrame([{
            'title': media.get('title', {}).get('romaji'),
            'english_title': media.get('title', {}).get('english'),
            'type': media.get('format'),
            'episodes': media.get('episodes'),
            'duration': media.get('duration'),
            'source': media.get('source'),
            'season': media.get('season'), 
            'genres': genres,
            'tags': tags,
            'score': media.get('averageScore'),
            'start_date': start_date,
            'country_of_origin': media.get('countryOfOrigin'),
            'next_episode_number': next_episode
        }])
        
        time.sleep(2)
        return df
        
    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(1)
        return ""

