import { DateTime } from 'luxon';
import { AccommodationScoring, RatingObject } from '../types';
import * as ReviewRepository from '../repositories/Review';

async function getAccommodationScores(
  accommodationId: string
): Promise<AccommodationScoring> {
  const reviews = await ReviewRepository.fetchReviews(accommodationId);

  const cleanedDataset: Array<RatingObject> = reviews.map((review) => ({
    rating: review.ratingGeneral,
    reviewDate: new Date(review.postedAt),
  }));

  return {
    accommodationId: accommodationId,
    scoring: {
      weightedAverage: {
        general: calculateWeightedAverage(cleanedDataset),
      },
    },
  };
}

function calculateWeightedAverage(reviews: Array<RatingObject>): number | null {
  const { weight, weightedScores } = reviews.reduce(
    (acc, review) => {
      if (review.rating === null) {
        return acc;
      }

      const reviewAgeInMonths = DateTime.now()
        .diff(DateTime.fromJSDate(review.reviewDate), 'months')
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
