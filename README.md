# coding-practice

This repository is based on the [template](https://github.com/yurirocha15/leetcode-practice-python) which automates the boilerplate code when adding solutions to leetcode problems.

Using a single command, one can get the question information, generate the python executable template, generate the test files, and update the table at the end of the README.

This repository uses [leetcode-cli](https://github.com/skygragon/leetcode-cli) to get the question information. Big thanks to the leetcode-cli owners for providing such tool.

## Usage

### Installation

To install the needed libraries:

```shell
$ make setup
```

For windows users, unzipping might not work because of firewall.

In that case, just download and unzip the [file](https://github.com/skygragon/leetcode-cli/releases/download/2.6.2/leetcode-cli.node10.win32.x64.zip) into bin/dist folder.

### Login to Leetcode

Currently, the only way to login is logging into chrome/firefox, then running:

```shell
$ make leetcode-login
```

This command automatically gets the needed cookies from the browser.

### Downloading a Question

To generate the files of a given question:

```shell
$ make get-question ID=<question_id>
```

## Question Solutions

| ID | Problem    | Category | Difficulty | From |
|:--:|------------|----------|------------|------|
|0 |[Get Maximum in Generated Array](src/array_problems/get_maximum_in_generated_array.py)|[array](src/array_problems)|Easy|[LeetCode](https://leetcode.com/problems/get-maximum-in-generated-array/)|
|1 |[Minimum Deletions to Make Character Frequencies Unique](src/sort_problems/minimum_deletions_to_make_character_frequencies_unique.py)|[sort](src/sort_problems)|Medium|[LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/)|
|2 |[Sell Diminishing-Valued Colored Balls](src/sort_problems/sell_diminishing_valued_colored_balls.py)|[sort](src/sort_problems)|Medium|[LeetCode](https://leetcode.com/problems/sell-diminishing-valued-colored-balls/)|
|3 |[Design an Ordered Stream](src/array_problems/design_an_ordered_stream.py)|[array](src/array_problems)|Easy|[LeetCode](https://leetcode.com/problems/design-an-ordered-stream/)|
|4 |[Determine if Two Strings Are Close](src/string_problems/determine_if_two_strings_are_close.py)|[string](src/string_problems)|Medium|[LeetCode](https://leetcode.com/problems/determine-if-two-strings-are-close/)|
|5 |[Minimum Operations to Reduce X to Zero](src/dp_problems/minimum_operations_to_reduce_x_to_zero.py)|[dp](src/dp_problems)|Medium|[LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)|
|6 |[Maximize Grid Happiness](src/dp_problems/maximize_grid_happiness.py)|[dp](src/dp_problems)|Hard|[LeetCode](https://leetcode.com/problems/maximize-grid-happiness/)|
|7 |[Check If Two String Arrays are Equivalent](src/string_problems/check_if_two_string_arrays_are_equivalent.py)|[string](src/string_problems)|Easy|[LeetCode](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)|
|8 |[Smallest String With A Given Numeric Value](src/string_problems/smallest_string_with_a_given_numeric_value.py)|[string](src/string_problems)|Medium|[LeetCode](https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/)|
|9 |[Richest Customer Wealth](src/array_problems/richest_costumer_wealth.py)|[array](src/array_problems)|Easy|[LeetCode](https://leetcode.com/problems/richest-customer-wealth/)|
|10 |[Find the Most Competitive Subsequence](src/stack_problems/find_the_most_competitive_subsequence.py)|[stack](src/stack_problems)|Medium|[LeetCode](https://leetcode.com/problems/find-the-most-competitive-subsequence/)|
|11 |[Minimum Moves to Make Array Complementary](src/array_problems/minimum_moves_to_make_array_complementary.py)|[array](src/array_problems)|Medium|[LeetCode](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/)|
|12 |[Minimize Deviation in Array](src/heap_problems/minimize_deviation_in_array.py)|[heap](src/heap_problems)|Hard|[LeetCode](https://leetcode.com/problems/minimize-deviation-in-array/)|
|13 |[Count of Matches in Tournament](src/greedy_problems/count_of_matches_in_tournament.py)|[greedy](src/greedy_problems)|Easy|[LeetCode](https://leetcode.com/problems/count-of-matches-in-tournament/)|
|14 |[Partitioning Into Minimum Number Of Deci-Binary Numbers](src/greedy_problems/partitioning_into_minimum_number_of_decibinary_numbers.py)|[greedy](src/greedy_problems)|Medium|[LeetCode](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/)|
|15 |[Stone Game VII](src/dp_problems/stone_game_vii.py)|[dp](src/dp_problems)|Medium|[LeetCode](https://leetcode.com/problems/stone-game-vii/)|
|16 |[Reformat Phone Number](src/string_problems/reformat_phone_number.py)|[string](src/string_problems)|Easy|[LeetCode](https://leetcode.com/problems/reformat-phone-number/)|
|17 |[Maximum Erasure Value](src/array_problems/maximum_erase_value.py)|[array](src/array_problems)|Medium|[LeetCode](https://leetcode.com/problems/maximum-erasure-value/)|
|18 |[Top K Frequent Elements](src/heap_problems/top_k_frequent_elements.py)|[heap](src/heap_problems)|Medium|[LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)|
|19 |[Decode XORed Array](src/bit_manipulation_problems/decode_xored_array.py)|[bit manipulation](src/bit_manipulation_problems)|Easy|[LeetCode](https://leetcode.com/problems/decode-xored-array/)|
|20 |[Swapping Nodes in a Linked List](src/list_problems/swapping_nodes_in_a_linked_list.py)|[linked lists](src/list_problems)|Medium|[LeetCode](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)|
|21 |[Minimize Hamming Distance After Swap Operations](src/greedy_problems/minimize_hamming_distance_after_swap_operations.py)|[greedy](src/greedy_problems)|Medium|[LeetCode](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/)|
|22 |[Find Minimum Time to Finish All Jobs](src/greedy_problems/find_minimum_time_to_finish_all_jobs.py)|[greedy](src/greedy_problems)|Hard|[LeetCode](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/)|
|23 |[Cat and Mouse II](src/dp_problems/cat_and_mouse_ii.py)|[dp](src/dp_problems)|Hard|[LeetCode](https://leetcode.com/problems/cat-and-mouse-ii/)|
|24 |[Latest Time by Replacing Hidden Digits](src/string_problems/latest_time_by_replacing_hidden_digits.py)|[string](src/string_problems)|Easy|[LeetCode](https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/)|
|25 |[Change Minimum Characters to Satisfy One of Three Conditions](src/string_problems/change_minimum_characters_to_satisfy_one_of_three_conditions.py)|[string](src/string_problems)|Medium|[LeetCode](https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/)|
|26 |[Find Minimum Time to Finish All Jobs](src/greedy_problems/find_minimum_time_to_finish_all_jobs.py)|[greedy](src/greedy_problems)|Hard|[LeetCode](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/)|
|27 |[Building Boxes](src/greedy_problems/find_minimum_time_to_finish_all_jobs.py)|[greedy](src/greedy_problems)|Hard|[LeetCode](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/)|
|28 |[Maximum Number of Balls in a Box](src/array_problems/maximum_number_of_balls_in_a_box.py)|[array](src/array_problems)|Easy|[LeetCode](https://leetcode.com/problems/maximum-number-of-balls-in-a-box/)|
|29 |[Restore the Array From Adjacent Pairs](src/greedy_problems/restore_the_array_from_adjacent_pairs.py)|[greedy](src/greedy_problems)|Medium|[Leetcode](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/)|
|30 |[Can You Eat Your Favorite Candy on Your Favorite Day?](src/array_problems/can_you_eat_your_favorite_candy_on_your_favorite_day.py)|[array](src/array_problems)|Medium|[Leetcode](https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/description/)|
|31 |[Palindrome Partitioning IV](src/dp_problems/palindrome_partitioning_iv.py)|[dp](src/dp_problems)|Hard|[Leetcode](https://leetcode.com/problems/palindrome-partitioning-iv/description/)|
|32 |[Minimum Changes To Make Alternating Binary String](src/greedy_problems/minimum_changes_to_make_alternating_binary_string.py)|[greedy](src/greedy_problems)|Easy|[Leetcode](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/)|
|33 |[Count Number of Homogenous Substrings](src/string_problems/count_number_of_homogenous_substrings.py)|[string](src/string_problems)|Medium|[Leetcode](https://leetcode.com/problems/count-number-of-homogenous-substrings/description/)|
|34 |[Minimum Limit of Balls in a Bag](src/heap_problems/minimum_limit_of_balls_in_a_bag.py)|[heap](src/heap_problems)|Medium|[Leetcode](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/)|
|35 |[Minimum Degree of a Connected Trio in a Graph](src/graph_problems/minimum_degree_of_a_connected_trio_in_a_graph.py)|[graph](src/graph_problems)|Hard|[Leetcode](https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/description/)|
|36 |[Merge Strings Alternately](src/string_problems/merge_strings_alternately.py)|[string](src/string_problems)|Easy|[Leetcode](https://leetcode.com/problems/merge-strings-alternately/description/)|
|37 |[Minimum Number of Operations to Move All Balls to Each Box](src/array_problems/minimum_number_of_operations_to_move_all_balls_to_each_box.py)|[array](src/array_problems)|Medium|[Leetcode](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/)|
|38 |[Maximum Score from Performing Multiplication Operations](src/dp_problems/maximum_score_from_performing_multiplication_operations.py)|[dp](src/dp_problems)|Medium|[Leetcode](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description/)|
|39 |[Maximize Palindrome Length From Subsequences](src/dp_problems/maximize_palindrome_length_from_subsequences.py)|[dp](src/dp_problems)|Hard|[Leetcode](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/description/)|
|40 |[Check if Binary String Has at Most One Segment of Ones](src/greedy_problems/check_if_binary_string_has_at_most_one_segment_of_ones.py)|[greedy](src/greedy_problems)|Easy|[Leetcode](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/)|
|41 |[Check if One String Swap Can Make Strings Equal](src/string_problems/check_if_one_string_swap_can_make_strings_equal.py)|[string](src/string_problems)|Easy|[Leetcode](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/)|
|42 |[Find Center of Star Graph](src/graph_problems/find_center_of_star_graph.py)|[graph](src/graph_problems)|Medium|[Leetcode](https://leetcode.com/problems/find-center-of-star-graph/description/)|
|43 |[Maximum Average Pass Ratio](src/heap_problems/maximum_average_pass_ratio.py)|[heap](src/heap_problems)|Medium|[Leetcode](https://leetcode.com/problems/maximum-average-pass-ratio/description/)|
|44 |[Maximum Score of a Good Subarray](src/greedy_problems/maximum_score_of_a_good_subarray.py)|[greedy](src/greedy_problems)|Hard|[Leetcode](https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/)|
|45 |[Maximum Ascending Subarray Sum](src/array_problems/maximum_ascending_subarray_sum.py)|[array](src/array_problems)|Easy|[Leetcode](https://leetcode.com/problems/maximum-ascending-subarray-sum/description/)|
|46 |[Number of Orders in the Backlog](src/greedy_problems/number_of_orders_in_the_backlog.py)|[greedy](src/greedy_problems)|Medium|[Leetcode](https://leetcode.com/problems/number-of-orders-in-the-backlog/description/)|
|47 |[Maximum Value at a Given Index in a Bounded Array](src/greedy_problems/maximum_value_at_a_given_index_in_a_bounded_array.py)|[greedy](src/greedy_problems)|Medium|[Leetcode](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/)|
|48 |[Number of Different Integers in a String](src/string_problems/number_of_different_integers_in_a_string.py)|[string](src/string_problems)|Easy|[Leetcode](https://leetcode.com/problems/number-of-different-integers-in-a-string/description/)|
|49 |[Minimum Number of Operations to Reinitialize a Permutation](src/array_problems/minimum_number_of_operations_to_reinitialize_a_permutation.py)|[array](src/array_problems)|Medium|[Leetcode](https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/description/)|
|50 |[Evaluate the Bracket Pairs of a String](src/string_problems/evaluate_the_bracket_pairs_of_a_string.py)|[string](src/string_problems)|Medium|[Leetcode](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/)|
|51 |[Maximize Number of Nice Divisors](src/greedy_problems/maximize_number_of_nice_divisors.py)|[greedy](src/greedy_problems)|Hard|[Leetcode](https://leetcode.com/problems/maximize-number-of-nice-divisors/description/)|
|52 |[Sign of the Product of an Array](src/math_problems/sign_of_the_product_of_an_array.py)|[math](src/math_problems)|Easy|[Leetcode](https://leetcode.com/problems/sign-of-the-product-of-an-array/description/)|
|53 |[Find the Winner of the Circular Game](src/array_problems/find_the_winner_of_the_circular_game.py)|[array](src/array_problems)|Medium|[Leetcode](https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/)|
|54 |[Check if the Sentence Is Pangram](src/string_problems/check_if_the_sentence_is_pangram.py)|[string](src/string_problems)|Easy|[Leetcode](https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/)|
|55 |[Maximum Ice Cream Bars](src/array_problems/maximum_ice_cream_bars.py)|[array](src/array_problems)|Medium|[Leetcode](https://leetcode.com/problems/maximum-ice-cream-bars/description/)|
|56 |[Single-Threaded CPU](src/heap_problems/singlethreaded_cpu.py)|[heap](src/heap_problems)|Medium|[Leetcode](https://leetcode.com/problems/single-threaded-cpu/description/)|
|57 |[Find XOR Sum of All Pairs Bitwise AND](src/math_problems/find_xor_sum_of_all_pairs_bitwise_and.py)|[math](src/math_problems)|Hard|[Leetcode](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/description/)||58 |[Longest Substring Of All Vowels in Order](src/string_problems/longest_substring_of_all_vowels_in_order.py)|[string](src/string_problems)|Medium|[Leetcode](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description/)|
