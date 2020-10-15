public static partial class Utils
    {
        static string WeightCountMustBeGreaterThanZero="Weight count must be greater than zero.";
        static string ElementWeightMustBeGreaterThanOrEqualToZero="Weight must be greater than or equal to zero";

    /// Returns random index in weights list with probability based on its weight value.
    /// Throws an exception if weights count is equal to or less than zero.

/// <example>

        /// var weights=new List&lt;int&gt;(new int[]{2,3,5,0});
        /// int v=new Random().WeightedRandom(weights);
        /// 20% chance for v==0
        /// 30% chance for v==1
        /// 50% chance for v==2
        /// 0% chance for v==3

        public static int WeightedRandom(this Random rnd, IList<int> weights)
        {
            if (weights == null)
            {
                throw new ArgumentNullException("weights");
            }
            if (weights.Count == 0)
            {
                throw new ArgumentOutOfRangeException("weights", WeightCountMustBeGreaterThanZero);
            }
            List<int> total_weights = new List<int>();
            for (int i = 0; i < weights.Count; i++)
            {
                if (weights[i] < 0)
                {
                    throw new ArgumentOutOfRangeException("weights", ElementWeightMustBeGreaterThanOrEqualToZero);
                }
                int last;
                if (total_weights.Count > 0)
                {
                    last = total_weights[total_weights.Count - 1];
                }
                else
                {
                    last = 0;
                }
                int w = checked(last + weights[i]);
                total_weights.Add(w);
            }
            int total_random = rnd.Next(total_weights[total_weights.Count - 1]);
            for (int i = 0; i < weights.Count; i++)
            {
                if (weights[i] > total_random)
                {
                    return i;
                }
                total_random -= weights[i];
            }
            throw new Exception();
        }
    }
