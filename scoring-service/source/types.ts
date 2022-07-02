export interface AccommodationScoring {
  accommodationId: string;
  scoring: {
    weightedAverage: {
      general: number | null;
      // location: number;
      // service: number;
      // priceQuality: number;
      // food: number;
      // interior: number;
      // size: number;
      // activities: number;
      // restaurants: number;
      // santiaryState: number;
      // accessibility: number;
      // nightlife: number;
      // culture: number;
      // surrounding: number;
      // atmosphere: number;
      // noviceSkiArea: number;
      // advancedSkiArea: number;
      // apresSki: number;
      // beach: number;
      // entertainment: number;
      // environmental: number;
      // pool: number;
      // terrace: number;
      // housing: number;
      // hygience: number;
    };
  };
}

// TODO: add full model
export interface Review {
  id: string;
  ratingGeneral: number;
  postedAt: string;
}

export interface ReviewsResponse {
  data: Array<Review>;
}

export interface RatingObject {
  rating: number | null;
  reviewDate: Date;
}
