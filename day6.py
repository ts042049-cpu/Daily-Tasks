class Solution {
public:
    int knapsack(vector<int>& weight, vector<int>& profit, int W) {
        int n = weight.size();
        vector<int> dp(W + 1, 0);

        for (int i = 0; i < n; i++) {
            for (int w = W; w >= weight[i]; w--) {
                dp[w] = max(dp[w],
                            profit[i] + dp[w - weight[i]]);
            }
        }

        return dp[W];
    }
};