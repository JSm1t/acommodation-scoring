import axios from 'axios';
import { config } from '../config';
import { ReviewsResponse, Review } from '../types';

async function fetchReviews(
  accommodationId: string,
  skip: number = 0,
  limit: number = 100
): Promise<Array<Review>> {
  const { data } = await axios.get(
    `${config.dataService.baseUrl}/accommodations/${accommodationId}/reviews?skip=${skip}&limit=${limit}`
  );

  return data.data;
}

export { fetchReviews };
