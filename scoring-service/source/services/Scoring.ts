import { DateTime } from 'luxon';
import {
  AccommodationScoring,
  RatingObject,
  Review,
  ReviewRatings,
} from '../types';
import * as ReviewRepository from '../repositories/Review';

async function getAccommodationScores(
  accommodationId: string
): Promise<AccommodationScoring> {
  // TODO: return all reviews by fetching all pages
  const reviews = await ReviewRepository.fetchReviews(accommodationId, 0, 1000);

  return {
    accommodationId: accommodationId,
    scoring: {
      weightedAverages: generateAllWeightedAverages(reviews),
    },
  };
}

function generateAllWeightedAverages(
  reviews: Array<Review>
): Record<string, number | null> {
  const ratingMapping: Record<string, string> = {
    general: 'rating_general',
    location: 'rating_location',
    service: 'rating_service',
    priceQuality: 'rating_price_quality',
    food: 'rating_food',
    room: 'rating_room',
    childFriendly: 'rating_child_friendly',
    interior: 'rating_interior',
    size: 'rating_size',
    activities: 'rating_activities',
    restaurants: 'rating_restaurants',
    sanitaryState: 'rating_sanitary_state',
    accessibility: 'rating_accessibility',
    nightlife: 'rating_nightlife',
    culture: 'rating_culture',
    surrounding: 'rating_surrounding',
    atmosphere: 'rating_atmoshpere',
    noviceSkipArea: 'rating_novice_ski_area',
    apresSki: 'rating_apres_ski',
    beach: 'rating_beach',
    entertainment: 'rating_entertainment',
    pool: 'rating_pool',
    terrace: 'rating_terrace',
    housing: 'rating_housing',
    hygiene: 'rating_hygiene',
  };

  return Object.keys(ratingMapping).reduce((ratingObject, ratingType) => {
    const reviewsForRating = mapReviewsForRating(
      reviews,
      ratingMapping[ratingType]
    );

    return {
      [ratingType]: calculateWeightedAverage(reviewsForRating),
      ...ratingObject,
    };
  }, {});
}

function mapReviewsForRating(
  reviews: Array<Review>,
  ratingProperty: string
): Array<RatingObject> {
  return reviews.map((review) => ({
    rating: review[ratingProperty as keyof ReviewRatings],
    reviewDate: review.entry_date,
  }));
}

function calculateWeightedAverage(reviews: Array<RatingObject>): number | null {
  const { weight, weightedScores } = reviews.reduce(
    (acc, review) => {
      if (review.rating === null) {
        return acc;
      }

      const reviewAgeInMonths = DateTime.now()
        .diff(DateTime.fromISO(review.reviewDate), 'months')
        .as('months');

      const weight = calculateWeight(reviewAgeInMonths);

      return {
        weight: acc.weight + weight,
        weightedScores: acc.weightedScores + weight * review.rating,
      };
    },
    {
      weight: 0,
      weightedScores: 0,
    }
  );

  if (weight === 0 && weightedScores === 0) {
    return null;
  }

  return Math.round((weightedScores / weight) * 100) / 100;
}

function calculateWeight(reviewAgeInMonths: number) {
  return reviewAgeInMonths > 24
    ? Math.log(1.77)
    : Math.log(25 - reviewAgeInMonths);
}

export { getAccommodationScores, calculateWeightedAverage };
