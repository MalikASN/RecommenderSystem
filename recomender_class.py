import json

class RecommenderSystem:
    """
    Simple recommender system based on cosine similarity JSON file.
    Input: list of 5 favorite movie IDs
    Output: 5 recommended movie IDs (1 per favorite)
    """

    def __init__(self, model_path: str, favorite_movie_ids: list[int]):
        self.model_path = model_path
        self.favorite_movie_ids = favorite_movie_ids

    def model_loader(self) -> dict:
        with open(self.model_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_recommended_movies(self) -> list[int]:
        model = self.model_loader()
        recommendations = []

        for fav_id in self.favorite_movie_ids:
            # Liste des 30 films similaires
            similar_list = model.get(str(fav_id), [])

            # Chercher le 1er film non favori
            for item in similar_list:
                rec_id = item["id"]
                if rec_id not in self.favorite_movie_ids:
                    recommendations.append(rec_id)
                    break

        return recommendations

    def save_recommended_movies(self):
        """
        Android implementation required: store Set<Int> in SharedPreferences.
        (Convert Int -> String for putStringSet)
        """
        pass
