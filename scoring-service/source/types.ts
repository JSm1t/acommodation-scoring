export interface AccommodationScoring {
  accommodationId: string;
  scoring: {
    weightedAverages: Record<string, number | null>;
  };
}

export interface ReviewRatings {
  rating_general: number;
  rating_location: number;
  rating_service: number;
  rating_price_quality: number;
  rating_food: number;
  rating_room: number;
  rating_child_friendly: number;
  rating_interior: number;
  rating_size: number;
  rating_activities: number;
  rating_restaurants: number;
  rating_sanitary_state: number;
  rating_accessibility: number;
  rating_nightlife: number;
  rating_culture: number;
  rating_surrounding: number;
  rating_atmosphere: number;
  rating_novice_ski_area: number;
  rating_apres_ski: number;
  rating_beach: number;
  rating_entertainment: number;
  rating_environmental: number;
  rating_pool: number;
  rating_terrace: number;
  rating_housing: number;
  rating_hygiene: number;
}

export interface Review extends ReviewRatings {
  id: string;
  entry_date: string;
}

export interface ReviewsResponse {
  data: Array<Review>;
}

export interface RatingObject {
  rating: number | null;
  reviewDate: string;
}
