import logging
from typing import Dict, List
from validator import ToolValidator

class CognitiveToolRecommender:
    """Recommends cognitive tools based on validated data."""
    
    def __init__(self):
        self.validator = ToolValidator()
        
    def get_top_tools(self, validated_tools: List[Dict], num_recommendations: int = 5) -> List[Dict]:
        """Returns the top recommended tools based on validation and popularity."""
        try:
            # Simple recommendation logic (can be replaced with ML models)
            sorted_tools = sorted(
                validated_tools,
                key=lambda x: (-len(x['description']), x['feedback_score']),
                reverse=True
            )
            return sorted_tools[:num_recommendations]
        except Exception as e:
            logging.error(f"Recommendation failed: {e}")
            raise

    def generate_recommendation_report(self, recommendations: List[Dict]) -> Dict:
        """Generates a report for recommended tools."""
        try:
            report = {
                'recommendations': [
                    {
                        'name': tool['name'],
                        'description': tool['description'],
                        'score': round(tool.get('feedback_score', 4.5), 1),
                        'source': tool['source']
                    } for tool in recommendations
                ],
                'timestamp': self._get_current_timestamp()
            }
            return report
        except Exception as e:
            logging.error(f"Report generation failed: {e}")
            raise

    def _get_current_timestamp(self) -> str:
        """Returns the current timestamp as a formatted string."""
        import datetime
        return datetime.datetime.now().isoformat()

    def get_personalized_recommendations(self, user_profile: Dict) -> List[Dict]:
        """Generates personalized recommendations based on user profile."""
        try:
            # Example logic using user profile data
            required_capabilities = user_profile.get('capabilities', [])
            preferred_tools = self.validator.validate_batch(
                tools,
                {'keywords': required_capabilities}
            )
            return self.get_top_tools(preferred_tools)
        except Exception as e:
            logging.error(f"Personalized recommendation failed: {e}")
            raise