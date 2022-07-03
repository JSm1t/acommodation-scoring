import axios from 'axios';
import { config } from '../config';
import { ReviewsResponse, Review } from '../types';

async function fetchReviews(accommodationId: string): Promise<Array<Review>> {
  // TODO: fallback if data-service is down

  const { data } = await axios.get(
    `${config.dataService.baseUrl}/accommodations/${accommodationId}/reviews`
  );

  return data.data;
}

export { fetchReviews };
