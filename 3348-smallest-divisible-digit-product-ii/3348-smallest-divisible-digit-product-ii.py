class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into prime factors 2, 3, 5, 7
        temp_t = t
        c2 = c3 = c5 = c7 = 0
        while temp_t % 2 == 0:
            c2 += 1
            temp_t //= 2
        while temp_t % 3 == 0:
            c3 += 1
            temp_t //= 3
        while temp_t % 5 == 0:
            c5 += 1
            temp_t //= 5
        while temp_t % 7 == 0:
            c7 += 1
            temp_t //= 7

        # Prime factors outside {2, 3, 5, 7} are impossible to form
        if temp_t > 1:
            return "-1"

        DIGIT_FACTORS = {
            0: (0, 0, 0, 0),
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        n = len(num)

        # Helper to find optimal digit counts for remaining factors in length L
        def get_min_counts(rem2, rem3, rem5, rem7, L):
            rem2, rem3, rem5, rem7 = (
                max(0, rem2),
                max(0, rem3),
                max(0, rem5),
                max(0, rem7),
            )
            best_counts = None

            # Try using k sixes (combining one 2 and one 3)
            for k in range(min(rem2, rem3) + 1):
                r2, r3 = rem2 - k, rem3 - k

                c9, c3_cnt = r3 // 2, r3 % 2
                c8, r2_rem = r2 // 3, r2 % 3
                c4 = 1 if r2_rem == 2 else 0
                c2_cnt = 1 if r2_rem == 1 else 0

                c6, c5_cnt, c7_cnt = k, rem5, rem7
                total_non_1 = (
                    c2_cnt
                    + c3_cnt
                    + c4
                    + c5_cnt
                    + c6
                    + c7_cnt
                    + c8
                    + c9
                )

                if total_non_1 > L:
                    continue

                c1 = L - total_non_1
                cand = (c1, c2_cnt, c3_cnt, c4, c5_cnt, c6, c7_cnt, c8, c9)

                # Compare digit count tuples lexicographically
                if best_counts is None:
                    best_counts = cand
                else:
                    for d in range(9):
                        if cand[d] != best_counts[d]:
                            if cand[d] > best_counts[d]:
                                best_counts = cand
                            break

            return best_counts

        def counts_to_string(counts):
            res = []
            for digit_val, count in enumerate(counts, start=1):
                if count > 0:
                    res.append(str(digit_val) * count)
            return "".join(res)

        # Step 2: Compute prefix factor counts
        pref2, pref3, pref5, pref7 = (
            [0] * (n + 1),
            [0] * (n + 1),
            [0] * (n + 1),
            [0] * (n + 1),
        )

        for i, ch in enumerate(num):
            f2, f3, f5, f7 = DIGIT_FACTORS[int(ch)]
            pref2[i + 1] = pref2[i] + f2
            pref3[i + 1] = pref3[i] + f3
            pref5[i + 1] = pref5[i] + f5
            pref7[i + 1] = pref7[i] + f7

        first_zero = num.find("0")
        if first_zero == -1:
            first_zero = n
            if (
                pref2[n] >= c2
                and pref3[n] >= c3
                and pref5[n] >= c5
                and pref7[n] >= c7
            ):
                return num

        # Step 3: Longest matching prefix search
        for i in range(n - 1, -1, -1):
            if i > first_zero:
                continue

            r2 = max(0, c2 - pref2[i])
            r3 = max(0, c3 - pref3[i])
            r5 = max(0, c5 - pref5[i])
            r7 = max(0, c7 - pref7[i])

            start_d = int(num[i]) + 1
            for d in range(start_d, 10):
                d2, d3, d5, d7 = DIGIT_FACTORS[d]
                rem2, rem3, rem5, rem7 = (
                    max(0, r2 - d2),
                    max(0, r3 - d3),
                    max(0, r5 - d5),
                    max(0, r7 - d7),
                )

                L = n - 1 - i
                counts = get_min_counts(rem2, rem3, rem5, rem7, L)
                if counts is not None:
                    return num[:i] + str(d) + counts_to_string(counts)

        # Step 4: Fallback to length > N if length N is impossible
        def get_min_len_req(c2, c3, c5, c7):
            min_len = float("inf")
            for k in range(min(max(0, c2), max(0, c3)) + 1):
                r2, r3 = max(0, c2) - k, max(0, c3) - k
                c9, c3_cnt = r3 // 2, r3 % 2
                c8, r2_rem = r2 // 3, r2 % 3
                c4 = 1 if r2_rem == 2 else 0
                c2_cnt = 1 if r2_rem == 1 else 0

                tot = (
                    c2_cnt
                    + c3_cnt
                    + c4
                    + max(0, c5)
                    + k
                    + max(0, c7)
                    + c8
                    + c9
                )
                min_len = min(min_len, tot)
            return min_len

        min_req = get_min_len_req(c2, c3, c5, c7)
        target_L = max(n + 1, min_req)
        counts = get_min_counts(c2, c3, c5, c7, target_L)
        return counts_to_string(counts)