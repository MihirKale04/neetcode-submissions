class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        long long low = 1;
        long long high = *max_element(piles.begin(), piles.end());
        long long ans = high;
        while (low <= high){
            long long mid = low + (high - low ) / 2;
            long long hours_needed = 0;

            for (int pile : piles) {
                hours_needed += (long long)ceil((double)pile/mid);
            }

            if (hours_needed <= h) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }    
        return ans;
        
    }
};
