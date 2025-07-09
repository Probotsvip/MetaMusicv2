import aiohttp
import asyncio
import logging
from typing import Union

import config

YOUR_API_KEY = "api_861f95a5a0874f7ab9f7"
MUSIC_API_BASE_URL = "https://ytapi-1fd43e42f22f.herokuapp.com"

class MusicAPI:
    def __init__(self):
        self.base_url = MUSIC_API_BASE_URL
        self.api_key = YOUR_API_KEY

    async def get_audio_stream_from_api(self, query: str):
        """Get audio stream URL from our Music Stream API with API key"""
        try:
            async with aiohttp.ClientSession() as session:
                params = {
                    'query': query,
                    'api_key': self.api_key
                }
                async with session.get(
                    f"{self.base_url}/stream",
                    params=params,
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get('stream_url'), data.get('title', query)
                    else:
                        logging.error(f"Music API failed with status: {response.status}")
                        return None, None
        except Exception as e:
            logging.error(f"Error calling Music Stream API: {str(e)}")
            return None, None

    async def track(self, query: str):
        """Get track info and stream URL from Music API"""
        try:
            stream_url, title = await self.get_audio_stream_from_api(query)
            if not stream_url:
                return None, None

            # Return details in expected format for direct streaming
            details = {
                "title": title,
                "duration_min": "Unknown",
                "thumb": config.STREAM_IMG_URL,
                "stream_url": stream_url,
                "vidid": "musicapi"
            }
            return details, "musicapi"
        except Exception as e:
            print(f"MusicAPI track error: {e}")
            return None, None

    @staticmethod
    async def valid(link: str):
        """Check if it's a valid search query for our API"""
        return True  # Accept any text query

    @staticmethod
    async def exists(link: str):
        """Check if query exists"""
        return True  # Always return True for search queries